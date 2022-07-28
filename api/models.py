from django.db import models

class Teacher(models.Model):
    tname = models.CharField(max_length=100)
    def __str__(self):
        return self.tname

class Std(models.Model):
    standard = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="test_teacher")

    def __str__(self):
        return self.standard        

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
  
    def __str__(self):
        return self.name

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


