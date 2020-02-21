from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.test),
    url(r'^popular/.*$', views.test, name='popular'),
    url(r'^ask/.*$', views.test, name='ask'),
    url(r'^answer/.*$', views.test, name='answer'),
    url(r'^signup/.*$', views.test, name='signup'),
    url(r'^login/.*$', views.test, name='login'),
    url(r'^logout/.*$', views.test, name='logout'),
    url(r'^new/.*$', views.test),
    url(r'^question/(?P<question_id>[0-9]+)/$', views.test, name='question'),
]
