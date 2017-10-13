from django.conf.urls import url

from accounts.api import views

urlpatterns = [
	url(r'^profiles/$', views.ProfileListAPIView.as_view(), name='profile-list'),
	url(r'^profiles/create/$', views.ProfileCreateAPIView.as_view(), name='profile-create'),
	url(r'^profiles/(?P<pk>\d+)/$', views.ProfileDetailAPIView.as_view(), name='profile-detail'),
	url(r'^profiles/(?P<pk>\d+)/update/$', views.ProfileUpdateAPIView.as_view(), name='profile-update'),
	url(r'^profiles/(?P<pk>\d+)/delete/$', views.ProfileDeleteAPIView.as_view(), name='profile-delete'),

	url(r'^users/$', views.UserListAPIView.as_view(), name='user-list'),
	url(r'^users/create/$', views.UserCreateAPIView.as_view(), name='user-create'),
	url(r'^users/(?P<pk>\d+)/$', views.UserDetailAPIView.as_view(), name='user-detail'),
	url(r'^users/(?P<pk>\d+)/update/$', views.UserUpdateAPIView.as_view(), name='user-update'),
	url(r'^users/(?P<pk>\d+)/delete/$', views.UserDeleteAPIView.as_view(), name='user-delete'),

]

