# Bandori Party

The BanG Dream! Girls Band Party database and community

#### Contribute

- [Get started: developers guide](https://github.com/MagiCircles/Circles/wiki/Developers-guide)
- [Tasks](https://github.com/MagiCircles/BanGDream/projects/1)

## Running locally

Dependencies are managed with [uv](https://docs.astral.sh/uv/) via `pyproject.toml`/`uv.lock` —
no separate virtualenv to create or activate, `uv run` handles that automatically.

```shell
# 1. Install dependencies (add --extra mysql if running against MariaDB/MySQL, prod's engine —
#    the driver package is named mysqlclient regardless of which of the two you're pointed at)
uv sync --extra mysql

# 2. Start a local database (first time: create it; after that, just start it)
docker run -d --name bangdream-mariadb \
    -e MARIADB_ROOT_PASSWORD=<password> -e MARIADB_DATABASE=bangdream -p 3307:3306 \
    mariadb:12.3 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
docker start bangdream-mariadb   # subsequent runs

# 3. Start the dev server
uv run python manage.py runserver
```
