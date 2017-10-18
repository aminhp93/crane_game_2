from django.conf.urls import url

from accounts.api import views

urlpatterns = [
	url(r'^profiles/$', views.ProfileListAPIView.as_view(), name='profile-list'),
	url(r'^profiles/create/$', views.ProfileCreateAPIView.as_view(), name='profile-create'),
	url(r'^profiles/(?P<pk>\d+)/$', views.ProfileDetailAPIView.as_view(), name='profile-detail'),
	url(r'^profiles/(?P<pk>\d+)/update/$', views.ProfileUpdateAPIView.as_view(), name='profile-update'),
	url(r'^profiles/(?P<pk>\d+)/delete/$', views.ProfileDeleteAPIView.as_view()	, name='profile-delete'),

	url(r'^login/$', views.LoginAPIView.as_view(), name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	# url(r'^search/$', views.search, name='search'),
	url(r'^check_email_exist/$', views.CheckEmailExist.as_view(), name='check_email_exist'),
]

