from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    type=models.CharField(max_length=10)
class Recycle_unit(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    street=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    building_no=models.CharField(max_length=30)
    license_no=models.CharField(max_length=30)
    manager=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    status=models.CharField(max_length=100)

class User(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    username=models.CharField(max_length=30)
    gender=models.CharField(max_length=10,default='')
    phone_no=models.CharField(max_length=30,default='')
    house_name = models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    post=models.CharField(max_length=30)
    pincode=models.IntegerField()
    Email=models.CharField(max_length=30)

class Waste(models.Model):
    Waste_type=models.CharField(max_length=30)
    Rate=models.IntegerField()

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    image=models.CharField(max_length=100)
    type=models.CharField(max_length=30)
    Rate=models.IntegerField()
    RECYCLEUNIT= models.ForeignKey(Recycle_unit,on_delete=models.CASCADE)

class WorkerCategory(models.Model):
    Category = models.CharField(max_length=30)

class Worker(models.Model):
    name=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=100)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)
    email=models.CharField(max_length=30)
    gender=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
    photo=models.CharField(max_length=250,default=0)
    CATEGORY=models.ForeignKey(WorkerCategory,on_delete=models.CASCADE,default="2")

class Area(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    place = models.CharField(max_length=30)

class Area_Allocation(models.Model):
    AREA=models.ForeignKey(Area,on_delete=models.CASCADE)
    WORKER=models.ForeignKey(Worker,on_delete=models.CASCADE)

class Complaint(models.Model):
    complaint=models.CharField(max_length=200)
    date=models.DateField()
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=15)
    reply=models.CharField(max_length=200)

class feedback(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    feedback=models.CharField(max_length=30)

class Notification(models.Model):
    worker_notification=models.CharField(max_length=30)
    update_notification=models.CharField(max_length=30)
    product_notification=models.CharField(max_length=30)
    delivery_notification=models.CharField(max_length=30)

class Pickup(models.Model):
    vehicle=models.CharField(max_length=30)
    vehicle_no=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    Email=models.CharField(max_length=30)
    status=models.CharField(max_length=15)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default="1")

class Request(models.Model):
    WASTE=models.ForeignKey(Waste,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Status=models.CharField(max_length=15)
    Date=models.DateField()

class Cart(models.Model):
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date = models.CharField(max_length=100)

class Donation(models.Model):
    charity_center=models.CharField(max_length=30)
    acc_no=models.CharField(max_length=16,default='')
    ifsc=models.CharField(max_length=12,default='')
    amount=models.IntegerField()
    RECYCLE=models.ForeignKey(Recycle_unit,on_delete=models.CASCADE)

class Order(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    status=models.CharField(max_length=15)
    date=models.DateField()

class Order_sub(models.Model):
    ORDER=models.ForeignKey(Order,on_delete=models.CASCADE)
    PRODUCT=models.ForeignKey(Product,on_delete=models.CASCADE)

class Recycle_req(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    WORKER=models.ForeignKey(Worker,on_delete=models.CASCADE)
    status=models.CharField(max_length=15)
    date=models.DateField()

class Waste_req(models.Model):
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    WASTE = models.ForeignKey(Waste, on_delete=models.CASCADE)
    Narration = models.CharField(max_length=200)
    status = models.CharField(max_length=15)
    Date=models.DateField()
    qty = models.IntegerField()


class Bank(models.Model):
    cardnumber=models.CharField(max_length=100)
    Acname=models.CharField(max_length=100)
    expiredate=models.CharField(max_length=100)
    Cvv=models.CharField(max_length=100)
    Balance=models.IntegerField()





















