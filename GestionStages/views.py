from turtle import st
from urllib.request import Request
from webbrowser import get
from django.core.exceptions import FieldDoesNotExist
from django.db.models import query
from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.template import context
from .models import *
from django.forms import inlineformset_factory
from .filters import *
from .forms import *
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import  HttpResponseNotFound
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate ,login  , logout 
from django.contrib.auth.decorators import  login_required
from django.db.models import Q
from itertools import chain
from .decorators import *
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.views.generic import View

from DREFC.utils import render_to_pdf #created in step 4
from django.template.loader import get_template

from django.db.models import Count
import os
from django.conf import settings
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
  



def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path



@login_required(login_url='login')
def render_pdf_view(request,pk):

    user = User.objects.get(username = pk)
    
    template_path = 'convention.html'
    context = {'user': user}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="convention.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response









@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def home(request):

    avg_company_stages =  (Stage.objects
    .values(
    'company',
    )
    .filter(
    type = '3CS',
    )
    .annotate(
    nb=Count('id'),
    )
    )

    avg_company_stagiaires = (Stage.objects
    .values(
    'company',
    )
    .annotate(
    total=Count('students'),
    )
    .order_by()
    )
    
    companies = Company.objects.all()
    print(avg_company_stagiaires)

    all_stages = Stage.objects.all()
    count_all_stages = all_stages.count()
    all_students = Student.objects.all()
    count_all_students = all_students.count()  
    all_companies = Company.objects.all()
    count_all_companies = all_companies.count()
    stages = Stage.objects.order_by("datedeb")[:10]
    students = Student.objects.order_by("id")[:10]
    hovered1 = 'hovered'
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'stages'     : stages,
        'count_all_stages' : count_all_stages,
        'count_all_students' : count_all_students,
        'count_all_companies' : count_all_companies,
        'students' : students,
        'avg_company_stages' : avg_company_stages,
        'avg_company_stagiaires' : avg_company_stagiaires ,
        'companies' : companies ,
        }
    return render(request , 'home.html',context)  




