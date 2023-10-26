from django.db import models


# Create your models here.
class PersonalData(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    classroom_number = models.IntegerField(default=(3))
    recording_number = models.IntegerField(default=(2))

    def __str__(self):
        return f"{self.name}: classroom {self.classroom_number} on age{self.age}"


class ClassSchedule(models.Model):
    topic = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=(2))
    classroom = models.ForeignKey(PersonalData, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.topic} - {self.date} - {self.start_time} - {self.classroom}"




#class Huawei(models.Model):
#    topic = models.CharField()
#    recording_number = models.ForeignKey(PersonalData, on_delete=models.CASCADE)

#    def __str__(self):
#        return f"{self.name}: recording_number {self.recording_number}"


