from django.db import models


class AboutMeDatabase(models.Model):
    """
    Main db.
    """
    name = models.CharField(max_length=15, blank=False)
    second_name = models.CharField(max_length=15, blank=False)
    age = models.IntegerField(blank=False, default=0)

    def __str__(self):
        """
        String method.
        :return:
        """
        return f"{self.name}, {self.second_name}"
