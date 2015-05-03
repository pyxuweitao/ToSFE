from django.conf.urls import include, url
# from django.contrib import admin
from SourceShare import views, urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'ToSFE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url( r'^$', views.index ),
    url( r'^SourceShare/', include( 'SourceShare.urls' ) ),
    url( r'^test/$', views.test ),
] + static( settings.STATIC_URL, document_root = settings.STATIC_ROOT )

