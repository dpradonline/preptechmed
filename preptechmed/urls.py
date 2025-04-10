from . import views
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('more/', views.more, name="more"),
    path('account/', views.account, name="account"),
    path('about/', views.about, name="about"),
    path('upload/', views.upload, name="upload"),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
