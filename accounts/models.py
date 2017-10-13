from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class ProfileManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)

class Profile(AbstractBaseUser, PermissionsMixin):
	email			= models.CharField(max_length=255, unique=True)
	password		= models.CharField(max_length=255)
	first_name		= models.CharField(max_length=128)
	last_name		= models.CharField(max_length=128)
	postal_code		= models.CharField(max_length=8)
	country_id 		= models.IntegerField(blank=True, null=True)
	address			= models.CharField(max_length=255)
	phone_number	= models.CharField(max_length=11)
	birthday		= models.DateField(auto_now=True)
	gender 			= models.BooleanField(default=True)
	created_at 		= models.DateTimeField(auto_now_add=True)
	updated_at 		= models.DateTimeField(auto_now=True)
	deleted_at 		= models.DateTimeField(auto_now=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = ProfileManager()

	def get_full_name(self):
		'''
		Returns the first_name plus the last_name, with a space in between.
		'''
		return self.email

	def get_short_name(self):
		'''
		Returns the short name for the user.
		'''
		return self.email

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''
		Sends an email to this User.
		'''
		send_mail(subject, message, from_email, [self.email], **kwargs)

	def __str__(self):
		return self.email


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