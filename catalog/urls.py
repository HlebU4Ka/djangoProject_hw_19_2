from django.urls import path

from catalog.views import home_page, info_page


urlpatterns = [
    path('', home_page),
    path('info_pages/', info_page)
]