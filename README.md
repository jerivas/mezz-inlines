# Mezzanine inline admin demo

Quick demo to showcase the issues described in stephenmcd/mezzanine#1575.

## Installation

```bash
git clone https://github.com/jerivas/mezz-inlines.git
cd mezz-inlines
pip install -r requirements.txt # This will clone Mezzanine master, may take a while
python manage.py createdb --noinput --nodata
python manage.py loaddata families.json
python manage.py runserver
```

## Reproduce

1. Log into the admin (admin / default).
1. Go to the Stacked > Familes admin page.
1. Tabular inlines work fine, notice problems with stacked.
