from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from myapp.models import *


def login(request):
    return render(request,'loginindex.html')
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    obj=Login.objects.filter(username=username,password=password)
    if obj.exists():
     obj2=Login.objects.get(username=username,password=password)
     request.session['lid']=obj2.id
     if obj2.type == 'admin':
        return redirect('/myapp/Admin_home/')
     elif obj2.type == 'recycle':
         return HttpResponse('''<script>alert("LOGIN SUCCESSFULL");window.location='/myapp/recycle_home/'</script>''')
     else:
         return HttpResponse('''<script>alert("INVALID LOGIN");window.location='/myapp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("INVALID LOGIN");window.location='/myapp/login/'</script>''')


def Admin_home(request):
    return render(request,'Admin/adminhomeindex.html')

def Change_Password(request):
    return render(request,'Admin/Change_password.html')

def Change_Password_post(request):
    Current_password=request.POST['textfield3']
    New_password=request.POST['textfield4']
    Confirm_password=request.POST['textfield5']
    log=Login.objects.filter(password=Current_password)
    if log.exists():
        log1=Login.objects.get(password=Current_password,id=request.session['lid'])
        if New_password==Confirm_password:
            log1=Login.objects.filter(password=Current_password,id=request.session['lid']).update(password=Confirm_password)
            return  HttpResponse('''<script>alert("SUCCESSFULLY CHANGED");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("PASSWORD MISMATCH");window.location='/myapp/Change_Password/'</script>''')
    else:
        return HttpResponse('''<script>alert("INVALID LOGIN");window.location='/myapp/Change_Password/'</script>''')

def Recycle_Verify(request):
    rec=Recycle_unit.objects.filter(status="pending")
    return render(request,'Admin/Recycle_verify.html',{'data':rec})

def Recycle_Verify_post(request):
    Search=request.POST['textfield']
    rec = Recycle_unit.objects.filter(name__icontains=Search, status="pending")
    return render(request,'Admin/Recycle_verify.html',{'data':rec})

def Approve_rec_unit(request,id):
    unit=Recycle_unit.objects.filter(LOGIN=id).update(status="Approved")
    reunit=Login.objects.filter(id=id).update(type="recycle")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/Recycle_Verify/#abc'</script>''')

def Reject_rec_unit(request,id):
    unit=Recycle_unit.objects.filter(LOGIN=id).update(status="Rejected")
    return HttpResponse('''<script>alert("REJECTED");window.location='/myapp/Recycle_Verify/#abc'</script>''')

def View_Approved_unit(request):
    rec = Recycle_unit.objects.filter(status="Approved")
    return render(request,'Admin/viewapprovedrecunit.html',{'data':rec})

def View_Approved_unit_post(request):
    Search=request.POST['textfield']
    rec = Recycle_unit.objects.filter(name__icontains=Search, status="Approved")
    return render(request,'Admin/viewapprovedrecunit.html',{'data':rec})


def View_Rejected_unit(request):
    rec = Recycle_unit.objects.filter(status="Rejected")
    return render(request,'Admin/rejectedreunitview.html',{'data':rec})

def View_Rejected_unit_post(request):
    Search = request.POST['textfield']
    rec = Recycle_unit.objects.filter(name__icontains=Search, status="Rejected")
    return render(request,'Admin/rejectedreunitview.html',{'data':rec})

def Reject_again_rec_unit(request,id):
    unit=Recycle_unit.objects.filter(LOGIN=id).update(status="Rejected")
    return HttpResponse('''<script>alert("REJECTED");window.location='/myapp/View_Approved_unit/#abc'</script>''')

def Approve_again_rec_unit(request,id):
    unit=Recycle_unit.objects.filter(LOGIN=id).update(status="Approved")
    reunit=Login.objects.filter(id=id).update(type="recycle")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Rejected_unit/#abc'</script>''')

def Pickup_Verify(request):
    pic=Pickup.objects.filter(status="pending")
    return render(request,'Admin/Pickup_verify.html',{'data':pic})

def Pickup_Verify_post(request):
    Search=request.POST['textfield']
    pic = Pickup.objects.filter(name__icontains=Search, status="pending")
    return render(request,'Admin/Pickup_verify.html',{'data':pic})

def Approve_pickup(request,id):
    pic=Pickup.objects.filter(LOGIN=id).update(status="Approved")
    pickup=Login.objects.filter(id=id).update(type="pickup")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/Pickup_Verify/#abc'</script>''')

def Reject_pickup(request,id):
    pic=Pickup.objects.filter(LOGIN=id).update(status="Rejected")
    return HttpResponse('''<script>alert("REJECTED");window.location='/myapp/Pickup_Verify/#abc'</script>''')

def View_Approved_pickup(request):
    pic = Pickup.objects.filter(status="Approved")
    return render(request,'Admin/viewapprovedpickup.html',{'data':pic})

def View_Approved_pickup_post(request):
    Search=request.POST['textfield']
    pic = Pickup.objects.filter(name__icontains=Search, status="Approved")
    return render(request,'Admin/viewapprovedpickup.html',{'data':pic})


def View_Rejected_pickup(request):
    pic = Pickup.objects.filter(status="Rejected")
    return render(request,'Admin/rejectedpickupview.html',{'data':pic})

def View_Rejected_pickup_post(request):
    Search = request.POST['textfield']
    pic = Pickup.objects.filter(name__icontains=Search, status="Rejected")
    return render(request,'Admin/rejectedpickupview.html',{'data':pic})

