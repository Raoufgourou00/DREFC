from configparser import LegacyInterpolation
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.forms import widgets
import django_filters
from .models import *
from django_filters import CharFilter , DateFilter 
from django import forms
from django.contrib.auth.models import User


class StudentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Prènom',lookup_expr='icontains')
    surname = django_filters.CharFilter(label='Nom',lookup_expr='icontains')
    class Meta:
        model = Student
        fields = ['name','surname','matricule','collegelevel']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'matricule': forms.TextInput(attrs={'class':'form-control','type':'matricule','id':'exampleInputMatricule'}),
            'collegelevel': forms.Select(attrs={'class':'form-control','type':'collegelevel','id':'exampleSelectCollegelevel'}),
        }


class TeacherFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Prènom',lookup_expr='icontains')
    surname = django_filters.CharFilter(label='Nom',lookup_expr='icontains')
    class Meta:
        model = Teacher
        fields = ['id','name','surname']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
        }        



class CompanyFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(label='Nom',lookup_expr='icontains')
    address = django_filters.CharFilter(label='Adresse',lookup_expr='icontains')
    class Meta:
        model = Company
        fields = ['id','name','address','legalstatus']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'address': forms.TextInput(attrs={'class':'form-control','type':'address','id':'exampleInputAddress'}),
            'legalstatus': forms.Select(attrs={'class':'form-control','type':'legalstatus','id':'exampleSelectLegalstatus'}),
        }                



class PromoterFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Prènom',lookup_expr='icontains')
    surname = django_filters.CharFilter(label='Nom',lookup_expr='icontains')
    class Meta:
        model = Promoter
        fields = ['id','name','surname','company']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
        }        

class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Prènom',lookup_expr='icontains')
    surname = django_filters.CharFilter(label='Nom',lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ['id','name','surname']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
        }        


class Stage1cpiFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(label='Titre',lookup_expr='icontains')
    class Meta:
        model = Stage
        fields = ['id','titre','promoter','status','company']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId','placeholder':'Code'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'status': forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }   


class Stage1csFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(label='Titre',lookup_expr='icontains')
    class Meta:
        model = Stage
        fields = ['id','titre','teacher','promoter','status','company']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'teacher','id':'exampleSelectTeacher'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'status': forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }   


class Stage3csFilter(django_filters.FilterSet):
    titre = django_filters.CharFilter(label='Titre',lookup_expr='icontains')
    class Meta:
        model = Stage
        fields = ['id','titre','teacher','promoter','status','company']

        widgets = {
            'id': forms.TextInput(attrs={'class':'form-control','type':'id','id':'exampleInputId'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'teacher','id':'exampleSelectTeacher'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'status': forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }   



class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label='username',lookup_expr='icontains')
    email = django_filters.CharFilter(label='email',lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['username','email','groups']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','type':'username','id':'exampleInputUsername'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail'}),
            'groups': forms.Select(attrs={'class':'form-control','type':'groups','id':'exampleSelectGroups'}),
        }        