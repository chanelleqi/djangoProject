from django.shortcuts import render, redirect
from myapp import support_functions
from myapp.models import Currency, User1
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    data = dict()
    import datetime
    time = datetime.datetime.now()
    data["time_of_day"] = time
    print(time)
    return render(request,"home.html",context=data)


from django.http import HttpResponseRedirect
from django.urls import reverse
def maintenance(request):
    data = dict()
    choice = "HOME"
    try:
        choice = request.GET['selection']
        if choice == "currencies":
            support_functions.add_currencies(support_functions.get_currency_list())
            c_list = Currency.objects.all()
            print("Got c_list",len(c_list))
            data['currencies'] = c_list
            return HttpResponseRedirect(reverse('currencies'))
    except:
        pass
    print(choice)

    return render(request,"maintenance.html",context=data)

def view_currencies(request):
    data = dict()
    c_list = Currency.objects.all()
    data['currencies'] = c_list
    return render(request,'currencies.html',context=data)

def currency_selection(request):
    data = dict()
    currencies =Currency.objects.all()
    data['currencies'] = currencies
    return render(request,"currency_selector.html",data)

def exch_rate(request):
    data=dict()
    try:
        currency1 = request.GET['currency_from']
        currency2 = request.GET['currency_to']
        c1 = Currency.objects.get(iso=currency1)
        c2 = Currency.objects.get(iso=currency2)
        data['currency1'] = c1
        data['currency2'] = c2
        try:
            rate = c1.rates_set.get(x_currency=c2.iso).rate
            data['rate'] = rate
        except:
            data['rate'] = "Not Available"
    except:
        pass
    return render(request,"exchange_detail.html",data)


from .models import User1
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        horoscope = request.POST.get('horoscope')
        if name and horoscope:
            # Create a new User1 object and save to the database
            user = User1(name=name, horoscope=horoscope)
            user.save()
            return render(request, 'userform.html')
        else:
            return redirect('maintenance')
    else:
        return render(request, 'userform.html')


def userinfo(request):
    users = User1.objects.all()
    return render(request, 'userinfo.html', {'users': users})