def Reject_again_pickup(request,id):
    pickup=Login.objects.filter(id=id).update(type="pending")
    pickup2=Pickup.objects.filter(LOGIN_id=id).update(status="Rejected")
    return HttpResponse('''<script>alert("REJECTED");window.location='/myapp/View_Approved_Pickup/#abc'</script>''')

def Approve_again_pickup(request,id):
    pic=Pickup.objects.filter(LOGIN=id).update(status="Approved")
    pickup=Login.objects.filter(id=id).update(type="pickup")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Rejected_Pickup/#abc'</script>''')

    # return HttpResponse('''<script>alert("SUCCESSFUL");window.locatikon='/myapp/View_Rejected_Pickup/#abc'</script>''')



def Waste_Rate(request):
    return render(request,'Admin/Waste_type.html')
def Waste_Rate_post(request):
    search=request.POST['textfield']
    return  HttpResponse("ok")
def Add_waste(request):
    waste=Waste.objects.all()
    return render(request,'Admin/Add_waste.html',{'data':waste})

def Add_waste_post(request):
    waste_type=request.POST['select']
    rate=request.POST['textfield']

    obj=Waste()
    obj.Waste_type=waste_type
    obj.Rate=rate
    obj.save()
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/Add_waste/#abc'</script>''')
def View_waste(request):
    waste1=Waste.objects.all()
    return render(request,'Admin/View_waste.html',{'data':waste1})
def View_waste_post(request):
    search = request.POST['textfield5']
    waste1 = Waste.objects.filter(Waste_type__icontains=search)
    return render(request,'Admin/View_waste.html',{'data':waste1})


def delete_waste(request,id):
    rs=Waste.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED SUCCESSFULLY");window.location='/myapp/View_waste/#abc'</script>''')


def Update_waste(request,id):
    waste1=Waste.objects.get(id=id)
    return render(request,'Admin/Update_waste.html',{'data':waste1})
def Update_waste_post(request):
    waste_type=request.POST['select']
    rate=request.POST['textfield']
    wid=request.POST['wid']
    obj=Waste.objects.get(id=wid)
    obj.Waste_type=waste_type
    obj.Rate=rate
    obj.save()
    return HttpResponse('''<script>alert("UPDATE SUCCESSFUL");window.location='/myapp/View_waste/#abc'</script>''')

def Worker_Verify(request):
    work=Worker.objects.filter(status="pending")
    return render(request,'Admin/worker_notf_verfy.html',{'data':work})

def Worker_Verify_post(request):
    search=request.POST['textfield']
    work=Worker.objects.filter(name__icontains=search, status="pending")
    return render(request,'Admin/worker_notf_verfy.html',{'data':work})




def Approve_worker(request,id):
    unit=Worker.objects.filter(LOGIN=id).update(status="Approved")
    reunit=Login.objects.filter(id=id).update(type="worker")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/Worker_Verify/#abc'</script>''')


def Reject_worker(request,id):
    unit=Worker.objects.filter(LOGIN=id).update(status="Rejected")
    return HttpResponse('''<script>alert("REJECTED");window.location='/myapp/Worker_Verify/#abc'</script>''')

def View_Approved_worker(request):
    rec = Worker.objects.filter(status="Approved")
    return render(request,'Admin/view approved workers.html',{'data':rec})
def View_Approved_worker_post(request):
    search = request.POST['textfield']
    rec = Worker.objects.filter(name__icontains=search, status="Approved")
    return render(request,'Admin/view approved workers.html',{'data':rec})

def Reject_again_worker(request,id):
    unit=Worker.objects.filter(id=id).update(status="Rejected")
    reunit=Login.objects.filter(id=id).update(type="worker")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Approved_worker/#abc'</script>''')


def View_Rejected_worker(request):
    rec = Worker.objects.filter(status="Rejected")
    return render(request,'Admin/view rejected workers.html',{'data':rec})


def Approve_again_worker(request,id):
    unit=Worker.objects.filter(id=id).update(status="Approved")
    reunit=Login.objects.filter(id=id).update(type="worker")
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Rejected_worker/#abc'</script>''')


def View_Rejected_worker_post(request):
    search = request.POST['textfield']
    rec = Worker.objects.filter(name__icontains=search, status="Rejected")
    return render(request,'Admin/view rejected workers.html',{'data':rec})









def View_Area(request):
    area1=Area.objects.all()
    return render(request,'Admin/Worker_mng_verify.html',{'data':area1})

def View_Area_post(request):
    search=request.POST['textfield']
    area1=Area.objects.filter(city__icontains=search)
    return render(request,'Admin/Worker_mng_verify.html',{'data':area1})


def delete_Area(request,id):
    rs=Area.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED SUCCESSFULLY");window.location='/myapp/View_Area/#abc'</script>''')

def Add_Area(request):
    return render(request,'Admin/Add_area_wrkr.html')

def Add_Area_post(request):
    city=request.POST['textfield']
    Street=request.POST['textfield3']
    place=request.POST['textfield2']
    var=Area()
    var.street=Street
    var.city=city
    var.place=place
    var.save()
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/Add_Area/#abc'</script>''')


def Update_Area(request,id):
    area2=Area.objects.get(id=id)
    return render(request,'Admin/Update_wrkr_area.html',{'data':area2})
def Update_Area_post(request):
    city=request.POST['textfield']
    Street=request.POST['textfield3']
    place=request.POST['textfield2']
    wid= request.POST['wid']
    obj= Area.objects.get(id=wid)
    obj.street= Street
    obj.city = city
    obj.place= place
    obj.save()
    return HttpResponse('''<script>alert("UPDATE SUCCESSFUL");window.location='/myapp/View_Area/#abc'</script>''')
