from django.shortcuts import render
from siteadmin.models import *
import datetime
# Create your views here.
def skill(request):
    return render(request,'skill.html')
def skillaction(request):
    ob=skill_tb(skill=request.POST['txtskill'])
    ob.save()
    return render(request,'skill.html',{'msg':'Added'})
def tim(request):
    return render(request,'time.html')
def timeaction(request):
    ob=time_tb(time=request.POST['txttime'])
    ob.save()
    return render(request,'time.html',{'msg':'Added'})
def login(request):
    return render(request,'login.html')
def educatorregister(request):
    ob=time_tb.objects.all()
    ob1=skill_tb.objects.all()
    return render(request,'educatorregister.html',{'time':ob,'skill':ob1})
def educatorregisteraction(request):
    skilid=skill_tb.objects.get(id=request.POST['ddskill'])
    timid=time_tb.objects.get(id=request.POST['ddtime'])
    print(skilid)
    if(len(request.FILES))!=0:
        ob=educator_tb(name=request.POST['txtname'],dob=request.POST['txtdate'],gender=request.POST['radgender'],phoneno=request.POST['txtno'],location=request.POST['txtloc'],qualification=request.POST['txtqua'],skills=skilid,availabletime=timid,experience=request.POST['txtexp'],certification=request.POST['txtcert'],charge=request.POST['txtcharge'],image=request.FILES['upload'],username=request.POST['txtusername'],password=request.POST['txtpassword'],status='pending')
        ob.save()
        return render(request,'educatorregister.html',{'msg':'You have beeen registered successfully'})
    else:
        return render(request,'educatorregister.html',{'msg':'please upload image'})
    
    return render(request,'educatorregister.html')
def userregister(request):
    ob=skill_tb.objects.all()
    return render(request,'userregister.html',{'skill':ob})
def userregisteraction(request):
    skilid=skill_tb.objects.get(id=request.POST['ddskill'])
    ob=user_tb(skill=skilid,name=request.POST['txtname'],dob=request.POST['txtdate'],location=request.POST['txtloc'],email=request.POST['txtmail'],gender=request.POST['radgender'],contactno=request.POST['txtno'],payment=request.POST['txtpay'],username=request.POST['txtusername'],password=request.POST['txtpassword'],status='pending')
    ob.save()
    return render(request,'userregister.html',{'msg':'Your have beeen registered successfully'})
def loginaction(request):
    ob=admin_tb.objects.filter(username=request.POST['txtusername'],password=request.POST['txtpassword'])
    if(ob.count()>0):
        
        return render(request,'adminhome.html')
    else:
        ob=educator_tb.objects.filter(username=request.POST['txtusername'],password=request.POST['txtpassword'],status='Approved')
        if(ob.count()>0):
            request.session['id']=ob[0].id
            ##print(ob[0].id)
            return render(request,'educatorhome.html')
        else:
            ob=user_tb.objects.filter(username=request.POST['txtusername'],password=request.POST['txtpassword'])
            if(ob.count()>0):
                request.session['id']=ob[0].id
                ##print(ob[0].id)
                return render(request,'userhome.html')
            else:
                return render(request,'login.html',{'msg':'Invalid username or password'})
    
    return render(request,'login.html')
def alleducator(request):
    ob=educator_tb.objects.filter(status='pending')
    return render(request,'viewall.html',{'data':ob})
    
def approve(request,uid):
    ob=educator_tb.objects.filter(id=uid).update(status='Approved')
    ob=educator_tb.objects.all()
    ob1=educator_tb.objects.filter(id=uid)
    return render(request,'viewall.html',{'data':ob1})


def viewrequest(request):
    ob=educator_tb.objects.filter(id=request.session['id'])
    print(ob[0].skills)
    ob2=user_tb.objects.filter(skill_id=ob[0].skills_id,status='pending')
    
    return render(request,'requests.html',{'data':ob2})
def accept(request,uid):
    #ob=user_tb.objects.filter(id=uid)
   
    ob1=user_tb.objects.filter(id=uid)
    return render(request,'request.html',{'data':ob1})
def acceptaction(request):
    edid=educator_tb.objects.get(id=request.session['id'])
    useid=user_tb.objects.get(id=request.POST['txtid'])
    skill=edid.skills_id
    timid=edid.availabletime_id
    print(timid)
    timid1=time_tb.objects.get(id=timid)
    print(timid1)
    skill1=skill_tb.objects.get(id=skill)
    print(skill)
    ob=accept_tb(time=datetime.datetime.now(),status='Accepted',timeid=timid1,skillid=skill1,educatorid=edid,userid=useid,contactno=request.POST['txtno'],payment=request.POST['txtpay'],email=request.POST['txtmail'])
    ob.save()
    ob1=user_tb.objects.filter(id=request.POST['txtid']).update(status='Accepted')
    ob2=user_tb.objects.filter(id=request.POST['txtid'])
    return render(request,'request.html',{'data':ob2,'msg':'Request has been accepted'})

def accepted(request):
    sid=educator_tb.objects.get(id=request.session['id'])
    ob=accept_tb.objects.filter(educatorid=sid)
    return render(request,'viewaccept.html',{'data':ob})

def booking(request):
    sid=user_tb.objects.get(id=request.session['id'])
    print(sid)
    ob3=educator_tb.objects.filter(skills=sid.skill_id)
    print(ob3)
    b=accept_tb.objects.filter(userid_id=sid)
    print(b)
    ob=accept_tb.objects.filter(userid=sid,skillid_id=sid.skill_id)
    print(ob)
    
    return render(request,'booking.html',{'data':ob})
def pay(request,uid):
    sid=user_tb.objects.filter(id=request.session['id'])
    ob=accept_tb.objects.filter(userid=sid)
    ob1=accept_tb.objects.filter(id=uid)
    return render(request,'pay.html',{'data':ob1})
def payaction(request):
    sid=user_tb.objects.get(id=request.session['id'])
    
   # print(sid)
    ob1=accept_tb.objects.filter(userid=sid)

   
    ob5=educator_tb.objects.get(id=ob1[0].educatorid_id)
    ob4=time_tb.objects.get(id=request.POST['txttime'])
    ob3=ob4.time
   
    ob=pay_tb(time=datetime.datetime.now(),userid=sid,timid=ob4,educatorid=ob5,totalamount=request.POST['txttot'],totalhours=request.POST['txthrs'],status='Payed')
    ob.save()
    
    return render(request,'new.html',{'msg':ob3})

def viewbooked(request):
    sid=user_tb.objects.get(id=request.session['id'])
    ob=pay_tb.objects.filter(userid=sid)
    return render(request,'viewbooked.html',{'data':ob})
def login(request):
    return render(request,'login.html')

def see(request):
    ob=educator_tb.objects.filter(status='Approved')
    return render(request,'approvededucators.html',{'data':ob})
