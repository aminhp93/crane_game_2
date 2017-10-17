from django.conf.urls import url

from accounts.api import views

urlpatterns = [
	url(r'^profiles/$', views.profilelist_serializer, name='profile-list'),
	url(r'^profiles/create/$', views.profilecreate_serializer, name='profile-create'),
	url(r'^profiles/(?P<pk>\d+)/$', views.profiledetail_serializer, name='profile-detail'),
	url(r'^profiles/(?P<pk>\d+)/update/$', views.profileupdate_serializer, name='profile-update'),
	url(r'^profiles/(?P<pk>\d+)/delete/$', views.profiledelete_serializer, name='profile-delete'),

	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
]

