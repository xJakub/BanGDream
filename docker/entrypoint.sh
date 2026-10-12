#!/usr/bin/env bash
set -ex

# Create virtualenv at ./.venv and install dependencies
uv sync

# Activate virtualenv
source .venv/bin/activate

# Create tables, initialize database (sqlite3)
python manage.py migrate

# Clone the static repo if it doesn't exist
export ORG='xJakub'
export REPO='BanGDream'
export PROJECT='bang'

if [ ! -d $PROJECT/static ]; then
  git clone https://github.com/$ORG/$REPO-Static.git
  mv $REPO-Static $PROJECT/static
fi

# Download front-end dependencies
bower install --allow-root

# Generate the generated settings and CSS
python manage.py generate_settings
python manage.py generate_css

# Launch the server
while true
do
  echo "Starting server at http://localhost:8000/"
  python manage.py runserver 0.0.0.0:8000 || true
  echo "Waiting 5 seconds until next start..."
  sleep 5
done
