from .base import *
import dj_database_url

CSRF_COOKIE_SECURE = True

DEBUG = True

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'student_manager',
#         'USER': 'root',
#         'PASSWORD': '03041999',
#         'HOST': 'localhost',
#         'PORT': '5432'
#     }
# }

DATABASES = {'default': {}}
db_from_env = dj_database_url.config(
    conn_max_age=600, 
    default='postgres://root:03041999@postgres/student_manager'
)
DATABASES['default'].update(db_from_env)

# DATABASES = {'default': {}}
# db_from_env = dj_database_url.config(
#     conn_max_age=600, 
#     default='postgres://qreiogwdduhteo:a8aa17f83e87119d84036612762e969d09f0631ef601301727f3a8b6784c1003@ec2-18-210-64-223.compute-1.amazonaws.com:5432/d9o48scpevsf7m'
# )
# DATABASES['default'].update(db_from_env)
