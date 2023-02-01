from django.db import models

class Branch (models.Model):
    branch_name = models.TextField()

class Floor (models.Model):
    floor_number = models.IntegerField(max_length=20)

class administrator(models.Model):
    administrator_name = models.CharField(max_length=50)

class Department (models.Model):
    dep_name = models.TextField()

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    employee_position = models.TextField()


class Computer(models.Model):
     computer_name = models.CharField(max_length=50)
     computer_serial_number = models.IntegerField(unique=True)
     computer_model = models.TextField()
     computer_mac_address = models.IntegerField(max_length=10)
     computer_invonteory = models.IntegerField(unique=True)
       

class Printer(models.Model):
    printer_ip = models.IntegerField(max_length=20)
    printer_serial = models.IntegerField(max_length=20)
    printer_model = models.TextField()
    printer_inv = models.IntegerField(max_length=20)

class Phone(models.Model):
    phone_number = models.IntegerField(max_length=20)
    phone_mac_address = models.IntegerField(max_length=10)

class Scanner(models.Model):
    scanner_serial = models.IntegerField(max_length=20)
    scanner_inv = models.IntegerField(max_length=20)


class Monitor(models.Model):
     monitor_serial = models.IntegerField(max_length=20)
     monitor_inv = models.IntegerField(max_length=20)
     monitor_model = models.TextField()