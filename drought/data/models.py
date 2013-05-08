from django.db import models

class Drought(models.Model):

	rowid = models.CharField(max_length=12, primary_key=True)
	date = models.DateField(blank=True, null=True)
	#none = models.FloatField(blank=True, null=True)
	#D0D4 = models.FloatField(blank=True, null=True)
	#D1D4 = models.FloatField(blank=True, null=True)
	#D2D4 = models.FloatField(blank=True, null=True)
	D3D4 = models.FloatField(blank=True, null=True)
	#D4 = models.FloatField(blank=True, null=True)

	class Meta:
		db_table = 'drought_data'

	# The __unicode__ method defines how an individual instance of this class
	# will represent itself as a string.
	def __unicode__(self):
		return unicode(self.rowid)