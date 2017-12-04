from django.contrib import admin
from .models import Team, Message, Comment,CustUser

admin.site.register(Team)
admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(CustUser)
