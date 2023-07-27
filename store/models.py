# store/models.py

from django.db import models

class StoreEntry(models.Model):
    name = models.CharField(max_length=100)
    entry_type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    date = models.DateField()
    quantity = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return self.name
# store/models.py


class Usage(models.Model):
    sl_no = models.CharField(max_length=50)
    date = models.DateField()
    product = models.ForeignKey(StoreEntry, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    given_by = models.CharField(max_length=100)
    taken_by = models.CharField(max_length=100)
    quantity = models.IntegerField()
    remarks = models.TextField()

    def __str__(self):
        return f"Usage {self.sl_no}"
