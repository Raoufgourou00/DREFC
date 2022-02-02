from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'matricule': forms.TextInput(attrs={'class':'form-control','type':'matricule','id':'exampleInputMatricule'}),
            'datebirth': forms.TextInput(attrs={'class':'form-control','type':'datebirth','id':'exampleInputDatebirth'}),
            'placebirth': forms.TextInput(attrs={'class':'form-control','type':'placebirth','id':'exampleInputPlacebirth'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','type':'phone','id':'exampleInputPhone'}),
            'collegelevel': forms.Select(attrs={'class':'form-control','type':'collegelevel','id':'exampleSelectCollegelevel'}),
            'user': forms.Select(attrs={'class':'form-control','type':'username','id':'exampleSelectUsername'}),
            'photo': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
        }
    
    def __init__(self, **kwargs):
        super(StudentForm, self).__init__(**kwargs)
        self.fields['user'].queryset = User.objects.filter(groups__name = 'student')

class TeacherForm(ModelForm):


    

    class Meta:
        model = Teacher
        fields = '__all__'
        
       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','type':'phone','id':'exampleInputPhone'}),
            'user': forms.Select(attrs={'class':'form-control','type':'username','id':'exampleSelectUsername'}),
            'photo': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
        }

    def __init__(self, **kwargs):
        super(TeacherForm, self).__init__(**kwargs)
        self.fields['user'].queryset = User.objects.filter(groups__name = 'teacher')


        
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'address': forms.TextInput(attrs={'class':'form-control','type':'address','id':'exampleInputAddress'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','type':'phone','id':'exampleInputPhone'}),
            'fax': forms.TextInput(attrs={'class':'form-control','type':'fax','id':'exampleInputFax'}),
            'legalstatus': forms.Select(attrs={'class':'form-control','type':'legalstatus','id':'exampleSelectLegalstatus'}),
            'website': forms.TextInput(attrs={'class':'form-control','type':'website','id':'exampleInputWebsite'}),
        }



class PromoterForm(ModelForm):
    class Meta:
        model = Promoter
        fields = '__all__'
        
       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','type':'phone','id':'exampleInputPhone'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
       
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','type':'name','id':'exampleInputName'}),
            'surname': forms.TextInput(attrs={'class':'form-control','type':'surname','id':'exampleInputSurname'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'phone': forms.TextInput(attrs={'class':'form-control','type':'phone','id':'exampleInputPhone'}),
            'user': forms.Select(attrs={'class':'form-control','type':'username','id':'exampleSelectUsername'}),
            'photo': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
        }
    def __init__(self, **kwargs):
        super(EmployeeForm, self).__init__(**kwargs)
        self.fields['user'].queryset = User.objects.filter(groups__name = 'admin')

class Stage1cpiForm(ModelForm):
    
    
    class Meta:     
        model = Stage
        fields = '__all__'
         
        widgets = {
            'type': forms.TextInput(attrs={'class':'form-control','type':'type','id':'exampleInputType','value':'1CPI'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'description': forms.Textarea(attrs={'class':'form-control','type':'description','id':'exampleFormControlTextarea1','rows':'3'}),
            'datedeb': forms.TextInput(attrs={'class':'form-control','type':'datedeb','id':'exampleInputDatebirth'}),
            'datefin': forms.TextInput(attrs={'class':'form-control','type':'datefin','id':'exampleInputDatebirth'}),
            'convention': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'rapport': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'students': forms.SelectMultiple(attrs={'class':'form-control','type':'students','id':'exampleSelectStudents'}),
            'status':  forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }

    def __init__(self, **kwargs):
        super(Stage1cpiForm, self).__init__(**kwargs)
        self.fields['students'].queryset = Student.objects.filter(collegelevel = '1CPI')

class Stage1csForm(ModelForm):
    
    
    class Meta:     
        model = Stage
        fields = '__all__'
         
        widgets = {
            'type': forms.TextInput(attrs={'class':'form-control','type':'type','id':'exampleInputType','value':'1CPI'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'description': forms.Textarea(attrs={'class':'form-control','type':'description','id':'exampleFormControlTextarea1','rows':'3'}),
            'datedeb': forms.TextInput(attrs={'class':'form-control','type':'datedeb','id':'exampleInputDatebirth'}),
            'datefin': forms.TextInput(attrs={'class':'form-control','type':'datefin','id':'exampleInputDatebirth'}),
            'convention': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'rapport': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv1': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'teacher': forms.Select(attrs={'class':'form-control','type':'teacher','id':'exampleSelectTeacher'}),
            'students': forms.SelectMultiple(attrs={'class':'form-control','type':'students','id':'exampleSelectStudents'}),
            'status':  forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }
    def __init__(self, **kwargs):
        super(Stage1csForm, self).__init__(**kwargs)
        self.fields['students'].queryset = Student.objects.filter(collegelevel = '1CS')




class Stage3csForm(ModelForm):
    
    

    
    class Meta:     
        model = Stage
        fields = '__all__'
         
        widgets = {
            'type': forms.TextInput(attrs={'class':'form-control','type':'type','id':'exampleInputType','value':'1CPI'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'description': forms.Textarea(attrs={'class':'form-control','type':'description','id':'exampleFormControlTextarea1','rows':'3'}),
            'datedeb': forms.TextInput(attrs={'class':'form-control','type':'datedeb','id':'exampleInputDatebirth'}),
            'datefin': forms.TextInput(attrs={'class':'form-control','type':'datefin','id':'exampleInputDatebirth'}),
            'convention': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'rapport': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv1': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv2': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv3': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'teacher': forms.Select(attrs={'class':'form-control','type':'teacher','id':'exampleSelectTeacher'}),
            'students': forms.SelectMultiple(attrs={'class':'form-control','type':'students','id':'exampleSelectStudents'}),
            'status':  forms.Select(attrs={'class':'form-control','type':'status','id':'exampleSelectStatus'}),
        }
    def __init__(self, **kwargs):
        super(Stage3csForm, self).__init__(**kwargs)
        self.fields['students'].queryset = Student.objects.filter(collegelevel = '3CS')


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2','groups']

    widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','type':'username','id':'exampleInputUsername'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','id':'exampleInputEmail1','placeholder':'exemple@gmail.com'}),
            'password1': forms.TextInput(attrs={'class':'form-control','type':'password1','id':'exampleInputPassword1'}),
            'password2': forms.TextInput(attrs={'class':'form-control','type':'password2','id':'exampleInputPassword2'}),
            'groups': forms.SelectMultiple(attrs={'class':'form-control','type':'groups','id':'exampleSelectGroups'}),
        }





class ValidStage(ModelForm):
    
    class Meta:     
        model = Stage
        fields = '__all__'
         
        widgets = {
            'type': forms.TextInput(attrs={'class':'form-control','type':'type','id':'exampleInputType'}),
            'titre': forms.TextInput(attrs={'class':'form-control','type':'titre','id':'exampleInputTitre'}),
            'description': forms.Textarea(attrs={'class':'form-control','type':'description','id':'exampleFormControlTextarea1','rows':'3'}),
            'datedeb': forms.TextInput(attrs={'class':'form-control','type':'datedeb','id':'exampleInputDatebirth'}),
            'datefin': forms.TextInput(attrs={'class':'form-control','type':'datefin','id':'exampleInputDatebirth'}),
            'convention': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'rapport': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv1': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv2': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'fichesuiv3': forms.FileInput(attrs={'class':'form-control-file','type':'file','id':'exampleFormControlFile1'}),
            'company': forms.Select(attrs={'class':'form-control','type':'company','id':'exampleSelectCompany'}),
            'promoter': forms.Select(attrs={'class':'form-control','type':'promoter','id':'exampleSelectPromoter'}),
            'teacher': forms.Select(attrs={'class':'form-control','type':'teacher','id':'exampleSelectTeacher'}),
            'students': forms.SelectMultiple(attrs={'class':'form-control','type':'students','id':'exampleSelectStudents'}),
            'status': forms.TextInput(attrs={'class':'form-control','type':'status','id':'exampleInputStatus','value':'Validé'}),
        }
     