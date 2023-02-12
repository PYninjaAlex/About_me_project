from django.db import models


class AboutMeDatabase(models.Model):
    name = models.CharField(max_length=15, blank=False)
    second_name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return f"{self.name}, {self.second_name}"
