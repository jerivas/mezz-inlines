# Mezzanine inline admin demo

Quick demo to showcase the issues described in [mezzanine#1575].

## Installation

```bash
git clone https://github.com/jerivas/mezz-inlines.git
cd mezz-inlines
pip install -r requirements.txt # This will clone Mezzanine master, may take a while
# Create your own local_settings.py with DB settings
python manage.py createdb --noinput --nodata
python manage.py loaddata families.json
python manage.py runserver
```

### Sample `local_settings.py`

```python
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "<some_key>"
NEVERCACHE_KEY = "<another_key>"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
```

## Reproduce

1. Log into the admin (admin / default).
1. Go to the Stacked > Familes admin page.
1. Tabular inlines work fine, notice problems with stacked.

[mezzanine#1575]: https://github.com/stephenmcd/mezzanine/issues/1575