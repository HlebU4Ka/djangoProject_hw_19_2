from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home_page, info_page


urlpatterns = [
    path('', home_page),
    path('info_page/', info_page)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)