def View_Alloc(request):
    var=Area_Allocation.objects.all()

    return render(request,'Admin/View_area_allctn.html',{'data':var})

def View_Alloc_post(request):
    search=request.POST['textfield']
    var = Area_Allocation.objects.filter(WORKER__name__icontains=search)
    return render(request,'Admin/View_area_allctn.html',{'data':var})
def delete_Alloc(request,id):
    rs=Area_Allocation.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED SUCCESSFULLY");window.location='/myapp/View_Alloc/#abc'</script>''')

def Allocate(request,id):
    var2=Worker.objects.all()
    return render(request,'Admin/area_allctn_wrkr.html',{'id':id,'data2':var2})
def Allocate_post(request):
    Area=request.POST['aid']
    Worker=request.POST['s2']
    area2=Area_Allocation()
    if Area_Allocation.objects.filter(WORKER_id=Worker).exists():
        area2 = Area_Allocation.objects.filter(WORKER_id=Worker)[0]
    area2.AREA_id=Area
    area2.WORKER_id=Worker
    area2.save()
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Alloc/#abc'</script>''')

def View_User(request):
    var=User.objects.all()
    return render(request,'Admin/view_user.html',{'data':var})
def View_User_post(request):
    search=request.POST['textfield']
    var = User.objects.filter(username__icontains=search)
    return render(request,'Admin/view_user.html',{'data':var})
def Add_Category(request):
    return render(request,'Admin/Add_category.html')
def Add_Category_post(request):
    Category=request.POST['category']
    var=WorkerCategory()
    var.Category=Category
    var.save()
    return HttpResponse('''<script>alert("SUCCESSFUL");window.location='/myapp/View_Category/#abc'</script>''')
# def View_Category(request):
#     var=WorkerCategory.objects.all()
#     return render(request,'Admin/View_category.html',{'data',var})

def view_cat(request):
    res=WorkerCategory.objects.all()
    return render(request,"Admin/View_category.html",{'dt':res})
def View_Category_post(request):
    search=request.POST['textfield']
    res=WorkerCategory.objects.filter(Category__icontains=search)
    return render(request,"Admin/View_category.html",{'dt':res})
def delete_category(request,id):
    rs=WorkerCategory.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED SUCCESSFULLY");window.location='/myapp/View_Category/#abc'</script>''')

def Update_Category(request,id):
    var1=WorkerCategory.objects.get(id=id)
    return render(request,'Admin/Update_category.html',{'data':var1})
def Update_Category_post(request):
    id=request.POST['id']
    Category=request.POST['category']
    obj=WorkerCategory.objects.get(id=id)
    obj.Category=Category
    obj.save()
    return HttpResponse('''<script>alert("UPDATED SUCCESSFULLY");window.location='/myapp/View_Category/#abc'</script>''')
def View_Complaint(request):
    var1=Complaint.objects.all()
    return render(request,'Admin/View_complaint.html',{'data':var1})
def View_Complaint_post(request):
    frm=request.POST['textfield']
    to=request.POST['textfield2']
    var1=Complaint.objects.filter(date__range=[frm,to])
    return render(request,'Admin/View_complaint.html',{'data':var1})


def Send_Reply(request,id):
    return render(request,'Admin/Send_reply.html',{'id':id})
def Send_Reply_post(request):
    Reply=request.POST['textarea']
    cid=request.POST['cid']
    obj=Complaint.objects.get(id=cid)
    obj.reply=Reply
    obj.status='Replied'
    obj.save()
    return HttpResponse('''<script>alert("Reply Sent");window.location='/myapp/View_Complaint/#abc'</script>''')


def Feedback(request):
    feed=feedback.objects.all()
    return render(request,'Admin/Feedback.html',{'data':feed})
def Feedback_post(request):
    frm = request.POST['textfield']
    to = request.POST['textfield2']
    feed = feedback.objects.filter(date__range=[frm, to])

    return render(request,'Admin/Feedback.html',{'data':feed})


#################################33333
def recycle_home(request):
    return render(request,'Recycleunit/recycleindex.html')


def Recycle_Signup(request):
    return render(request,'recsignupindex.html')
def Recycle_Signup_post(request):
    Username=request.POST['textfield']
    Place=request.POST['textfield2']
    street=request.POST['textfield3']
    city=request.POST['textfield4']
    building_no=request.POST['textfield5']
    license_no=request.POST['textfield6']
    manager=request.POST['textfield7']
    phone_no=request.POST['textfield8']
    Email=request.POST['textfield9']
    password=request.POST['textfield10']
    confirm_password=request.POST['textfield11']

    lobj=Login()
    lobj.username=Email
    lobj.password=confirm_password
    lobj.type='pending'
    lobj.save()

    obj=Recycle_unit()
    obj.name=Username
    obj.email=Email
    obj.place=Place
    obj.street=street
    obj.city=city
    obj.building_no=building_no
    obj.license_no=license_no
    obj.manager=manager
    obj.phone_no=phone_no
    obj.LOGIN=lobj
    obj.status='pending'
    obj.save()
    return HttpResponse('''<script>alert("SUCCESS");window.location='/myapp/login/'</script>''')


def recycle_Change_Password(request):
    return render(request,'Recycleunit/recycle_changepassword.html/')

