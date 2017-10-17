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
	first_name		= models.CharField(max_length=128, blank=True)
	last_name		= models.CharField(max_length=128, blank=True)
	postal_code		= models.CharField(max_length=8, null=True, blank=True)
	country_id 		= models.IntegerField(null=True, blank=True)
	address			= models.CharField(max_length=255, null=True, blank=True)
	phone_number	= models.CharField(max_length=11, null=True, blank=True)
	birthday		= models.DateField(auto_now=True, null=True, blank=True)
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
