from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=300)
	author = models.CharField(max_length=300)
	year = models.IntegerField(blank=True, null=True)
	isbn = models.CharField(max_length=300, blank=True)
	edition = models.CharField(max_length=300, blank=True)

	def get_absolute_url(self):
		return f"/bookcollection/{self.pk}"

	def go_back(self):
		return f"/bookcollection/"

	
	def __str__(self):
		return self.title
