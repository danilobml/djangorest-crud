from django.db import models


class Location(models.Model):
    locationName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.location_name


class Item(models.Model):
    itemName = models.CharField(max_length=100)
    dateAdded = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(on_delete=models.CASCADE())

    def __str__(self):
        return self.itemName
