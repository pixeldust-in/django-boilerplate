DEBUG = True
PRODUCTION = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or
        # 'oracle'.
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # Or path to database file if using sqlite3.
        "NAME": "",
        "USER": "",  # Not used with sqlite3.
        "PASSWORD": "",  # Not used with sqlite3.
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
