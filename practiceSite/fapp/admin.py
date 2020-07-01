from django.contrib import admin
from fapp.models import AccessRecord, Topic, Webpage, Users, UserInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)
admin.site.register(UserInfo)