from django.shortcuts import redirect, render,HttpResponse


# from login.views import index 


from registrastion.models import stu_data
# Create your views here.

def index(request):
    return render(request,'Student_Registration.html')

def data(request):
    ans = {}
    if request.method == "POST":
        print("yes")
        F_name = request.POST.get("first_name")    
        M_name = request.POST.get("mid_name")
        L_name = request.POST.get("last_name")
        email = request.POST.get("email_id")
        phone_num = request.POST.get("mobil_no")
        ans["phone"] = False
        if len(phone_num) < 11:
            ans["phone"] = True
            ans["phone_txt"]= "plese enter 10 digit number" 
        if phone_num == "" :
            phone_num = None



        office_num = request.POST.get("mobil_no2")
        ans["phone_2"] = False
        if len(office_num) < 11:
            print("PLESE ENTER A 10 DIGIT")
            ans["phone"] = True
            ans["phone_txt"]= "plese enter 10 digit number" 
        if office_num == "":
            office_num = None

        user_pass = request.POST.get("Password")
        print('pass_1s',user_pass)
        user_pass2 =request.POST.get("Password_2")
        print('pass_2',user_pass2)
        hobby = request.POST.getlist("hobby[]")
        gender = request.POST.get("gender")
        country = request.POST.get("country")
        state = request.POST.get("state")
        city = request.POST.get("City")
        collage = request.POST.getlist("collage")
        joine_date = request.POST.get("date")
        if joine_date == "":
            joine_date = None
        address =request.POST.get("Address")
        markshit_12 = request.FILES.get("markshit_12")
        print('in',markshit_12)
    
        ans['pass']=False
        if user_pass != user_pass2 or user_pass == "":
            ans['pass']=True
            ans['text']= 'plese check password '
            return render(request,'Student_Registration.html',ans) 
        

        StudentData = stu_data()
        StudentData.Address = address
        StudentData.user_pass = user_pass
        StudentData.frist_name = F_name
        StudentData.middle_name = M_name
        StudentData.last_name = L_name
        StudentData.email = email
        StudentData.phone_num = phone_num
        StudentData.office_num = office_num
        StudentData.country = country
        StudentData.state = state
        StudentData.city = city
        StudentData.collage = collage
        StudentData.joine_date = joine_date
        StudentData.hobby = hobby
        StudentData.gender = gender
        StudentData.markshit_12 = markshit_12

        StudentData.save()
    return redirect("/login/")
   

def logout(request):
    print("del",request.session['login_user'])
    del request.session['login_user'] 
    return redirect("/registration/")


