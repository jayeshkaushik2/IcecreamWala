from django.shortcuts import render, HttpResponse, redirect
from home.models import *
from django.db.models import Q
from datetime import datetime
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    print(User.objects.all())
    login_is = False
    if request.user.is_authenticated:
        login_is = True
    if request.method == 'POST':
        # we have to add the icecream to the cart/wishlist
        icecream = request.POST.get('item_id')
        print(icecream)
        return redirect('/')

    data = Icecream_item.objects.all()
    username = request.user.username
    
    Icecream_data = {
        'items' : data,
        'username': username,
        'login_is': login_is
    }
    return render(request, 'home.html', Icecream_data)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            massage = request.POST.get('massage')
            contact = Contact(name=name, email=email, password=password, massage=massage, date=datetime.today())
            contact.save()
            messages.success(request, 'Message has been sent!')
            return redirect('/')
        else:
            return render(request, 'contact.html')
    else:
        messages.success(request, 'Please login first!')
        return redirect('/login_user')

    
def wishlist(request):
    # shows the icecreams u wanted to perchase
    if request.method == 'POST':
        if request.user.is_authenticated:
            # we have to add that data to the wishlist
            return HttpResponse('this is it')
        else:
            return redirect('/login_user')
    if request.user.is_authenticated:
        return render(request, 'wishlist.html')
    else:
        return redirect('/login_user')


def searchlist(request):
    if request.method == 'GET':
        # searched name by the user
        icecream_name = request.GET.get('icecream_name').lower().strip()
        search = Search(icecream_name=icecream_name, date=datetime.today())
        search.save()
        data = Icecream_item.objects.all()
        context = {
            'item_name': icecream_name,
            'items': data
        }
        return render(request, 'searchlist.html', context)
    else:
        return HttpResponse('No data found!!')


def buy(request):
    '''
    first check if the user is loged in or not
    if the user is loged than address page
    if user is not loged in then go the the sign up page
    '''
    if request.user.is_authenticated:
        if request.method == 'POST':
            name = request.POST.get('item_name')
            price = request.POST.get('item_price')
            id = request.POST.get('item_id')
            item_details = {
                'name' : name,
                'price' : price,
                'id': id
            }
            print(item_details)
            return render(request, 'address.html', item_details)
        
    else:
        return redirect('/login_user')
    

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        user_password = request.POST.get('password')
        user = authenticate(username=user_name, password=user_password)
        if user is not None:
            login_is = True
            context = {
                'login_is':login_is
            }
            login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Your Password or Username is wrong!')

    if request.user.is_authenticated:
        messages.success(request, 'Your are already logged in!')
        return redirect('/')
    else:
        return render(request, 'login_user.html')


def logout_user(request):
    login_is = False
    context = {
        'login_is':login_is
    }
    logout(request)
    return render(request, 'login_user.html', context)


def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname  = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conform_password = request.POST.get('conform_password')

        if len(password) < 8:
            messages.success(request, 'Your password should be atleast of 8 characters!')
            return redirect('/signup')

        elif  password != conform_password:
            messages.success(request, 'Conform password is not matching!')
            return redirect('/signup')

        elif len(username) >= 20:
            messages.success(request, 'Your username should contain less than 20 characters!')
            return redirect('/signup')

        else:
            user_profile = User_profile(first_name=firstname, last_name=lastname, username=username, email=email, password=password, logged_in=logged_in)
            # user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password)
            user_profile.save()
            # login(request, user)
            return redirect('/')

    if request.user.is_authenticated:
        messages.success(request, 'you are already logged in!')
        return redirect('/')
    else:
        return render(request, 'signup.html')


def address(request):
    if request.user.is_authenticated:
        return render(request, 'address.html')
    else:
        return redirect('/login_user')


def save_address(request):
    if request.method == 'POST':
        # item details is below, we have to save this is model name Item_details
        item_id_is = request.POST.get('item_id')
        item_name  = request.POST.get('item_name')
        item_price      = request.POST.get('item_price')

        print(item_id_is, item_name, item_price)

        item = Items(name=item_name, item_id=item_id_is, price=item_price)
        item.save()
        bought_items = Bought_items(item=item)
        bought_items.save()
        # user Address and information about user is below
        username     = request.user.username
        email        = request.user.email
        country      = request.POST.get('country')
        fullname     = request.POST.get('fullname')
        mobilenumber = request.POST.get('mobilenumber')
        pincode      = request.POST.get('pincode')
        home_address = request.POST.get('home_address')
        village      = request.POST.get('village')
        landmark     = request.POST.get('landmark')
        town_city    = request.POST.get('town_city')
        state        = request.POST.get('state')
        
        address = Address(username=username, email=email, country=country, fullname=fullname, mobilenumber=mobilenumber,
        pincode=pincode, home_address=home_address, village=village,
         landmark=landmark, town_city=town_city, state=state, item_id=bought_items, date=datetime.today())
        address.save()
        messages.success(request, 'Your order has been placed!!')
        return redirect('/')


def user_profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        fullname = request.user.get_full_name()
        context = {
            'username': username,
            'fullname': fullname
        }
        return render(request, 'user_profile.html', context)
    else:
        messages.success(request, 'Login your account first!')
        return redirect('login_user')