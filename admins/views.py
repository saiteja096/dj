from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")
def admin(request):
    id=request.POST["name"]
    pword=request.POST["pword"]
    return render(request,"admin.html",{'name':id,'pword':pword})
def super_admin(request):
    id=request.POST["name"]
    pword=request.POST["pword"]
    return render(request,"super_admin.html",{'name':id,'pword':pword})
