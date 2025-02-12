from django.http import HttpResponse
from django.conf import settings
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

settings.configure(
    DEBUG=True,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
)

def index(request):
    return HttpResponse("Hello, World!")

from django.urls import path
urlpatterns = [path("", index)]

if __name__ == "__main__":
    execute_from_command_line(["django_hello.py", "runserver", "127.0.0.1:6006"])

