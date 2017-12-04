from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    team_id = models.CharField(max_length=20)
    bot_user_id = models.CharField(max_length=20)
    bot_access_token = models.CharField(max_length=100)
    channel_id = models.CharField(max_length=100, blank=True, null=True, default='1')


    def __str__(self):
        return self.name


class Message(models.Model):
    ts = models.CharField(max_length=100)
    text = models.TextField(max_length=2000)
    user_id = models.CharField(max_length=50)
    channel = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    workspace = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    ts= models.CharField(max_length=100)
    text= models.TextField(max_length=2000)
    user_id= models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Сообщение: %s. Ответ: %s' %(self.message, self.text)


class CustUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user