@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def students(request):
    hovered1 = ''
    hovered2 = 'hovered'
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    students = Student.objects.all()
    MyFilter = StudentFilter(request.GET,queryset=students)
    students = MyFilter.qs
    count_students = students.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'students'   : students,
        'MyFilter'   : MyFilter,
        'count_students' : count_students, }
    return render(request , 'students.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createstudent(request):
    hovered1 = ''
    hovered2 = 'hovered'
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    form = StudentForm()
    if request.method == 'POST':
        #print(request.POST)
        form = StudentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('students')


    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'studentform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatestudent(request,pk):
    hovered1 = ''
    hovered2 = 'hovered'
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    student  = Student.objects.get(id=pk)
    form = StudentForm(instance=student)
    if request.method == 'POST':
        #print(request.POST)
        form = StudentForm(data=request.POST, files=request.FILES,instance=student)
        if form.is_valid():
            form.save()
            return redirect('students')
    
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'studentform.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletestudent(request,pk):
    hovered1 = ''
    hovered2 = 'hovered'
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    who = 'Etudiant'
    student  = Student.objects.get(id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'student'    : student,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  







@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def teachers(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = 'hovered'
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    teachers = Teacher.objects.all()
    MyFilter = TeacherFilter(request.GET,queryset=teachers)
    teachers = MyFilter.qs
    count_teachers = teachers.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'teachers'   : teachers,
        'MyFilter'   : MyFilter,
        'count_teachers' : count_teachers, }
    return render(request , 'teachers.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createteacher(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = 'hovered'
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    form = TeacherForm()
    if request.method == 'POST':
        #print(request.POST)
        form = TeacherForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teachers')


    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'teacherform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updateteacher(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = 'hovered'
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    teacher  = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        #print(request.POST)
        form = TeacherForm(data=request.POST, files=request.FILES,instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teachers')
    
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'teacherform.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deleteteacher(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = 'hovered'
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    who = 'Encadreur'
    teacher  = Teacher.objects.get(id=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'teacher'    : teacher,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  








@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def companies(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = 'hovered'
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    companies = Company.objects.all()
    MyFilter = CompanyFilter(request.GET,queryset=companies)
    companies = MyFilter.qs
    count_companies = companies.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'companies'   : companies,
        'MyFilter'   : MyFilter,
        'count_companies' : count_companies,}
    return render(request , 'companies.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createcompany(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = 'hovered'
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    form = CompanyForm()

    if request.method == 'POST':
        #print(request.POST)
        form = CompanyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies')


    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'companyform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatecompany(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = 'hovered'
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    company  = Company.objects.get(id=pk)
    form = CompanyForm(instance=company)
    if request.method == 'POST':
        #print(request.POST)
        form = CompanyForm(data=request.POST,instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies')
    
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'companyform.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletecompany(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = 'hovered'
    hovered6 = ''
    hovered7 = ''
    hovered8 = ''
    who = 'Entreprise'
    company  = Company.objects.get(id=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('companies')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'company'    : company,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  









@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def promoters(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = 'hovered'
    hovered7 = ''
    hovered8 = ''
    promoters = Promoter.objects.all()
    MyFilter = PromoterFilter(request.GET,queryset=promoters)
    promoters = MyFilter.qs
    count_promoters = promoters.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'promoters'   : promoters,
        'MyFilter'   : MyFilter,
        'count_promoters' : count_promoters,}
    return render(request , 'promoters.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createpromoter(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = 'hovered'
    hovered7 = ''
    hovered8 = ''
    form = PromoterForm()

    if request.method == 'POST':
        #print(request.POST)
        form = PromoterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('promoters')


    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'promoterform.html',context) 

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatepromoter(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = 'hovered'
    hovered7 = ''
    hovered8 = ''
    promoter  = Promoter.objects.get(id=pk)
    form = PromoterForm(instance=promoter)
    if request.method == 'POST':
        #print(request.POST)
        form = PromoterForm(data=request.POST,instance=promoter)
        if form.is_valid():
            form.save()
            return redirect('promoters')
    
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'promoterform.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletepromoter(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = 'hovered'
    hovered7 = ''
    hovered8 = ''
    who = 'Promoteur'
    promoter  = Promoter.objects.get(id=pk)
    if request.method == 'POST':
        promoter.delete()
        return redirect('promoters')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'promoter'    : promoter,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  







@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def stages1cpi(request):
    
    stages1cpi = Stage.objects.filter(type='1CPI') 
    companies = Company.objects.all()
    promoters = Promoter.objects.all()
    MyFilter = Stage1cpiFilter(request.GET,queryset=stages1cpi)
    stages1cpi = MyFilter.qs
    count_stages1cpi = stages1cpi.count()
    context = {
        'stages1cpi'   : stages1cpi,
        'companies'  : companies, 
        'promoters'  : promoters,
        'MyFilter'   : MyFilter,
        'count_stages1cpi' : count_stages1cpi,}
    return render(request , 'stages1cpi.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createstage1cpi(request):
    
    form = Stage1cpiForm()
    if request.method == 'POST':
        form = Stage1cpiForm(data=request.POST, files=request.FILES)
        if(form.is_valid):
            #print(request.POST)
            form.save()
            return redirect('stages1cpi')

    context = {
        'form'       : form,          
    }
    
    return render(request , 'stage1cpiform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatestage1cpi(request,pk):
    
    stage = Stage.objects.get(id=pk)
    form = Stage1cpiForm(instance=stage)
    if request.method == 'POST':
        form = Stage1cpiForm(data=request.POST, files=request.FILES,instance=stage)
        if(form.is_valid):
            print(request.POST)
            form.save()
            return redirect('stages1cpi')

    context = {
        'form'       : form,   
    }
    
    return render(request , 'stage1cpiform.html',context) 
    
@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletestage1cpi(request,pk):
    
    who = 'stage1cpi'
    stage  = Stage.objects.get(id=pk)
    if request.method == 'POST':
        stage.delete()
        return redirect('stages1cpi')

    context = {
        'who'        : who,
        'stage'      : stage,
        }
    return render(request , 'deletestage.html',context)  


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def stages1cs(request):
    
    companies = Company.objects.all()
    promoters = Promoter.objects.all()
    teachers  = Teacher.objects.all()  
    stages1cs = Stage.objects.filter(type='1CS') 
    MyFilter = Stage1csFilter(request.GET,queryset=stages1cs)
    stages1cs = MyFilter.qs
    count_stages1cs = stages1cs.count()
    context = {
        'stages1cs'   : stages1cs,
        'MyFilter'   : MyFilter,
        'companies'  : companies, 
        'promoters'  : promoters,
        'teachers'   : teachers,
        'count_stages1cs' : count_stages1cs,}
    return render(request , 'stages1cs.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createstage1cs(request):
    
    form = Stage1csForm()
    if request.method == 'POST':
        form = Stage1csForm(data=request.POST, files=request.FILES)
        if(form.is_valid):
            #print(request.POST)
            form.save()
            return redirect('stages1cs')

    context = {
        'form'       : form,        
    }
    
    return render(request , 'stage1csform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatestage1cs(request,pk):
    
    stage = Stage.objects.get(id=pk)
    form = Stage1csForm(instance=stage)
    if request.method == 'POST':
        form = Stage1csForm(data=request.POST, files=request.FILES,instance=stage)
        if(form.is_valid):
            print(request.POST)
            form.save()
            return redirect('stages1cs')

    context = {
        'form'       : form,   
    }
    
    return render(request , 'stage1csform.html',context) 
    
@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletestage1cs(request,pk):
    
    who = 'stage1cs'
    stage  = Stage.objects.get(id=pk)
    if request.method == 'POST':
        stage.delete()
        return redirect('stages1cs')

    context = {
        'who'        : who,
        'stage'      : stage,
        }
    return render(request , 'deletestage.html',context)  




@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def stages3cs(request):
    
    companies = Company.objects.all()
    promoters = Promoter.objects.all()
    teachers  = Teacher.objects.all()  
    stages3cs = Stage.objects.filter(type='3CS') 
    MyFilter = Stage1csFilter(request.GET,queryset=stages3cs)
    stages3cs = MyFilter.qs
    count_stages3cs = stages3cs.count()
    context = {
        'stages3cs'   : stages3cs,
        'MyFilter'   : MyFilter,
        'companies'  : companies, 
        'promoters'  : promoters,
        'teachers'   : teachers,
        'count_stages3cs' : count_stages3cs,}
    return render(request , 'stages3cs.html',context)  

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createstage3cs(request):
    
    form = Stage3csForm()
    if request.method == 'POST':
        form = Stage3csForm(data=request.POST, files=request.FILES)
        if(form.is_valid):
            #print(request.POST)
            form.save()
            return redirect('stages3cs')

    context = {
        'form'       : form,        
    }
    
    return render(request , 'stage3csform.html',context) 


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updatestage3cs(request,pk):
    
    stage = Stage.objects.get(id=pk)
    form = Stage3csForm(instance=stage)
    if request.method == 'POST':
        form = Stage3csForm(data=request.POST, files=request.FILES,instance=stage)
        if(form.is_valid):
            print(request.POST)
            form.save()
            return redirect('stages3cs')

    context = {
        'form'       : form,   
    }
    
    return render(request , 'stage3csform.html',context) 
    
@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deletestage3cs(request,pk):
    
    who = 'stage3cs'
    stage  = Stage.objects.get(id=pk)
    if request.method == 'POST':
        stage.delete()
        return redirect('stages3cs')

    context = {
        'who'        : who,
        'stage'      : stage,
        }
    return render(request , 'deletestage.html',context)  












@notLoggedUsers
def userLogin(request):  
  
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username=username, password=password)
            if user is not None:
             login(request, user)
             return redirect('home')
            else:
                messages.info(request, 'Credentials error')
    
        context = {}

        return render(request , 'login.html', context )



@login_required(login_url='login')
def userLogout(request):  
    logout(request)
    return redirect('login') 




@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def employees(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = 'hovered'
    employees = Employee.objects.all()
    MyFilter = EmployeeFilter(request.GET,queryset=employees)
    employees = MyFilter.qs
    count_employees = employees.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'employees'   : employees,
        'MyFilter'   : MyFilter,
        'count_employees' : count_employees, }
    return render(request , 'employees.html',context)  



@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createemployee(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = 'hovered'
    form = EmployeeForm()

    if request.method == 'POST':
        #print(request.POST)
        form = EmployeeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees')


    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'employeeform.html',context) 

@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updateemployee(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = 'hovered'
    employee  = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        #print(request.POST)
        form = EmployeeForm(data=request.POST, files=request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees')
    
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'form'       : form,
        }
    return render(request , 'employeeform.html',context)  



@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deleteemployee(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = ''
    hovered8 = 'hovered'
    who = 'Employee'
    employee  = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'employee'    : employee,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  





@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def users(request):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = 'hovered'
    groups = Group.objects.all()
    users = User.objects.all()
    MyFilter = UserFilter(request.GET,queryset=users)
    users = MyFilter.qs
    count_users = users.count()
    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'users'   : users,
        'groups'  : groups,
        'MyFilter'   : MyFilter,
        'count_users' : count_users,}
    return render(request , 'users.html',context)  


@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def createuser(request):   
            form = CreateNewUser()
            if request.method == 'POST': 
                form = CreateNewUser(request.POST)
                group = request.POST.get('groups')
                if form.is_valid():
                    user = form.save()
                    group2 = Group.objects.get(id=group)
                    user.groups.add(group2)
                    #username = form.cleaned_data.get('username')
                    #messages.success(request , username + ' Created Successfully !')
                    return redirect('users')
                       
            context = {'form':form}

            return render(request ,'userform.html', context )



@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def updateuser(request,pk):

    user = User.objects.get(id=pk)
    form = CreateNewUser(instance=user)
    if request.method == 'POST': 
       
        form = CreateNewUser(data=request.POST,instance=user)
        group = request.POST.get('groups')
        if form.is_valid():
            user = form.save()
            user.groups.clear()
            group2 = Group.objects.get(id=group)
            user.groups.add(group2)
            #username = form.cleaned_data.get('username')
            #messages.success(request , username + ' Created Successfully !')
            return redirect('users')
                       
    context = {'form':form}
    return render(request , 'userform.html',context)  



@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def deleteuser(request,pk):
    hovered1 = ''
    hovered2 = ''
    hovered3 = ''
    hovered4 = ''
    hovered5 = ''
    hovered6 = ''
    hovered7 = 'hovered'
    hovered8 = ''
    who = 'Utilisateur'
    user  = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')

    context = {
        'hovered1'   : hovered1,
        'hovered2'   : hovered2,
        'hovered3'   : hovered3,
        'hovered4'   : hovered4,
        'hovered5'   : hovered5,
        'hovered6'   : hovered6,
        'hovered7'   : hovered7,
        'hovered8'   : hovered8,
        'user'    : user,
        'who'        : who,
        }
    return render(request , 'delete.html',context)  




@login_required(login_url='login')
def pdf_view(request,pk,b):

    try:
        obj = Stage.objects.get(id=pk)
        fs = FileSystemStorage()
        if b == 0:
            filename = obj.convention.name
        else:
            if b == 1:
                filename = obj.rapport.name
            else:
                if b == 2:
                    filename = obj.fichesuiv1.name
                else:
                    if b == 3:  
                        filename = obj.fichesuiv2.name
                    else:
                        filename = obj.fichesuiv3.name    
           
        if fs.exists(filename):
            with fs.open(filename) as pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                #response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"' #user will be prompted with the browser’s open/save file
                response['Content-Disposition'] = 'inline; filename="mypdf.pdf"' #user will be prompted display the PDF in the browser
                return response
    except PermissionError:
        return HttpResponseNotFound('Fichier Non Encore Dispanible !')





@login_required(login_url='login')
@forstudent(allowedGroups=['student'])
def studenthome(request):
    stages = Stage.objects.all()
    context = {
        'stages' : stages,
    }
    return render(request , 'studenthome.html',context)  




@login_required(login_url='login')
@forstudent(allowedGroups=['student'])
def validstage(request,pk):

    stage = Stage.objects.get(id=pk)
    form = ValidStage(instance=stage)
    if request.method == 'POST': 
        form = ValidStage(data=request.POST,files=request.FILES,instance=stage)
        if form.is_valid():
            form.save()
            return redirect('studenthome')
                       
    context = {'form':form}
    return render(request , 'validstage.html',context)  

@login_required(login_url='login')
@forstudent(allowedGroups=['student'])
def vosstages(request):
    stages = Stage.objects.all()
    context = {
        'stages' : stages,
    }
    return render(request , 'vosstages.html',context)  



@login_required(login_url='login')
@forstudent(allowedGroups=['student'])
def password(request,pk):

    user = User.objects.get(id=pk)
    form = CreateNewUser(instance=user)
    if request.method == 'POST': 
       
        form = CreateNewUser(data=request.POST,instance=user)
        group = request.POST.get('groups')
        if form.is_valid():
            user = form.save()
            user.groups.clear()
            group2 = Group.objects.get(id=group)
            user.groups.add(group2)
            #username = form.cleaned_data.get('username')
            #messages.success(request , username + ' Created Successfully !')
            return redirect('studenthome')
                       
    context = {'form':form}
    return render(request , 'password.html',context)  












@login_required(login_url='login')
@foradmin(allowedGroups=['admin'])
def passwordemp(request,pk):


    user = User.objects.get(id=pk)
    form = CreateNewUser(instance=user)
    if request.method == 'POST': 
       
        form = CreateNewUser(data=request.POST,instance=user)
        group = request.POST.get('groups')
        if form.is_valid():
            user = form.save()
            user.groups.clear()
            group2 = Group.objects.get(id=group)
            user.groups.add(group2)
            #username = form.cleaned_data.get('username')
            #messages.success(request , username + ' Created Successfully !')
            return redirect('home')
                       
    context = {'form':form}
    return render(request , 'passwordemp.html',context)  





def changephoto(request,pk,r):
    
    if r == 2:
        actor = Student.objects.get(id=pk)
        form = StudentForm(instance=actor)
        if request.method == 'POST':
            #print(request.POST)
            form = StudentForm(data=request.POST, files=request.FILES,instance=actor)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form}
        return render(request , 'changephotostu.html',context)  

    elif  r == 1:
        actor = Employee.objects.get(id=pk)
        form = EmployeeForm(instance=actor)
        if request.method == 'POST':
            #print(request.POST)
            form = EmployeeForm(data=request.POST, files=request.FILES,instance=actor)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form}
        return render(request , 'changephotoemp.html',context)  
    
    elif r == 3:
        actor = Teacher.objects.get(id=pk)
        form = TeacherForm(instance=actor)
        if request.method == 'POST':
            #print(request.POST)
            form = TeacherForm(data=request.POST, files=request.FILES,instance=actor)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form':form}
        return render(request , 'changephototea.html',context)  
    
    

@login_required(login_url='login')
@forteacher(allowedGroups=['teacher'])
def teacherhome(request):
    stages = Stage.objects.all()
    context = {
        'stages' : stages,
    }
    return render(request , 'teacherhome.html',context)  




@login_required(login_url='login')
@forteacher(allowedGroups=['teacher'])
def validencadrement(request,pk):

    stage = Stage.objects.get(id=pk)
    form = ValidStage(instance=stage)
    if request.method == 'POST': 
        form = ValidStage(data=request.POST,files=request.FILES,instance=stage)
        if form.is_valid():
            form.save()
            return redirect('teacherhome')
                       
    context = {'form':form}
    return render(request , 'validencadrement.html',context)  




@login_required(login_url='login')
@forteacher(allowedGroups=['teacher'])
def teacherencadrements(request):
    stages = Stage.objects.all()
    context = {
        'stages' : stages,
    }
    return render(request , 'teacherencadrements.html',context)  



@login_required(login_url='login')
@forteacher(allowedGroups=['teacher'])
def passwordtea(request,pk):

    user = User.objects.get(id=pk)
    form = CreateNewUser(instance=user)
    if request.method == 'POST': 
       
        form = CreateNewUser(data=request.POST,instance=user)
        group = request.POST.get('groups')
        if form.is_valid():
            user = form.save()
            user.groups.clear()
            group2 = Group.objects.get(id=group)
            user.groups.add(group2)
            #username = form.cleaned_data.get('username')
            #messages.success(request , username + ' Created Successfully !')
            return redirect('teacherhome')
                       
    context = {'form':form}
    return render(request , 'passwordtea.html',context)  








