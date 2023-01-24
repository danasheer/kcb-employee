from django.contrib import admin

from employees import models 

to_register = [
    models.Branch,
    models.Floor,
    models.Employee,
    models.Department,
    models.Printer
]

admin.site.register(to_register)