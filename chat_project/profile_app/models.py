from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(blank=True)
	friends = models.ManyToManyField('self', blank=True)

	def __repr__(self):
		return "<User: {}>".format(self.user.username)

	def __str__(self):
		return '{}'.format(self.user.username)