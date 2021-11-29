from django.db import models

def newRandomPassowrd():
  import random
  import string
  return''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))


class  User(models.Model):
  user_name = models.CharField(max_length = 80, unique = True, blank = False)
  password = models.CharField(max_length= 10, blank = False, default=newRandomPassowrd())
  birth_date = models.DateField()

  def __str__(self):
    return self.user_name


    