def recycle_Change_Password_post(request):
    Current_password=request.POST['textfield3']
    New_password=request.POST['textfield4']
    Confirm_password=request.POST['textfield5']
    log=Login.objects.filter(password=Current_password)
    if log.exists():
        log1=Login.objects.get(password=Current_password,id=request.session['lid'])
        if New_password==Confirm_password:
            log1=Login.objects.filter(password=Current_password,id=request.session['lid']).update(password=Confirm_password)
            return  HttpResponse('''<script>alert("SUCCESSFULLY CHANGED");window.location='/myapp/login/'</script>''')
        else:
            return HttpResponse('''<script>alert("PASSWORD MISMATCH");window.location='/myapp/recycle_Change_Password/'</script>''')
    else:
        return HttpResponse('''<script>alert("INVALID LOGIN");window.location='/myapp/recycle_Change_Password/'</script>''')


def View_Profile(request):
    var=Recycle_unit.objects.get(LOGIN=request.session['lid'])
    return render(request,'Recycleunit/view_profile.html',{'data':var})
# def View_Profile_post(request):
#     return  HttpResponse("ok")
def Edit_Profile(request,id):
    var=Recycle_unit.objects.get(id=id)
    return render(request,'Recycleunit/edit_profile.html',{'data':var})
def Edit_Profile_post(request):
    id=request.POST['id']

    name=request.POST['textfield']
    email=request.POST['textfield2']
    phone=request.POST['textfield3']
    manager=request.POST['textfield4']
    license_no=request.POST['textfield5']
    place=request.POST['textfield6']
    street=request.POST['textfield7']
    city=request.POST['textfield8']
    Building=request.POST['textfield9']
    obj=Recycle_unit.objects.get(id=id)
    obj.name=name
    obj.email=email
    obj.place=place
    obj.street=street
    obj.city=city
    obj.building_no=Building
    obj.license_no=license_no
    obj.manager=manager
    obj.phone_no=phone
    obj.save()

    return HttpResponse('''<script>alert("UPDATED SUCCESSFULLY");window.location='/myapp/View_Profile/#abc'</script>''')
def View_Req(request):
    var=Waste_req.objects.filter(status="Picked Up",USER__place__icontains=Recycle_unit.objects.get(LOGIN_id=request.session['lid']).place )
    return render(request,'Recycleunit/veiw_req.html',{'data':var})
def View_Req_post(request):
    frm = request.POST['textfield']
    to = request.POST['textfield2']
    var = Waste_req.objects.filter(status="Picked Up", USER__place__icontains=Recycle_unit.objects.get(
        LOGIN_id=request.session['lid']).place,Date__range=[frm, to])
    return render(request, 'Recycleunit/veiw_req.html', {'data': var})

def Add_Product(request):
    return render(request,'Recycleunit/recycled_prod.html')
def Add_Product_post(request):
    product_name=request.POST['textfield']
    image=request.FILES['fileField']
    Rate=request.POST['textfield3']
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d-%H%M%S")+".jpg"
    fs=FileSystemStorage()
    fn=fs.save(date,image)
    path=fs.url(date)
    type=request.POST['textfield2']
    obj=Product()
    obj.product_name=product_name
    obj.image=path
    obj.type=type
    obj.Rate=Rate
    obj.RECYCLEUNIT=Recycle_unit.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("SUCCESSFULL");window.location='/myapp/Add_Product/#abc'</script>''')
def View_Product(request):
    var=Product.objects.all()
    return render(request,'Recycleunit/view_prod.html',{'data':var})
def View_Product_post(request):
    search=request.POST['textfield']
    var = Product.objects.filter(product_name__icontains=search)
    return render(request,'Recycleunit/view_prod.html',{'data':var})

def Update_Product(request,id):
    var=Product.objects.get(id=id)

    return render(request,'Recycleunit/update_prod.html',{'data':var})
def Update_Product_post(request):
    id=request.POST['id']
    product_name=request.POST['textfield1']
    type=request.POST['textfield']
    Rate=request.POST['textfield3']
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d%H%M%S") + " .jpg"
        fs = FileSystemStorage()
        fn = fs.save(date, image)
        obj=Product.objects.get(id=id)
        obj.image=fs.url(date)
        # obj.Rate=Rate
        obj.save()
        return HttpResponse('''<script>alert("UPDATED SUCCESSFULLY");window.location='/myapp/View_Product/#abc'</script>''')
    else:
        obj=Product.objects.get(id=id)
        obj.product_name=product_name
        obj.type=type
        obj.Rate=Rate
        obj.save()
        return HttpResponse('''<script>alert("UPDATED SUCCESSFULLY");window.location='/myapp/View_Product/#abc'</script>''')

def delete_Product(request,id):
    rs=Product.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("DELETED SUCCESSFULLY");window.location='/myapp/View_Product/#abc'</script>''')

def Profit_Donation(request):
    return render(request,'Recycleunit/add_profit.html')
