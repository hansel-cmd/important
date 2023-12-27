from django.http import HttpResponse
from django.shortcuts import render

# If the models are on a different application, 
# import it using the name of the application.
# Otherwise, use .models
from meetings.models import Meeting



# Create your views here.
def welcome(request):
    template = 'website/welcome.html'
    meetings = Meeting.objects.all()
    num_meetings = Meeting.objects.count()
    context = {
        'meetings': meetings
    }
    return render(request, template, context)

def about(request):
    return HttpResponse(
        "Hello world, "
        "Test application!"
    )