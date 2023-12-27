from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory


from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    template = 'meetings/detail.html'
    meeting = get_object_or_404(Meeting, pk = id)
    context = {
        'meeting': meeting
    }
    print(meeting)
    return render(request, template, context)

def rooms_list(request):
    template = 'meetings/rooms.html'
    rooms = Room.objects.all()
    print(rooms)
    context = {
        'rooms': rooms
    }

    return render(request, template, context)


MeetingForm = modelform_factory(Meeting, exclude = [])

def new(request):
    template = 'meetings/new.html'
    form = MeetingForm()
    
    
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
        
    context = {
        'form': form
    }

    return render(request, template, context)