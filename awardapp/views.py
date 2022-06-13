from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
import datetime as dt

from awardapp.models import Profile
from .forms import AddProjectForm

# Create your views here.


def home(request):
    date = dt.date.today()
    return render(request, "home.html", {"date": date})

def profile(request):
    return render(request, "user/profile.html")

def project(request):
    return render(request, "project/project.html") 
   
def add_project(request):
    if request.method == "POST":
        form = AddProjectForm(request.POST, request.FILES)
        current_user = request.user
        try:
            profile = Profile.objects.get(user = current_user)
        except Profile.DoesNotExist:
            raise Http404()
        if form.is_valid():
            project = form.save(commit= False)
            project.profile = profile
            project.save()

        return redirect("home")
    else:
        form = AddProjectForm()
    return render(request, 'project/add_project.html', {"form": form}) 

