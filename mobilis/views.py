from django.http import HttpResponse
from django.shortcuts import render

from classschedule.models import PersonalData
from classschedule.models import ClassSchedule


# Create your views here.
def wahome(request):
    return render(request, 'website/welcome.html',
                  {'student_numbers': PersonalData.objects.all()})


def mobilis(request):
    return render(request, 'website/details.html',
                  {'details': ClassSchedule.objects.all()})


def learn(request):
    return HttpResponse("Django is interesting")


def geek(request, id):
    meeting = ClassSchedule.objects.get(pk=id)
    return render(request, 'website/details.html', {'meeting': meeting})


def zooms(request):
    return render(request, "website/zoom.html",
                  {"zoomit": PersonalData.objects.all()})
