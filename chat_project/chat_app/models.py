from django.db import models
from profile_app.models import UserProfileInfo

# Create your models here.

class Message(models.Model):
	contact = models.ForeignKey(UserProfileInfo, related_name='messages', on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)

	def __repr__(self):
		return "<From: {} Text: {}>".format(self.contact.user.username, self.content[:15])

	def __str__(self):
		return self.contact.user.username


class Chat(models.Model):
	participants = models.ManyToManyField(
		UserProfileInfo, related_name='chats', blank=True)
	messages = models.ManyToManyField(Message, blank=True)

	def __repr__(self):
		return "<Chat {}: {} participants>".format(self.pk, self.messages.all().count())

	def __str__(self):
		return "Chat {}: {} participants".format(self.pk, self.messages.all().count())

