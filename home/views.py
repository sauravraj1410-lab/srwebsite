from django.shortcuts import render,HttpResponse
from datetime  import  datetime
from home.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def base(request):
    return render(request,'base.html')
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        message=request.POST.get("message")
        contact = Contact(name=name,email=email,mobile=mobile,message=message,date=datetime.today())
        contact.save()
        return HttpResponse("<h2>✅ Message sent successfully!</h2>")
    return render(request,'contact.html')
def game(request):
    return render(request,'game.html')
def joke(request):
    return render(request,'joke.html')
def story(request):
    return render(request,'story.html')
def motivation(request):
    return render(request,'motivation.html')
def telegram(request):
    return render(request,'telegram.html')
def reasoning(request):
    return render(request,'reasoning.html')