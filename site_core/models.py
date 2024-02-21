from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AssetsDB(models.Model):
    name = models.CharField(unique=True, max_length = 200)
    description = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='')
    def __str__(self):
        return self.name

class LibraryDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(AssetsDB, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'asset')