from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('test/', include('emoklore_charasheet_app.urls')),
    path('admin/', admin.site.urls),
]