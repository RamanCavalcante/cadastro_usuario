from django.db import models

def newRandomPassword():
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

class Usuario(models.Model):
	login = models.CharField(max_length=80, unique = True, blank = False)
	senha = models.CharField(max_length=8, blank = False, default=newRandomPassword())
	data_nascimento = models.DateField()

	def __str__(self):
		return self.login
