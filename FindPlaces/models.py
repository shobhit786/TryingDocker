from django.db import models


class Place(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Places"



