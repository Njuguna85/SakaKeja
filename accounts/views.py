from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
# Create your views here.

def register(request):
    if request.method == 'POST':
        ##get form values
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
    

        ##Check if passwords match
        if password == password2:
            ##check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "The username is taken")
                return redirect('register')
            else:
                ##Check email
                if User.objects.filter(email=email).exists():
                    messages.error(request, "The email is taken")
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,last_name=last_name)
                    ##Login in after register
                    """    auth.login(request, user)
                        messages.success(request, "You are now Logged in")
                        return redirect('index')"""
                    ## save the user
                    user.save()
                    messages.success(request, "You are now Registered. Now Login")
                    return redirect('login')
        # Display the error message        
        else:
            messages.error(request, 'Passwords Do Not Match!!')
            return redirect('register')
        
    else:
        return render (request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #authenticate user
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            ## login in the user
            auth.login(request, user)
            messages.success(request, "You are now Logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render (request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,"You have been logged out")
    return redirect ('index')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    
    context={
        'contacts': user_contacts
    }
    return render (request, 'accounts/dashboard.html', context)


