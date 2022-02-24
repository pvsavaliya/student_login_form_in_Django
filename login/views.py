from django.shortcuts import render,HttpResponse,redirect

from registrastion.models import stu_data
from studentdata.views import index as std
# Create your views here.

def index(request):
    ans ={}
    if request.method == "POST":
        Uname = request.POST.get("Uname")
        Password = request.POST.get("Pass")
        StudentData = stu_data.objects.filter(email = Uname ,user_pass = Password).first()
        if StudentData:
            request.session['login_user'] = {'email' : Uname,'passWORD' : Password}
            print(request.session['login_user'])
            ans['error_text'] = False
            return redirect("/login/data/")
        else:
            ans['error_text'] = True
            ans['error_msg'] = 'plese chek id password '
            return render(request,"login.html",ans)


    return render(request,"login.html")

def studata(request):
    if request.session.has_key('login_user'):
        print("studata",request.session.has_key('login_user'))
        # context  = {}

        # Studentdata = stu_data.objects.all()
        # context['Studentdata'] = Studentdata
        # return render(request,'stu_data.html',context)
        return redirect('/studentdata/')

    else:
        return redirect('/login/')
def update(request,id=None):

    if request.method == 'POST':

        F_name = request.POST.get("first_name")
        M_name = request.POST.get("mid_name")
        L_name = request.POST.get("last_name")
        email = request.POST.get("email_id")
        phone_num = request.POST.get("mobil_no")    
        if phone_num == "":
            phone_num = None
        office_num = request.POST.get("mobil_no2")
        if office_num == "":
            office_num = None
        user_pass = request.POST.get("Password")
        hobby = request.POST.getlist("hobby[]")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("City")
        collage = request.POST.getlist("collage")
        joine_date = request.POST.get("date")
        if joine_date == "":
            joine_date = None
        address = request.POST.get("Address")
        markshit_12 = request.FILES.get("markshit_12")

        id = request.POST.get("id")


        Student_Data = stu_data.objects.filter(id=id).first()
        Student_Data.frist_name = F_name
        Student_Data.middle_name = M_name
        Student_Data.last_name = L_name
        Student_Data.email = email
        Student_Data.phone_num = phone_num
        Student_Data.office_num = office_num
        Student_Data.user_pass = user_pass
        Student_Data.hobby  = hobby
        Student_Data.genderlist = gender
        Student_Data.country_ = country
        Student_Data.state_ = state
        Student_Data.city_ = city
        Student_Data.collage = collage
        Student_Data.Address = address

        Student_Data.joine_date = joine_date
        if markshit_12 != None and markshit_12 != "":
            print('in')
            Student_Data.markshit_12 =  markshit_12 
        
        Student_Data.save()


        # request.session['User'] = {'frist_name' : F_name,
        #                                     'middle_name' : M_name,
        #                                     'last_name' : L_name,
        #                                     'email' : email,
        #                                     'phone_num' : phone_num,
        #                                     'office_num' : office_num,
        #                                     'user_pass' : user_pass,
        #                                     'hobby' : hobby,
        #                                     'gender' : gender,
        #                                     'country' : country,
        #                                     'state' : state,
        #                                     'city' : city,
        #                                     'collage' : collage,
        #                                     'joine_date' : joine_date,
        #                                     }
        # print(request.session['User'])


        return redirect("/login/data")
    else:
        context = {}
        Student_Data = stu_data.objects.filter(id=id).first()
        context['Student_Data'] = Student_Data
        return render(request,'Update_Registration.html',context)

def delete(request,id):

    Student_Data = stu_data.objects.filter(id=id).delete()
    return redirect("/login/data")
