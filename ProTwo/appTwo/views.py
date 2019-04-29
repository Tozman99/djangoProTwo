from django.shortcuts import render
#from django.http import HttpResponse
#from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')
"""
def users(request):
    servaient a display ds la page users

    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'appTwo/users.html',context=user_dict)
"""

def users(request):
    form = NewUserForm()# form = instance 

    if request.method == 'POST':# ici veut dire qd qlq envoies des datas , 
    # on regarde si elles sont valides et on le renvoie a l index page 
        form = NewUserForm(request.POST)

    if form.is_valid():
        form.save(commit=True)
        return index(request)

    else:
        print('Error form invalid')

    return render(request,'appTwo/users.html',{'form':form})
# on va aussi return le ontext qui contient la form 

