from django.db import models
from accounts.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class DaysOfWeek(models.Model):
    name = models.CharField(verbose_name="name", max_length=10)
    
    def __str__(self):
        return f"{self.id} - {self.name}"
    
    class Meta:
        ordering = ('id',)

class Lesson(models.Model):
    title = models.CharField(max_length = 32)
    time = models.TimeField(blank=True)
    teacher = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "teacher")
    cabinet = models.IntegerField(blank= True)
    day = models.ForeignKey(DaysOfWeek, on_delete= models.CASCADE ,related_name = "day", blank= True)

    def __str__(self):
        return f"{self.title} is teached by {self.teacher} on {self.time}"

    class Meta:
        unique_together = ('teacher')
    
class Students(models.Model):
    group_year = models.IntegerField()
    group_title = models.CharField(max_length= 10)
    group_number = models.IntegerField()
    lessons = models.ManyToManyField(Lesson, blank=True)

    def __str__(self):
        return f"{self.group_year}{self.group_title}-{self.group_number}"

    class Meta:
        unique_together = ('group_year', 'group_title', 'group_number')