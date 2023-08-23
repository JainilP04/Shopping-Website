"""

https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#DJANGO.CORE=PACKAGE,WSGI-MODULE,GET=FUNCTION  IMPORTING FUNCTION FROM WSGI MODULE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'thelittlethings.settings')
#          FUNCTION           ENVIRONMENTAL VARIABLE      VALUE
#DEFINING SETTINGS MODULE TO ENVIRONMENTAL VERIALLE



application = get_wsgi_application()
#OBJECT CALLED