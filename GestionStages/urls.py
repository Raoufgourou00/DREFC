from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth import views as aut_views


urlpatterns = [
    
    path('render_pdf_view/<str:pk>/', views.render_pdf_view,name='render_pdf_view'),



    path('home/', views.home,name='home'),

    path('students/', views.students,name='students'),
    path('createstudent/', views.createstudent,name='createstudent'),
    path('updatestudent/<str:pk>/', views.updatestudent,name='updatestudent'),
    path('deletestudent/<str:pk>/', views.deletestudent,name='deletestudent'),

    path('teachers/', views.teachers,name='teachers'),
    path('createteacher/', views.createteacher,name='createteacher'),
    path('updateteacher/<str:pk>/', views.updateteacher,name='updateteacher'),
    path('deleteteacher/<str:pk>/', views.deleteteacher,name='deleteteacher'),

    path('employees/', views.employees,name='employees'),
    path('createemployee/', views.createemployee,name='createemployee'),
    path('updateemployee/<str:pk>/', views.updateemployee,name='updateemployee'),
    path('deleteemployee/<str:pk>/', views.deleteemployee,name='deleteemployee'),

    path('companies/', views.companies,name='companies'),
    path('createcompany/', views.createcompany,name='createcompany'),
    path('updatecompany/<str:pk>/', views.updatecompany,name='updatecompany'),
    path('deletecompany/<str:pk>/', views.deletecompany,name='deletecompany'),

    path('promoters/', views.promoters,name='promoters'),
    path('createpromoter/', views.createpromoter,name='createpromoter'),
    path('updatepromoter/<str:pk>/', views.updatepromoter,name='updatepromoter'),
    path('deletepromoter/<str:pk>/', views.deletepromoter,name='deletepromoter'),

    path('stages1cpi/', views.stages1cpi,name='stages1cpi'),
    path('createstage1cpi/', views.createstage1cpi,name='createstage1cpi'),
    path('updatestage1cpi/<str:pk>/', views.updatestage1cpi,name='updatestage1cpi'),
    path('deletestage1cpi/<str:pk>/', views.deletestage1cpi,name='deletestage1cpi'),

    path('stages1cs/', views.stages1cs,name='stages1cs'),
    path('createstage1cs/', views.createstage1cs,name='createstage1cs'),
    path('updatestage1cs/<str:pk>/', views.updatestage1cs,name='updatestage1cs'),
    path('deletestage1cs/<str:pk>/', views.deletestage1cs,name='deletestage1cs'),

    path('stages3cs/', views.stages3cs,name='stages3cs'),
    path('createstage3cs/', views.createstage3cs,name='createstage3cs'),
    path('updatestage3cs/<str:pk>/', views.updatestage3cs,name='updatestage3cs'),
    path('deletestage3cs/<str:pk>/', views.deletestage3cs,name='deletestage3cs'),

    path('users/', views.users,name='users'),
    path('createuser/', views.createuser,name='createuser'),
    path('updateuser/<str:pk>/', views.updateuser,name='updateuser'),
    path('deleteuser/<str:pk>/', views.deleteuser,name='deleteuser'),

    path('login/', views.userLogin,name='login'),
    path('logout/', views.userLogout,name='logout'),

    path('pdf_view/<str:pk>/<int:b>/',views.pdf_view, name='pdf_view'),
    
    path('studenthome/', views.studenthome,name='studenthome'),
    path('validstage/<str:pk>/', views.validstage,name='validstage'),
    path('vosstages/', views.vosstages,name='vosstages'),
    path('password/<str:pk>/', views.password,name='password'),
    

    path('passwordemp/<str:pk>/', views.passwordemp,name='passwordemp'),
    path('changephoto/<str:pk>/<int:r>/', views.changephoto,name='changephoto'),


    path('teacherhome/', views.teacherhome,name='teacherhome'),
    path('validencadrement/<str:pk>/', views.validencadrement,name='validencadrement'),
    path('teacherencadrements/', views.teacherencadrements,name='teacherencadrements'),
    path('passwordtea/<str:pk>/', views.passwordtea,name='passwordtea'),


    path('reset_password/', aut_views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_sent/', aut_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name='password_reset_sent'),
    path('reset/<uidb64>/<token>/', aut_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/', aut_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name='password_reset_complete'),
    
]




