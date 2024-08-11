from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Size (models.Model):
  title = models.CharField(max_length= 30)
  def __str__(self):
    return self.title

class Pizza (models.Model):
  topping1 = models.CharField(max_length= 40 )
  topping2 = models.CharField(max_length= 40 )
  Size = models.ForeignKey(Size , on_delete = models.CASCADE )
  user = models.ForeignKey(User , on_delete = models.CASCADE , related_name= "pizza")  