from django.shortcuts import render, redirect

from myapp import support_functions
from myapp.models import Currency, Names, ZodiacSign


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



from django.http import HttpResponseRedirect
from django.urls import reverse

def userform(request):
    data = dict()
    try:
        choice = request.GET['selection']
        if choice == "zodiac":
            support_functions.add_zodiac(support_functions.scrape_zodiac())
            z_list = ZodiacSign.objects.all()
            print("Got z_list",len(z_list))
            data['zodiac'] = z_list
            return HttpResponseRedirect(reverse('userinfo'))
    except:
        pass
    return render(request,"userform.html",context=data)

def view_Zodiac(request):
    data = dict()
    z_list = ZodiacSign.objects.all()
    data['zodiac'] = z_list
    return render(request,'userinfo.html',context=data)

