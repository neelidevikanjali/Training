from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class details(models.Model):
    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE, primary_key=True
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name

class information(models.Model):
    subject = models.ForeignKey(details, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject, self.name


