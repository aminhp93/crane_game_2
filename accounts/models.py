from django.db import models


class Profile(models.Model):
	email			= models.CharField(max_length=256)
	password		= models.CharField(max_length=256)
	first_name		= models.CharField(max_length=128)
	last_name		= models.CharField(max_length=128)
	postal_code		= models.CharField(max_length=8)
	country_id 		= models.IntegerField()
	address			= models.CharField(max_length=512)
	phone_number	= models.CharField(max_length=11)
	birthday		= models.DateField(auto_now=True)
	gender 			= models.BooleanField(default=True)
	created_at 		= models.DateTimeField(auto_now_add=True)
	updated_at 		= models.DateTimeField(auto_now=True)
	deleted_at 		= models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} {}".format(self.first_name, self.last_name)


class User(models.Model):
	profile 						= models.ForeignKey(Profile)
	nick_name 						= models.CharField(max_length=128)
	posessing_points				= models.IntegerField()
	posessing_tickets 				= models.IntegerField()
	rank 							= models.IntegerField()
	is_mail_magazine 				= models.BooleanField(default=False)
	is_confirmed_by_phone 			= models.BooleanField(default=False)
	registered_at					= models.DateTimeField(auto_now_add=True)
	last_updated_at					= models.DateTimeField(auto_now=True)
	withdrawed_at					= models.DateTimeField(auto_now_add=True)
	signup_at						= models.DateTimeField(auto_now_add=True)
	is_withdrawed					= models.BooleanField(default=False)
	platform_id						= models.IntegerField()
	is_first_time_browser_benefit 	= models.BooleanField(default=False)
	is_first_tiem_app_benefit 		= models.BooleanField(default=False)
	created_at						= models.DateTimeField(auto_now_add=True)
	updated_at  					= models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.nick_name