from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # if user is deleted then also delete the profile but if we delete the profile then user wont delte
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

        # this ll also change in database lets migrate
        # error after trying make migrations its say instll pillow which works on images in python
