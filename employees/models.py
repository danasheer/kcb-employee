from django.db import models

class Branch (models.Model):
    name = models.TextField()

class Floor (models.Model):
    floor = models.IntegerField()
    braches =  models.ForeignKey(Branch, on_delete=models.CASCADE, related_name= "floors")


class Employee (models.Model):
     name = models.CharField(max_length=50)
     sn = models.IntegerField(unique=True)
     computer_name = models.TextField(unique=True)
     inv = models.IntegerField(max_length=10)
     employee_id = models.IntegerField(unique=True)
     
class Department (models.Model):
    dep_name = models.TextField()
    floors = models.ManyToManyField(Floor, related_name="departments")
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="departments")

class Printer (models.Model):
    printsn = models.IntegerField(max_length=20)
    printers = models.ForeignKey(Department, on_delete=models.CASCADE, related_name= "printers")
