#-*-coding: utf-8 -*-
import os
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = frozenset(['lucretius.glad@gmail.com'])
SECRET_KEY = 'This string will be replaced with a proper key in production.'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = "somethingimpossibletoguess"

RECAPTCHA_USE_SSL = False
RECAPTCHA_PUBLIC_KEY = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
RECAPTCHA_PRIVATE_KEY = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'
RECAPTCHA_OPTIONS = {'theme': 'white'}

LANGUAGES = {
    'ru': u'Русский',
}

MAIL_SUPPRESS_SEND = True
MAIL_DEFAULT_SENDER = 'test@test.com'

#flask-security
SECURITY_PASSWORD_HASH = 'bcrypt'
SECURITY_PASSWORD_SALT = '$2a$16$PnnIgfMwkOjGX4SkHqSOPO'
#SECURITY_EMAIL_SENDER = ''
#SECURITY_CONFIRMABLE = ''
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False

BABEL_DEFAULT_LOCALE = 'ru'