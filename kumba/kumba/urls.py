from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scenetext.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imgtotxt/','scenetext.views.imgtotxt', name='upload'),
    url(r'^test/','scenetext.views.test', name='test'),
    url(r'^add_image$', 'scenetext.views.showAddImageForm'),
    url(r'^upload_image/', 'scenetext.views.upload_image', name='upload_image'),
    url(r'^upload/', 'scenetext.views.upload', name='upload'),
)
