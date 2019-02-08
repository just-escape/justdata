from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, re_path


def admin_redirect(request):
    return redirect('admin/', permanent=True)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*$', admin_redirect),
]
