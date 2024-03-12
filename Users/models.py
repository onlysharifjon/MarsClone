from  django.db import models

class StudentModel(models.Model):
    modme_id = models.BigIntegerField(unique=True)
    password = models.BigIntegerField(default=4321)
    name = models.CharField(max_length=32)
    coins = models.IntegerField()
    student_group = models.IntegerField(null=True)

    def str(self):
        return self.name

class Teachers(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)
    direc = (
        ("Fronted", 'Fronted'),
        ("Backend", 'Backend'),
        ("Design", 'Design'),
        ("Starter", 'Starter')
    )
    directory = models.CharField(max_length=200, choices=direc)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    students = models.ManyToManyField( StudentModel )
    coins = models.IntegerField()

    def str(self):
        return self.name