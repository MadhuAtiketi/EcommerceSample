from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from .models import Product, Register
from math import ceil
from django.utils import timezone

a = 0
canLogin=False
def Index(request):
    allProds = []
    catprods = Product.objects.values('category', 'id')

    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    print("Index Entry 1",canLogin)
    if canLogin:
        #print("MAAAAA",Login)
        params = {'allProds': allProds,'userinfo':uname}
    else:
        params = {'allProds': allProds,'userinfo':''}
    print("Index Entry 2")
    return render(request,"shop/index.html",params)

def About(request):
    return HttpResponse("About page of Shop")

def Tracker(request):
    return HttpResponse("Tracker page of Shop")

def Registery(request):
    if request.method == 'POST':
        firstname = request.POST.get('Firstname')
        print("FIRSTNAME",firstname)
        lastname = request.POST.get('Lastname')
        print("lastname :",lastname)
        middlename = request.POST.get('Middlename')
        username = request.POST.get('Username')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('Address')
        contact = request.POST.get('ContactNumber')
        Register.objects.create(firstname=firstname,middlename=middlename,lastname=lastname, username=username,mail=mail,password=password,address=address,contact=contact,
        cust_create_date=timezone.now())
    return render(request,"shop/register.html")

def registrySuccess(request):
    return HttpResponse("Registration Successfull")

def Login(request):

    if request.method == 'POST':
        print("Entry point")
        global uname
        global password
        global canLogin
        uname = request.POST.get('username')
        password = request.POST.get('password')
        print("MAMAAAAAAA")
        query = Register.objects.all()
        print("Entry point 1")
        canLogin=False
        for i in query:
            print(i.username)
            print("Entry point 2")
            if i.username== uname and i.password == password:
                canLogin=True
            else:
                canLogin = False
        if canLogin:
            return Index(request)
        else:
            return render(request, "shop/wrong_login.html")

    return render(request, "shop/login.html")

