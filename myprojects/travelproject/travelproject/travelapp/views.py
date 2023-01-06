from django.http import HttpResponse
from django.shortcuts import render
from .models import place, team


# Create your views here.



def demo(request):
   obj=place.objects.all()
   obj1 = team.objects.all()

   return render(request,"index.html",{'result':obj,'result1':obj1})

# def demo1(request):
#    obj=team.objects.all()
#
#    return render(request,"index.html",{'result1':obj})
#


# def Home(request):
#    return HttpResponse("Home")
#
# def about(request):
#    return render(request,"result.html")
#
# def contact(request):
#    return HttpResponse("contact")
#
# def details(request):
#    return render(request,"details.html")
#
# def Thanks(request):
#    return HttpResponse("Thanks")
#

# def addition(request):
#
#    x=int(request.GET['num1'])
#    y=int(request.GET['num2'])
#    res=x+y
#    res1=x*y
#    res2=x/y
#    res3=x-y
#
#    return render(request,"result.html",{'result':res,'result1':res1,'result2':res2,'result3':res3})


# def multiplication(request):
#    x1=int(request.GET['num1'])
#    y1=int(request.GET['num2'])
#    res1=x1-y1
# #
#    return render(request,"result.html",{'result':res1})

   # res2=x*y
   # res3=x/y


