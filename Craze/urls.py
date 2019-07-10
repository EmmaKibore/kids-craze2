from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^$',views.home,name= 'home'),
     url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'profile/$',views.profile,name='profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^categories/$',views.categories,name='categories'),
    url(r'^category/(\d+)/',views.category,name='category'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)