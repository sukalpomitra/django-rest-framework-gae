from django.db import models

# Create your models here.

class Eeg(models.Model):
	name = models.CharField(max_length=20)

	class Meta:
		db_table = "eeg"