def Profit_Donation_post(request):
    Charity_Donation=request.POST['textfield']
    amount=request.POST['textfield2']
    Acc_no=request.POST['textfield3']
    ifsc=request.POST['textfield4']
    obj=Donation()
    obj.charity_center=Charity_Donation
    obj.acc_no=Acc_no
    obj.ifsc=ifsc
    obj.amount=amount
    obj.RECYCLE=Recycle_unit.objects.get(LOGIN_id=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("SUCCESSFULL");window.location='/myapp/Profit_Donation/#abc'</script>''')
def View_Donation(request):
    var=Donation.objects.all()
    return render(request,'Recycleunit/View_donation.html',{'data':var})
def View_Donation_post(request):
    search=request.POST['textfield']
    var = Donation.objects.filter(charity_center__icontains=search)
    return render(request, 'Recycleunit/View_donation.html', {'data': var})
def View_Product_Order(request):
    var=Order_sub.objects.all()
    return render(request,'Recycleunit/View_prod_order.html',{'data':var})
def View_Product_Order_post(request):
    frm = request.POST['textfield']
    to = request.POST['textfield2']
    var = Order_sub.objects.filter(ORDER__date__range=[frm, to])

    return render(request,'Recycleunit/View_prod_order.html',{'data':var})

#################################################worker
def Worker_Signup(request):
    photo=request.POST['photo']
    import base64
    from datetime import datetime
    date=datetime.now().strftime("%Y%m%d%H%M%S")
    a=base64.b64decode(photo)
    fh=open("D:\\Smart_Waste\\media\\Worker\\"+date+".jpg","wb")
    path="/media/Worker/"+date+".jpg"
    fh.write(a)
    fh.close()
    name=request.POST['name']
    phone_no=request.POST['phone_no']
    email=request.POST['email']
    gender=request.POST['gender']
    category=request.POST['category']

    password=request.POST['password']
    confirm_password=request.POST['confirm_password']

    if password==confirm_password:


        lobj=Login()
        lobj.username=email
        lobj.password=confirm_password
        lobj.type='pending'
        lobj.save()

        obj=Worker()
        obj.name=name
        obj.phone_no=phone_no
        obj.email=email
        obj.gender=gender
        obj.status='pending'
        obj.LOGIN=lobj
        obj.CATEGORY_id=category
        obj.photo=path
        obj.save()

        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'not ok'})


def view_category(request):
    res=WorkerCategory.objects.all()
    l=[]
    for i in res:
        l.append({"id":i.id,"cat":i.Category})
    return JsonResponse({"status":'ok',"data":l})


def and_Login(request):
    username=request.POST['username']
    password=request.POST['password']
    obj = Login.objects.filter(username=username, password=password)
    if obj.exists():
        obj2 = Login.objects.get(username=username, password=password)
        lid=obj2.id
        if obj2.type == 'worker':
            return JsonResponse({'status': 'ok',"type":obj2.type,'lid':str(lid)})
        elif obj2.type == 'user':
            return JsonResponse({'status': 'ok',"type":obj2.type,'lid':str(lid)})
        else:
            return JsonResponse({'status':'no'})
    else:
        return JsonResponse({'status': 'not ok'})


def Worker_Profile(request):
    lid = request.POST['lid']
    var=Worker.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','id':var.id,'name':var.name,'phone_no':var.phone_no,'email':var.email,'gender':var.gender,'category':var.CATEGORY.Category,'photo':var.photo})

def Edit_Worker_Profile(request):

    name = request.POST['name']
    cat = request.POST['category']
    phone_no = request.POST['phone_no']
    email = request.POST['email']
    gender = request.POST['gender']
    lid=request.POST['lid']
    print(lid,"hiiiiiiiii")


    obj = Worker.objects.get(LOGIN_id=lid)
    photo = request.POST['photo']

    if len(photo)>0:

        import base64
        from datetime import datetime
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        a = base64.b64decode(photo)
        fh = open("D:\\Smart_Waste\\media\\Worker\\" + date + ".jpg", "wb")
        path = "/media/Worker/" + date + ".jpg"
        fh.write(a)
        fh.close()
        obj = Worker.objects.get(LOGIN_id=lid)
        obj.photo=path
        obj.save()

    obj = Worker.objects.get(LOGIN_id=lid)
    obj.name = name
    obj.phone_no = phone_no
    obj.email = email
    obj.gender = gender
    obj.CATEGORY_id=cat
    obj.save()
    print(obj)
    return JsonResponse({'status':'ok'})

def worker_changepass(request):
    lid = request.POST['lid']
    current_password=request.POST['current_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    return JsonResponse({'status': 'ok'})

def View_User_rqst(request):
    var=Request.objects.all()
    l=[]
    for i in var:
        l.append({
            'id':i.id,
            'waste':i.WASTE.Waste_type,
            'Quantity':i.WASTE.Quantity,
            'Rate':i.WASTE.Rate,
            'username':i.USER.username,
            'phone_no':i.USER.phone_no,
            'house':i.USER.house_name,
            'place':i.USER.place,
            'status':i.Status,
            'Date':i.Date})
    return JsonResponse({'status':'ok','data':l})

def View_Alloc_Area(request):
    lid= request.POST["lid"]
    var = Area_Allocation.objects.filter(WORKER__LOGIN_id=lid)
    l = []
    for i in var:
        l.append({
            'id': i.id,
            'city':i.AREA.city,
            'street':i.AREA.street,
            'place':i.AREA.place,
            'name':i.WORKER.name,
            'phone_no':i.WORKER.phone_no
        })
    return JsonResponse({'status':'ok','data':l})


def worker_view_user_waste_request(request):
    res=Waste_req.objects.filter(status='pending',USER__place__icontains=Area_Allocation.objects.filter(WORKER__LOGIN_id=request.POST['lid'])[0].AREA.place)
    ress=Waste.objects.filter()
    l=[]
    l2=[]
    for i in res:
        l.append({
                  "id":i.id,
                  "user":i.USER.username,
                  "phone_no":i.USER.phone_no,
                  "house_name":i.USER.house_name,
                  "place":i.USER.place,
                  "post":i.USER.post,
                  "pincode":i.USER.pincode,
                  "waste":i.WASTE.Waste_type,
                  "narration":i.Narration,
                  "Date":i.Date,
                  "status":i.status,
                  "qty":i.qty,
                  })
    for i in ress:
        l2.append({
                  "id":i.id,
                  "Waste_type":i.Waste_type,
                  })
    return JsonResponse({'status': 'ok',"data":l,"datas":l2})

def worker_add_qntty(request):
    rid=request.POST['rid']
    qntty=request.POST['qntity']

    res=Waste_req.objects.filter(id=rid).update(qty=qntty, status='pending')


    return JsonResponse({"status":"ok"})

################################################user



def User_signup(request):
    username = request.POST['username']
    phone_no = request.POST['phone_no']
    house_name = request.POST['house_name']
    place = request.POST['place']
    post = request.POST['post']
    pincode = request.POST['pincode']
    Email = request.POST['Email']
    gen = request.POST['gen']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
        lobj = Login()
        lobj.username = Email
        lobj.password = confirm_password
        lobj.type="user"
        lobj.save()

        obj = User()
        obj.username = username
        obj.phone_no = phone_no
        obj.house_name = house_name
        obj.place = place
        obj.post = post
        obj.pincode = pincode
        obj.Email = Email
        obj.gender=gen
        obj.LOGIN = lobj
        obj.save()

    return JsonResponse({'status': 'ok'})

def User_Login(request):
    username = request.POST['username']

    password = request.POST['password']
    print(username, "haii")
    print(password, "hellooo")
    obj = Login.objects.filter(username=username, password=password)
    if obj.exists():
        obj2 = Login.objects.get(username=username, password=password)
        if obj2.type == 'user':
            print("hiiiiiiiiiiiiiiii")
            lid = obj2.id
            return JsonResponse({'status': 'ok', 'lid':str(lid), 'type':'user'})
        elif obj2.type == 'pickup':
            lid = obj2.id
            return JsonResponse({'status': 'ok','lid':str(lid),'type':'pickup'})
        elif obj2.type == 'worker':
            print("hhhhhhhhhhhhhhh")
            lid = obj2.id
            return JsonResponse({'status': 'ok','lid':str(lid),'type':'worker'})
    else:
        return JsonResponse({'status': 'not ok'})

def User_Change_Password(request):
        lid = request.POST['lid']
        Current_password = request.POST['current']
        New_password = request.POST['new']
        Confirm_password = request.POST['confirm']
        log = Login.objects.filter(password=Current_password)
        if log.exists():
            log1 = Login.objects.get(password=Current_password, id=lid)
            if New_password == Confirm_password:
                log1 = Login.objects.filter(password=Current_password, id=lid).update(password=Confirm_password)
                return JsonResponse({'status': 'ok'})
            else:
                return JsonResponse({'status':'no'})
        else:
            return JsonResponse({'status':'none'})



def View_profile(request):
    lid = request.POST['lid']
    var = User.objects.get(LOGIN_id=lid)

    return JsonResponse({'status': 'ok',  'username': var.username,
            'gender':var.gender,
            'phone_no': var.phone_no,
            'house_name': var.house_name,
            'place': var.place,
            'post': var.post,
            'pincode': var.pincode,
            'Email': var.Email,})




def User_edit_Profile(request):
    username = request.POST['username']
    gender = request.POST['gender']
    phone_no = request.POST['phone_no']
    house_name = request.POST['house_name']
    place = request.POST['place']
    post = request.POST['post']
    pincode = request.POST['pincode']
    Email = request.POST['email']
    lid = request.POST['lid']

    obj = User.objects.get(LOGIN=lid)
    obj.username = username
    obj.gender = gender
    obj.phone_no = phone_no
    obj.house_name = house_name
    obj.place = place
    obj.post = post
    obj.pincode = pincode
    obj.Email = Email
    obj.save()

    return JsonResponse({'status': 'ok'})
def User_complaint(request):
    complaint=request.POST['complaint']
    lid=request.POST['lid']

    obj = Complaint()
    obj.complaint = complaint
    import datetime
    obj.date = datetime.date.today()
    obj.reply = 'pending'
    obj.status='pending'
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})





def Cart_(request):
    pid=request.POST["pid"]
    lid=request.POST["lid"]
    qty=request.POST["qty"]

    c=Cart()
    c.USER= User.objects.get(LOGIN_id= lid)
    c.PRODUCT_id=pid
    from datetime import datetime
    c.date=datetime.now().date()
    c.quantity= qty
    c.save()
    return JsonResponse({'status': 'ok'})


def view_Reply(request):

    lid= request.POST["lid"]
    var = Complaint.objects.filter(USER__LOGIN_id= lid)
    l = []
    for i in var:
        l.append({
            'id': i.id,
            'complaint': i.complaint,
            'Reply': i.reply,
            'Date': i.date,
            'status': i.status
            })


    return JsonResponse({'status': 'ok','data':l})




def User_feedbacks(request):
    from datetime import datetime
    date=datetime.now()
    Feedback=request.POST['feedback']


    obj=feedback()
    obj.date=date
    obj.feedback=Feedback

    return JsonResponse({'status': 'ok'})
def View_feedbacks(request):
    var = feedback.objects.all()
    l = []
    for i in var:
        l.append({
            'feedback': i.feedback.feedback,
            'Date': i.Date})
    return  JsonResponse({'status':'ok'})
def View_wrk_category(request):
    var = Area_Allocation.objects.all()
    l = []
    for i in var:
        l.append({
            'id': i.WORKER.id,
            'Category': i.WORKER.CATEGORY.Category,
            'name': i.WORKER.name,'phoneno': i.WORKER.phone_no,
            'gender': i.WORKER.gender,
            'photo': i.WORKER.photo,})
    print(l)
    return JsonResponse({'status':'ok','data':l})


def user_view_product(request):
    var = Product.objects.all()
    if 'value' in request.POST:
        value = request.POST['value']
        var = Product.objects.filter(product_name__icontains=value)
    l = []
    for i in var:
        l.append({
            'id': i.id,
            'product name': i.product_name,
            'image': i.image,
            'type': i.type,
            'Rate':i.Rate,
            })
    print(l)
    return JsonResponse({'status':'ok','data':l})




def View_worker_ntfy(request):
    var = Notification.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'worker_notification':i.worker_notification})
    return JsonResponse({'status': 'ok','data':l})
import  datetime

def user_work_request(request):
    lid=request.POST["lid"]
    workerid=request.POST["workerid"]

    a=Recycle_req()
    a.WORKER_id= workerid
    a.USER= User.objects.get(LOGIN_id= lid)
    a.date= datetime.datetime.now()
    a.status="pending"
    a.save()
    return JsonResponse({'status':'ok'})
################################################################################################pickup


def pickup_signup(request):
    vehicle = request.POST['vehicle']
    vehicle_no = request.POST['vehicle_no']
    Email = request.POST['email']
    phone_no = request.POST['phone_no']
    password = request.POST['password']
    confirm_password = request.POST['confirm_password']

    if password == confirm_password:
        lobj = Login()
        lobj.username = Email
        lobj.password = confirm_password
        lobj.save()

        obj = Pickup()
        obj.vehicle = vehicle
        obj.vehicle_no = vehicle_no
        obj.Email = Email
        obj.phone_no = phone_no
        obj.status='pending'
        obj.LOGIN = lobj
        obj.save()

    return JsonResponse({'status': 'ok'})

def pickup_changepass(request):
    lid = request.POST['lid']
    current_password=request.POST['current_password']
    new_password=request.POST['new_password']
    confirm_password=request.POST['confirm_password']
    return JsonResponse({'status': 'ok'})
def Pickup_Profile(request):
    lid = request.POST['lid']
    var = Pickup.objects.get(LOGIN_id=lid)
    return JsonResponse({'status': 'ok','vehicle':var.vehicle,'vehicle_no':var.vehicle_no,'email':var.Email,'phone_no':var.phone_no})

def pickup_edit_Profile(request):
    lid = request.POST['lid']
    vehicle = request.POST['vehicle']
    vehicle_no = request.POST['vehicle_no']
    phone_no = request.POST['phone_no']
    Email = request.POST['email']

    obj = Pickup.objects.get(LOGIN_id=lid)
    obj.vehicle = vehicle
    obj.vehicle_no = vehicle_no
    obj.phone_no = phone_no
    obj.Email = Email
    obj.save()
    return JsonResponse({'status': 'ok'})

def view_Waste_collect(request):
    var = Waste_req.objects.filter(status='Picked Up')
    l = []
    for i in var:
        l.append({
            "id": i.id,
            "user": i.USER.username,
            "phone_no": i.USER.phone_no,
            "house_name": i.USER.house_name,
            "place": i.USER.place,
            "post": i.USER.post,
            "pincode": i.USER.pincode,
            "waste": i.WASTE.Waste_type,
            "narration": i.Narration,
            "Date": i.Date,

            "status": i.status,
            "qty": i.qty,
        })
    return JsonResponse({'status': 'ok',"data":l})


def view_user_waste(request):
    lid=request.POST['lid']
    res=Waste_req.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in res:
        l.append({
                  "id":i.id,
                  "Rate":i.WASTE.Rate,
                  "type":i.WASTE.Waste_type,
                  "narration": i.Narration,
                  "status": i.status,
                  "Date": i.Date,
                  "qty":i.qty})
    return JsonResponse({'status': 'ok',"data":l})
#
# def User_view_category(request):
#     r=
#     return JsonResponse({'status': 'ok'})

def view_user_waste_request(request):
    res=Waste_req.objects.filter(status='pending')
    ress=Waste.objects.filter()
    l=[]
    l2=[]
    for i in res:
        l.append({
                  "id":i.id,
                  "user":i.USER.username,
                "phone_no": i.USER.phone_no,
            "house_name": i.USER.house_name,
            "place": i.USER.place,
            "post": i.USER.post,
            "pincode": i.USER.pincode,
                  "waste":i.WASTE.Waste_type,
                  "narration":i.Narration,
                  "Date":i.Date,

                  "status":i.status,
                  "qty":i.qty,
                  })
    for i in ress:
        l2.append({
                  "id":i.id,
                  "Waste_type":i.Waste_type,
                  })
    return JsonResponse({'status': 'ok',"data":l,"datas":l2})

def user_waste_request(request):
    lid=request.POST["lid"]
    WASTE_id=request.POST["type"]
    Narration=request.POST["narration"]
    from datetime import datetime
    Date = datetime.now().date()

    print(Waste)

    a=Waste_req()

    a.USER= User.objects.get(LOGIN__id= lid)
    a.WASTE_id = WASTE_id
    a.Narration= Narration
    a.Date= Date
    a.status="pending"
    a.qty="0"
    a.save()
    return JsonResponse({'status':'ok'})


def pickup_add_qntty(request):
    rid=request.POST['rid']
    # qntty=request.POST['qntity']
    res=Waste_req.objects.filter(id=rid).update(status='Picked Up')
    return JsonResponse({"status":"ok"})

def delete_Cart(request):
    cid=request.POST['cid']
    rs=Cart.objects.get(id=cid).delete()
    return JsonResponse({'status':'ok'})


def user_make_payment(request):
    lid = request.POST['lid']
    # cardnumber=request.POST['cardnumber']
    # holdername=request.POST['name']
    # expiredate=request.POST['expiredate']
    # Cvv=request.POST['cvv']
    # Amount=float(request.POST['amount'])

    # if Bank.objects.filter(cardnumber=cardnumber, Acname=holdername, expiredate=expiredate, Cvv=Cvv, Balance__gte=Amount).exists():
    res = Cart.objects.filter(USER__LOGIN_id=lid).values_list('PRODUCT__RECYCLEUNIT__id').distinct()

    for i in res:
        print(i)
        res2 = Cart.objects.filter(USER__LOGIN_id=lid, PRODUCT__RECYCLEUNIT_id=i[0])
        boj = Order()
        boj.USER = User.objects.get(LOGIN_id=lid)
        # boj.amount=0
        boj.status = 'Paid'
        from datetime import datetime
        boj.order_date = datetime.now().date().today()
        boj.date=datetime.now().date().today()
        # boj.RECYCLE_id = i[0]
        boj.save()

        # res3 =
        mytotal = 0
        for j in res2:
            print(j)
            bs = Order_sub()
            bs.ORDER_id = boj.id
            bs.PRODUCT_id = j.PRODUCT.id
            # bs.qty=j.quantity
            bs.save()

            # mytotal+=(float(j.PRODUCT.amount)*j.quantity)
            mytotal += (float(j.PRODUCT.Rate))
        Cart.objects.filter(PRODUCT__RECYCLEUNIT_id=i[0], USER__LOGIN_id=lid).delete()
        b1oj = Order.objects.get(id=boj.id)
        # b1oj.amount =mytotal
        b1oj.save()
        #
        # for i in
        return JsonResponse({'k': '0', 'status': "ok"})


####################################

def u_add_to_cart(request):
    lid=request.POST['lid']
    prod_id=request.POST['product_id']
    qty=request.POST['qty']
    from datetime import datetime
    date=datetime.now()

    var=Cart()
    var.date=date
    var.PRODUCT_id=prod_id
    var.USER=User.objects.get(LOGIN_id=lid)
    var.quantity=qty
    var.save()
    return JsonResponse({'status':'ok'})


def view_cart(request):
    lid=request.POST['lid']
    var=Cart.objects.filter(USER__LOGIN_id=lid)

    l=[]
    total=0
    for i in var:
        total += (float(i.PRODUCT.Rate) * int(i.quantity))
        l.append({'id':i.id,
                  'date':i.date,
                  'qty':i.quantity,
                  'product':i.PRODUCT.product_name,
                  'recycle_name':i.PRODUCT.RECYCLEUNIT.name,
                  'amount':i.PRODUCT.Rate,
                  'image': i.PRODUCT.image,
                  })

    return JsonResponse({'status':'ok','data':l,'total':total})


def remove_cart(request):
    id=request.POST['id']
    var=Cart.objects.filter(id=id).delete()

    return JsonResponse({'status':'ok'})


def user_payment(request):
    lid=request.POST['lid']
    # cardnumber=request.POST['cardnumber']
    # holdername=request.POST['name']
    # expiredate=request.POST['expiredate']
    # Cvv=request.POST['cvv']
    # Amount=float(request.POST['amount'])

    # if Bank.objects.filter(cardnumber=cardnumber, Acname=holdername, expiredate=expiredate, Cvv=Cvv, Balance__gte=Amount).exists():
    res = Cart.objects.filter(USER__LOGIN_id=lid).values_list('PRODUCT__RECYCLEUNIT__id').distinct()

    for i in res:
        print(i)
        res2 = Cart.objects.filter(USER__LOGIN_id=lid,PRODUCT__RECYCLEUNIT_id=i[0])
        boj = Order()
        boj.USER=User.objects.get(LOGIN_id=lid)
        # boj.amount=0
        boj.status=0
        from datetime import datetime
        boj.order_date = datetime.now().date().today()
        # boj.RECYCLE_id = i[0]
        boj.save()

        # res3 =
        mytotal=0
        for j in res2:
            print(j)
            bs=Order_sub()
            bs.ORDER_id=boj.id
            bs.PRODUCT_id=j.PRODUCT.id
            # bs.qty=j.quantity
            bs.save()

            # mytotal+=(float(j.PRODUCT.amount)*j.quantity)
            mytotal+=(float(j.PRODUCT.Rate))
        Cart.objects.filter(PRODUCT__RECYCLEUNIT_id=i[0], USER__LOGIN_id=lid).delete()
        b1oj=Order.objects.get(id=boj.id)
        # b1oj.amount =mytotal
        b1oj.save()
            #
            # for i in
        return JsonResponse({'k':'0','status':"ok"})
    # else:
    #     return JsonResponse({"status":"no"})


def view_notification(request):
    var=Notification.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,
                  'worker_notification':i.worker_notification,
                  'update_notification':i.update_notification,
                  'product_notification':i.product_notification,
                  'delivery_notification':i.delivery_notification})

    return JsonResponse({'status':'ok','data':l})


def View_order_status(request):

    lid= request.POST["lid"]
    var = Order.objects.filter(USER__LOGIN_id=lid)
    l = []
    for i in var:
        l.append({
            'id': i.id,
            'Date': i.date,
            'status': i.status
            })


    return JsonResponse({'status': 'ok','data':l})

def View_order_sub_status(request):

    oid= request.POST["oid"]
    var = Order_sub.objects.filter(ORDER_id= oid)
    l = []
    for i in var:
        l.append({
            'id': i.id,
            'image':i.PRODUCT.image,
            'Product': i.PRODUCT.product_name,
            'Rate': i.PRODUCT.Rate,
            })
    return JsonResponse({'status': 'ok','data':l})

