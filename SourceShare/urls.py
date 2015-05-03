__author__ = 'xuweitao'
from django.conf.urls import url
from SourceShare import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'ToSFE.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url( r'^getDirectory$', views.getDirectory ,name='directory' ),
]