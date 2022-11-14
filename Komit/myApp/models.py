from django.db import models
from django.utils import timezone
# Create your models here.
class Roka(models.Model):
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='static/images/roka',default="")

	class Meta:
		ordering=('-publish',)

	def __str__(self):
		return str(self.photo)

class Prewedding(models.Model):
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='static/images/prewedding',default="")

	class Meta:
		ordering=('publish',)

	def __str__(self):
		return self.photo

class Shadi(models.Model):
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	photo=models.ImageField(upload_to='static/images/shadi',default="")

	class Meta:
		ordering=('-publish',)

	def __str__(self):
		return self.photo