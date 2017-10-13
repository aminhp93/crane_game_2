from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
)

from accounts.models import User, Profile


class ProfileListSerializer(ModelSerializer):
	users = SerializerMethodField()
	class Meta:
		model = Profile
		fields = [
			'id',
			'email',
			'password',
			'first_name',
			'last_name',
			'postal_code',
			'country_id',
			'address',
			'phone_number',
			'birthday',
			'gender',
			'created_at',
			'updated_at',
			'deleted_at',
			'users'
		]

	def get_users(self, obj):
		users_qs = obj.user_set.all()
		users = UserSerializer(users_qs, many=True).data
		return users

class ProfileSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = [
			'id',
			'email',
			'password',
			'first_name',
			'last_name',
			'postal_code',
			'country_id',
			'address',
			'phone_number',
			'birthday',
			'gender',
			'created_at',
			'updated_at',
			'deleted_at'
		]

class UserListSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'profile',
			'nick_name',
			'posessing_points',
			'posessing_tickets',
			'rank',
			'is_mail_magazine',
			'is_confirmed_by_phone',
			'registered_at',
			'last_updated_at',
			'withdrawed_at',
			'is_withdrawed',
			'platform_id',
			'is_first_time_browser_benefit',
			'is_first_tiem_app_benefit',
			'created_at',
			'updated_at',
		]


class UserSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'id',
			'profile',
			'nick_name',
			'posessing_points',
			'posessing_tickets',
			'rank',
			'is_mail_magazine',
			'is_confirmed_by_phone',
			'registered_at',
			'last_updated_at',
			'withdrawed_at',
			'is_withdrawed',
			'platform_id',
			'is_first_time_browser_benefit',
			'is_first_tiem_app_benefit',
			'created_at',
			'updated_at',
		]

