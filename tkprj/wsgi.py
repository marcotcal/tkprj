"""
WSGI config for tkprj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import django
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application


#application = get_wsgi_application()


class TKWSGI(WSGIHandler):

	def __call__(self, environ, start_response):
		return super(TKWSGI, self).__call__(environ, start_response)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tkprj.settings")
django.setup(set_prefix=False)
application = TKWSGI()

