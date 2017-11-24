from django.db import models
from django.conf import settings

class Profiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    data_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank = True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
