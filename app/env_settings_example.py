import os

# *****************************
# Environment specific settings
# *****************************

# The settings below can (and should) be over-ruled by OS environment variable settings

# Flask settings                     # Generated with: import os; os.urandom(24)
SECRET_KEY = '\xb9\x8d\xb5\xc2\xc4Q\xe7\x8ej\xe0\x05\xf3\xa3kp\x99l\xe7\xf2i\x00\xb1-\xcd'
# PLEASE USE A DIFFERENT KEY FOR PRODUCTION ENVIRONMENTS!

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///../app.sqlite'

# Flask-Mail settings
MAIL_USERNAME = 'postmaster@sandboxe186d9e577054347ba3c6c6dd52932cc.mailgun.org'
MAIL_PASSWORD = '7a3faa2e7ad6212219036029394e84f6'
MAIL_DEFAULT_SENDER = '"AppName" <noreply@example.com>'
MAIL_SERVER = 'MAIL_SERVER', 'smtp.mailgun.org'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False

ADMINS = [
    '"Dan" <dan@danwins.com>',
    ]
