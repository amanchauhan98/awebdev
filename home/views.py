from django.shortcuts import render, redirect
from home.models import feedback, userdata, basicPython, Cprog, websites, code_desc, c_code
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.  # password ; fuck123##, sunil user
def index(request):
    if request.user.is_anonymous:
        return redirect("/view_login")
    
    pythonB = basicPython.objects.all()
    Cprogram = Cprog.objects.all()
    web = websites.objects.all()
    # for Paginator code 
    pages1 = Paginator(pythonB, 3)
    page_number1 = request.GET.get('page')
    pythonBfinal = pages1.get_page(page_number1)

    # for C paginator code 
    pages2 = Paginator(Cprogram, 3)
    page_number2 = request.GET.get('page')
    Cprogramfinal = pages2.get_page(page_number2)

    params = {
        "progP": pythonBfinal,
        "progC" : Cprogramfinal,
        "web_site": web
    }

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        # print(name, email, message)
        ins = feedback(name=name, email=email, message=message)
        ins.save()

    
    return render(request, 'index.html', params)

def about(request):
    if request.user.is_anonymous:
        return redirect("/view_login")
       
    return render(request, 'about.html')



def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('first-name','')
        lname = request.POST.get('last-name','')
        email = request.POST.get('email-address','')
        password = request.POST.get('password','')
        Rpassword = request.POST.get('password-text','')
        website = request.POST.get('company-website','')
        state = request.POST.get('state','')
        address = request.POST.get('street-address','')
        city =  request.POST.get('city','')
        postalcode = request.POST.get('postal-code','')
        file_upload = request.POST.get('file-upload','')
        print(fname, lname,email, password, website, Rpassword, state,  address, city, postalcode)

        user = User.objects.create_user(fname, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        ins = userdata(fname=fname, lname=lname, email=email, password=password, Rpassword=Rpassword, website=website, state=state, address=address, city=city, postalcode=postalcode, file_upload = file_upload)
        ins.save()
        send_mail(
        f'Welcome {fname} in Our A-Web Developer Community',
        f'This is a Welcome Mail MR. MS {fname}. In Our Community You are free to do anything.',
        'avinashthakurchauhan07@gmail.com',
        [f'{email}'],
        fail_silently= False

    ) 




    return render(request, 'contact.html')





def view_login(request):
    if request.method == 'POST':
        username = request.POST.get('fname','')
        password = request.POST.get('password','')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else :
            return render(request, 'login.html')

    return render(request, 'login.html')









def work(request):
    if request.user.is_anonymous:
        return redirect("/view_login")
    ckacode = Cprog.objects.all()
    pykacode = basicPython.objects.all()
    params = {
        'works':ckacode,
        'pythons':pykacode
    }    
    return render(request, 'work.html', params)

def view_logout(request):
    logout(request)
    return redirect('/view_login')


# main imp func
def detailC(request,new_slug):
    code = code_desc.objects.get(new_slug = new_slug)
    print(code)
    params = {
        "code" : code
    }
    return render(request, 'code_detail.html', params)  

def c_codes(request, new_slug):
    codes = c_code.objects.get(new_slug = new_slug)
    print(codes)
    params = {
        "codes":codes
    }
    return render(request, "c_code_detail.html", params)

