from rest_framework.serializers import (
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
)

from accounts.models import Profile

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

class ProfileUpdateSerializer(ModelSerializer):
	class Meta:
		model = Profile
		fields = [
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