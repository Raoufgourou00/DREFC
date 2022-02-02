
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Student(models.Model):
    YEAR_IN_COLLEGE_CHOICES = [
        ('1CPI','1CPI'),
        ('2CPI','2CPI'),
        ('1CS','1CS'),
        ('2CS','2CS'),
        ('3CS','3CS'),
    ]
    user         = models.OneToOneField(User,null=True, on_delete=models.CASCADE,unique=TRUE)
    name         = models.CharField(max_length=190)
    surname      = models.CharField(max_length=190)
    datebirth    = models.DateField(null=False)
    placebirth   = models.CharField(max_length=190)
    matricule    = models.CharField(max_length=190,unique=True)
    email        = models.EmailField(max_length=190)
    phone        = models.CharField(max_length=10)
    collegelevel = models.CharField(max_length=4, choices=YEAR_IN_COLLEGE_CHOICES)
    photo        = models.ImageField(upload_to = 'images/' ,default='images/user.png',null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (self.name + ' ' + self.surname + ' ' + self.matricule + ' ' + self.collegelevel)

class Teacher(models.Model):
    user         = models.OneToOneField(User,null=True, on_delete=models.CASCADE,unique=TRUE)
    name         = models.CharField(max_length=190)
    surname      = models.CharField(max_length=190)
    email        = models.EmailField(max_length=190)
    phone        = models.CharField(max_length=10)
    photo        = models.ImageField(upload_to = 'images/' ,default='images/user.png',null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (self.name + ' ' + self.surname)


class Company(models.Model):
    LEGAL_STATUS_CHOICES = [
        ('Publique','Publique'),
        ('Privée','Privée'),
        ('Semi-Publique','Semi-Publique'),
    ]
    
    name         = models.CharField(max_length=190,unique=True)
    address      = models.CharField(max_length=190,null=True,blank=True)
    email        = models.EmailField(max_length=190)
    phone        = models.CharField(max_length=10)
    fax          = models.CharField(max_length=100,null=True,blank=True)
    legalstatus  = models.CharField(max_length=15, choices=LEGAL_STATUS_CHOICES,null=True,blank=True)
    website      = models.CharField(max_length=190,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (self.name)



class Promoter(models.Model):
    
    name         = models.CharField(max_length=190)
    surname      = models.CharField(max_length=190)
    email        = models.EmailField(max_length=190)
    phone        = models.CharField(max_length=10)
    company      = models.ForeignKey(Company, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (self.name + ' ' + self.surname + ' ' + '(' + self.company.name + ')')



class Stage(models.Model):
    
    
    STATUS_CHOICES = [
        ('En Cours','En Cours'),
        ('Annulé','Annulé'),
        ('Validé','Validé'),
        ('Délai Non Respecté','Délai Non Respecté'),
    ]
    type         = models.CharField(max_length=190,null=False)
    titre        = models.CharField(max_length=4000)
    description  = models.TextField(max_length=4000)
    datedeb      = models.DateField(null=False)
    datefin      = models.DateField(null=False)
    convention   = models.FileField(upload_to = 'files/' ,null=True,blank=True)  # all
    rapport      = models.FileField(upload_to = 'files/' ,null=True,blank=True)  # all
    fichesuiv1   = models.FileField(upload_to = 'files/' ,null=True,blank=True)  #for 1CS & 3CS
    fichesuiv2   = models.FileField(upload_to = 'files/' ,null=True,blank=True)  # 3CS
    fichesuiv3   = models.FileField(upload_to = 'files/' ,null=True,blank=True)  # 3CS
    teacher      = models.ForeignKey(Teacher, on_delete=models.CASCADE,null=True,blank=True) # for 1CS & 3CS
    promoter     = models.ForeignKey(Promoter, on_delete=models.CASCADE,null=True,blank=True) # for all
    company      = models.ForeignKey(Company, on_delete=models.CASCADE) # for all
    students     = models.ManyToManyField(Student) # for all
    status       = models.CharField(max_length=190,choices=STATUS_CHOICES,default='inprogress')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    




class Employee(models.Model):
    user         = models.OneToOneField(User,null=True, on_delete=models.CASCADE,unique=TRUE)
    name         = models.CharField(max_length=190)
    surname      = models.CharField(max_length=190)
    email        = models.EmailField(max_length=190)
    phone        = models.CharField(max_length=10)
    photo        = models.ImageField(upload_to = 'images/' ,default='images/user.png',null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    

    def __str__(self):
        return (self.name + ' ' + self.surname )