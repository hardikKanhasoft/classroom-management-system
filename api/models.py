from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(unique=True)
    CHOICES = (("principal","principal"),("teacher","teacher"))
    type = models.CharField(max_length=9,choices=CHOICES)

class Teacher(models.Model):
    tname = models.CharField(max_length=100)

class Std(models.Model):
    standard = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="test_teacher")      

class division(models.Model):
    div = models.CharField(max_length=20)
    def __str__(self):
        return self.div
                    
class classroom(models.Model):
    id = models.IntegerField(primary_key=True)
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    std = models.ForeignKey(Std, on_delete=models.CASCADE)
    div = models.ForeignKey(division, on_delete= models.CASCADE)
    is_monitor = models.BooleanField(default=False)

    class Meta:
        unique_together = ('roll_no', 'std', 'div')

    def save(self):
        if self.is_monitor:
            try:
                a = classroom.objects.get(is_monitor=True, std=self.std, div = self.div)
                if self != a:
                    a.is_monitor = False
                    a.save()    
            except:
                pass
        super(classroom, self).save()


