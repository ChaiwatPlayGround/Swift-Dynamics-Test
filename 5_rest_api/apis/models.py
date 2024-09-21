from django.db import models

class School(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

class Classroom(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms')
    grade = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.grade}/{self.section}"

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
