DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'tinyurl'
DATABASE_USER = 'psql_admin'
DATABASE_PASSWORD = 'psql_admin'
DATABASE_HOST = 'localhost'
DATABASE_PORT = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.%s' %DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}