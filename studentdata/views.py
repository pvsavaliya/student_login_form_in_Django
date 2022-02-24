from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Q

from registrastion.models import stu_data
# Create your views here.

def index(request):
    if request.session.has_key('login_user'):

        context  = {}
        
        if request.GET.get("search"):
            search_data = request.GET.get("search")
            Studentdata = stu_data.objects.filter(Q(frist_name__icontains=search_data)|Q(last_name__icontains=search_data))
            print(Studentdata)
            context['Studentdata'] = Studentdata
            return render(request,'stu_data.html',context)

        else:
            Studentdata = stu_data.objects.all()
            context['Studentdata'] = Studentdata
            return render(request,'stu_data.html',context)
    else:
        return redirect("/login/")
    
