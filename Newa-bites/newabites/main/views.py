from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail,EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    return render(request,'user/home.html')
def contribution(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        recipename = request.POST['recipename']
        recipe = request.POST['recipe']
        history = request.POST['history']
        contribution = Contribution(name=name,email=email,recipename=recipename,recipe=recipe,history=history)
        contribution.save()
        subject="Your Recipe has been submitted"
        message=render_to_string('user/message.html',{'name':name})
        from_email='newabites@gmail.com'
        recipient_list=[email]
        msg_email=EmailMessage(subject,message,from_email,recipient_list)
        msg_email.send(fail_silently=True)
        # messages.success(request,f"Hi {name}, your form has been successfully submitted.")
        return redirect('home')
    return render(request,'user/contribution.html')
def recommendations(request,id):
    data=Recipe.objects.get(id=id)
    dd=Shop.objects.all()
    d = OnlineShop.objects.select_related('ingredient').all()
    restro=Restaurant.objects.all()
    return render(request,'user/recommendations.html',{'data':data,'shops':dd,'onlineshops':d,'restro':restro})


def recipe(request,id):
    data=Recipe.objects.get(id=id)
    return render(request,'user/recipe.html',{'data':data})
def listoffood(request):
    data=Recipe.objects.all()
    return render(request,'user/listoffood.html',{'data':data})

def donate(request):
    data=Recipe.objects.all()
    return render(request,'user/donate.html',{'data':data})