from django.db import models

class Department(models.Model):
    department_ID = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255)
    Bldg_no = models.IntegerField()
    Location = models.IntegerField()

    def __str__(self):
        return self.department_name

class Project(models.Model):
    project_ID = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    Start_date = models.DateField()
    due_date = models.DateField()
    department = models.OneToOneField(Department, on_delete=models.CASCADE, related_name='project')

    def __str__(self):
        return self.project_name

class Employee(models.Model):
    Employee_ID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Contact_Information = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    projects = models.ManyToManyField(Project, related_name='employees')

    def __str__(self):
        return self.Name