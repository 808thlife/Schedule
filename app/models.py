from django.db import models

from accounts.models import User

# Create your models here.

class Lesson(models.Model):
    title = models.CharField(max_length = 32, default = "Write Description of this class (Who is the teacher? Who teacher going to teach and what subject etc...)" )
    time = models.CharField(max_length=12)
    teacher = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "teacher")
    cabinet = models.IntegerField()
    description = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return f"{self.title} is teached by {self.teacher} on {self.time}"
    
class Students(models.Model):
    group_year = models.IntegerField()
    group_title = models.CharField(max_length= 10)
    group_number = models.IntegerField()
    lessons = models.ManyToManyField(Lesson)

    def __str__(self):
        return self.group_title