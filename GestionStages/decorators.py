from django.shortcuts import redirect
from django.http import HttpResponse




def notLoggedUsers(view_func):
    def wrapper_func(request , *args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request , *args,**kwargs)
    return wrapper_func



def foradmin(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'admin':
               return view_func(request , *args,**kwargs)
            else:
                if group == 'student':
                    return redirect('studenthome')
                else:
                    if group == 'teacher':
                        return redirect('teacherhome')
        return wrapper_func
    return decorator

def forstudent(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'student':
               return view_func(request , *args,**kwargs)
            else:
                if group == 'admin':
                    return redirect('home')
                else:
                    if group == 'teacher':
                        return redirect('teacherhome')
        return wrapper_func
    return decorator

def forteacher(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args,**kwargs): 
            group = None
            if request.user.groups.exists():
               group =  request.user.groups.all()[0].name
            if group == 'teacher':
               return view_func(request , *args,**kwargs)
            else:
                if group == 'admin':
                    return redirect('home')
                else:
                    if group == 'student':
                        return redirect('studenthome')
        return wrapper_func
    return decorator