from django.db import models
import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return (f"{type(self).__name__}(name={self.name}, "
                f"floor_number={self.floor_number}, "
                f"room_number={self.room_number})")


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=datetime.time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return (f"{type(self).__name__}(title={self.title}, "
                f"start_time={self.start_time}, date={self.date}, "
                f"duration={self.duration})")


