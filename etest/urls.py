
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('register/', resgister, name='resgister'),
    path('test/', test, name='test'),
    path('logout', logout_button, name='logout'),
    path('audio-file', audio_file, name='audio_file'),
]
urlpatterns = urlpatterns+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)