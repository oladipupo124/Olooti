from django.db import models


class Event(models.Model):
    EVENT_CHOICES = [("Wedding", "Wedding"),
                     ("Naming Ceremony", "Naming Ceremony"),
                     ("Birthday", "Birthday"),
                     ("Graduation", "Graduation"),
                     ("Hang-out", "Hang-out"),
                     ("Others", "Others")]

    event_type = models.CharField(choices=EVENT_CHOICES, max_length=50)
    date = models.DateField()
    location = models.CharField(max_length=100)
    expected_number = models.IntegerField()
    budget_range = models.IntegerField()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return "{}({})".format(self.id, self.location)
