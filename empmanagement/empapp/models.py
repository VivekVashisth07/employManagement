from django.db import models

class EmployDetails(models.Model):
    employe_name = models.CharField(max_length=30)
    employe_id = models.CharField(max_length=6, unique=True)
    department = models.CharField(max_length=20)
    salary = models.IntegerField(max_length=10)
    manager= models.CharField(max_length=30)
    task= models.CharField(max_length=50)
    task_in_progress= models.CharField(max_length=4)
    id_proof = models.FileField(upload_to=None)


# class EmployTask(EmployDetails):
#     task= models.CharField(max_length=50)
#     work_in_progress= models.BooleanField(max_length=4)
