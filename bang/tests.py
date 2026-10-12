# -*- coding: utf-8 -*-
"""
Characterization/smoke tests for Bandori Party.

These exist to catch "the site is broken" during the Python 2->3 / Django 1.7->5.2 migration,
not to verify business logic in detail. Kept deliberately small: each test creates its own
minimal data (never relies on any transient dev snapshot), so they stay meaningful
regardless of what's actually in the dev database at the time.
"""
from django.contrib.auth.models import User
from django.test import TestCase

from magi.item_model import get_item_url
from bang import models


class HomePageTestCase(TestCase):
    def test_home_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


class CollectionListPagesTestCase(TestCase):
    """List pages should render without error even with no data in them."""

    def test_member_list_page_loads(self):
        response = self.client.get('/members/')
        self.assertEqual(response.status_code, 200)

    def test_card_list_page_loads(self):
        response = self.client.get('/cards/')
        self.assertEqual(response.status_code, 200)

    def test_event_list_page_loads(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)


class ItemDetailPageTestCase(TestCase):
    """Detail pages for a freshly-created, minimal item of each core model."""

    def setUp(self):
        self.owner = User.objects.create_user(username='detail_owner', password='testpass123')

    def test_member_detail_page_loads(self):
        member = models.Member.objects.create(
            owner=self.owner, name=u'Test Member', japanese_name=u'Test Member',
            image=u'test.png', square_image=u'test.png')
        response = self.client.get(get_item_url(member))
        self.assertEqual(response.status_code, 200)

    def test_card_detail_page_loads(self):
        member = models.Member.objects.create(
            owner=self.owner, name=u'Test Member For Card', japanese_name=u'Test Member For Card',
            image=u'test.png', square_image=u'test.png')
        card = models.Card.objects.create(id=1, owner=self.owner, member=member, i_rarity=1, i_attribute=1)
        response = self.client.get(get_item_url(card))
        self.assertEqual(response.status_code, 200)

    def test_event_detail_page_loads(self):
        event = models.Event.objects.create(owner=self.owner, name=u'Test Event', japanese_name=u'Test Event')
        response = self.client.get(get_item_url(event))
        self.assertEqual(response.status_code, 200)


class SignupLoginLogoutTestCase(TestCase):
    def test_signup_and_login_pages_render(self):
        # GET, not just POST - the form templates only render on GET (or a failed POST),
        # and a POST-only test can pass while the actual signup/login page is broken.
        self.assertEqual(self.client.get('/signup/').status_code, 200)
        self.assertEqual(self.client.get('/login/').status_code, 200)

    def test_signup_then_login_then_logout(self):
        signup_response = self.client.post('/signup/', {
            'username': 'newtestuser',
            'email': 'newtestuser@example.com',
            'password': 'testpass123',
        })
        self.assertIn(signup_response.status_code, (302, 200))
        self.assertTrue(User.objects.filter(username='newtestuser').exists())

        self.client.logout()

        login_response = self.client.post('/login/', {
            'username': 'newtestuser',
            'password': 'testpass123',
        })
        self.assertIn(login_response.status_code, (302, 200))

        profile_response = self.client.get('/')
        self.assertEqual(profile_response.status_code, 200)
        self.assertTrue(profile_response.wsgi_request.user.is_authenticated)

        self.client.logout()


class APITestCase(TestCase):
    def test_api_root_loads(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_api_cards_endpoint_loads(self):
        response = self.client.get('/api/cards/')
        self.assertEqual(response.status_code, 200)
