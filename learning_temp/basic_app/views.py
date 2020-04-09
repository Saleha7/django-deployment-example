from django.shortcuts import render
from basic_app.forms import NewUser

# Create your views here.
def index(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context_dict)
def base(request):
    return render(request,'basic_app/base.html')
def relative(request):
    return render(request,'basic_app/relative_url_templates.html')
def users(request):
    form=NewUser()
    if request.method=="POST":
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request,'basic_app/others.html',{'form':form})
