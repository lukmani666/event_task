from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    image = models.ImageField(upload_to='event_images/')
    venue_name = models.CharField(max_length=200)
    venue_address = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def __str__(self):
        return self.title


