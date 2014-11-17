#encoding=utf-8
"""
WSGI config for eatit project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
# 定义路径,导入第三方库
root = os.path.dirname(__file__)
# 两者取其一
sys.path.insert(0, os.path.join(root, '../site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eatit.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
