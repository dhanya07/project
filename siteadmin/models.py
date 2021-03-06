from django.db import models

# Create your models here.
class time_tb(models.Model):
    time=models.CharField(max_length=20)
class skill_tb(models.Model):
    skill=models.CharField(max_length=20)
class educator_tb(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=20,default='1')
    location=models.CharField(max_length=20)
    qualification=models.CharField(max_length=20)
    skills=models.ForeignKey(skill_tb,on_delete='CASCADE',default='1')
    experience=models.CharField(max_length=20)
    certification=models.CharField(max_length=20)
    charge=models.CharField(max_length=20)
    availabletime=models.ForeignKey(time_tb,on_delete='CASCADE',default='1')
    image=models.FileField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='1')
class user_tb(models.Model):
    name=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    contactno=models.CharField(max_length=20,default='1')
    location=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    skill=models.ForeignKey(skill_tb,on_delete='CASCADE',default='1')
    payment=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='1')
class admin_tb(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
class accept_tb(models.Model):
    userid=models.ForeignKey(user_tb,on_delete='CASCADE')
    educatorid=models.ForeignKey(educator_tb,on_delete='CASCADE')
    skillid=models.ForeignKey(skill_tb,on_delete='CASCADE',default='1')
    timeid=models.ForeignKey(time_tb,on_delete='CASCADE',default='1')
    contactno=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    payment=models.CharField(max_length=20)
    status=models.CharField(max_length=20,default='1')
    time=models.CharField(max_length=20,default='1')
class pay_tb(models.Model):
    userid=models.ForeignKey(user_tb,on_delete='CASCADE')
    timid=models.ForeignKey(time_tb,on_delete='CASCADE',default='1')
    time=models.CharField(max_length=20,default='1')
    educatorid=models.ForeignKey(educator_tb,on_delete='CASCADE')
    totalamount=models.CharField(max_length=20)
    totalhours=models.CharField(max_length=20)
    status=models.CharField(max_length=20)
