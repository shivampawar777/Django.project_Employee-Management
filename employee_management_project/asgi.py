import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_management_project.settings')

application = get_asgi_application()
