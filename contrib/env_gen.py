#!/env/bin/env python

"""
Django SECRET_KEY generator.
"""
from django.utils.crypto import get_random_string


chars = "us60t%y4js9=p6zr430c6od_#z9nn5sb-tqrog07)1og(88gz*"

CONFIG_STRING = """
NOME_PROJETO=
URL_SITE=
DEBUG=True
SECRET_KEY=%s
ALLOWED_HOSTS=127.0.0.1, .localhost
#DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
DEFAULT_FROM_EMAIL=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_HOST=
EMAIL_SERVER=
EMAIL_PORT=
EMAIL_USE_TLS=
""".strip() % get_random_string(
    50, chars
)

# Writing our configuration file to '.env'
with open(".env", "w") as configfile:
    configfile.write(CONFIG_STRING)
