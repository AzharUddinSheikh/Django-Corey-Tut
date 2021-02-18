from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # if user is deleted then also delete the profile but if we delete the profile then user wont delte
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # this func run after save it ll reduced the size of our image
    def save(self):
        super().save()

        # first open the image
        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100, 100)
            img.thumbnail(output_size)
            img.save(self.image.path)

        # this ll also change in database lets migrate
        # error after trying make migrations its say instll pillow which works on images in python
