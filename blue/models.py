from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
# Create your models here.
class Blue(models.Model):
    title = models.CharField(_("title"),max_length=25)
    content = models.TextField(_("content"))
    app_name = models.CharField(_("app_name"),max_length=25)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title