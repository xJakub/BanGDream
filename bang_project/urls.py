from django.urls import include, re_path
from django.contrib import admin
from rest_framework import routers
import api.views as api_views

handler500 = 'magi.views.handler500'
handler403 = 'magi.views.handler403'

router = routers.DefaultRouter()

router.register(r'members', api_views.MemberViewSet)
router.register(r'memberids', api_views.MemberIDViewSet)
router.register(r'cards', api_views.CardViewSet)
router.register(r'cardids', api_views.CardIDViewSet)
router.register(r'events', api_views.EventViewSet)
router.register(r'costumes', api_views.CostumeViewSet)
router.register(r'areaitems', api_views.AreaItemViewSet)
router.register(r'assets', api_views.AssetViewSet)
router.register(r'items', api_views.ItemViewSet)

urlpatterns = [
    re_path(r'^', include('magi.urls')),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
]
