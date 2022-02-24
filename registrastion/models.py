from django.db import models

# Create your models here.

class stu_data(models.Model):
    frist_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    middle_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(max_length=100)
    phone_num = models.IntegerField(default=None, blank=True, null=True)
    office_num = models.IntegerField(default=None, blank=True, null=True)
    user_pass = models.CharField(max_length=255,default=None, blank=True, null=True)
    user_pass2 = models.CharField(max_length=255,default=None, blank=True, null=True)
    hobby = models.CharField(max_length=255,default=None, blank=True, null=True)
    Address = models.TextField(default=None, blank=True, null=True)
    genderlist = [
        ('0', 'Male'),
        ('1', 'Female'),
    ]
    gender = models.IntegerField(choices=genderlist,default=None, blank=True, null=True)
    # gender=models.BooleanField()

    country_ = [
        ('0','INDIA'),
        ('1','USA'),
        ('2','UK'),
        ('3','Other'),
    ]
    country = models.IntegerField( choices=country_, default=None, blank=True, null=True)

    state_ =[
        ('0','gujrat'),
        ('1','maharastra'),
        ('2','up'),
        ('3','Other'),
    ]
    state = models.IntegerField( choices=state_, default=None, blank=True, null=True)

    city_ =[
        ('0','surat'),
        ('1','vadodra'),
        ('2','rajkot'),
        ('3','Other'),
    ]
    city = models.IntegerField( choices=city_, default=None, blank=True, null=True)

 
    collage = models.CharField(max_length=255, default=None, blank=True, null=True)

    # refrancelist =[
    #     ('0','sociale_media'),
    #     ('1','office'),
    #     ('2','Other'),
    # ]
    # refrance = models.CharField(max_length=255, choices=refrancelist, default=None, blank=True, null=True)
    joine_date = models.DateField(default=None, blank=True, null=True)
    markshit_12  = models.ImageField( upload_to="media/", default=None, blank=True, null=True )

