from django.conf.urls import url
from .views import *
from django.conf.urls import url, include

app_name = "libraryapp"

urlpatterns = [
    url(r'^$', book_list, name='home'),
    url(r'^books$', book_list, name='book'),
    url(r'^librarians$', list_librarians, name='librarians'),
    url(r'^libraries$', list_libraries, name='libraries'),
    url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout_user, name='logout'),
]