from django.shortcuts import render
#from django.http import HttpResponse
from .models import Lesson, Assignment, ClassFile
import datetime

# Create your views here.

def index(request):
    lessons = Lesson.objects.all().order_by('date') #add the filter for this. https://stackoverflow.com/questions/761352/django-queryset-order?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa says i need a dash in front?
    assignments = Assignment.objects.all()
    classfiles = ClassFile.objects.all()

    lsn_dates = []
    for lsn in lessons:
        formatted_time = lsn.date.strftime('%B %d, %Y').replace(" 0", " ")
        lsn_dates.append(formatted_time)
        
    formatted_time = get_next_lesson_date(lsn_dates)
    
    return render(request, 'index.html', {'lessons':lessons, 'assignments':assignments, 'classfiles':classfiles, 'formatted_time':formatted_time})



def resources(request):

    return render(request, 'resources.html', {})





# Added functionality, not to be called directly. Gives back date to jump to on load.

def get_next_lesson_date(lsn_dates):
    today = datetime.date.today() # use this to set website to actual time-now. Just uncomment
    #today = datetime.date(2018,3,5) # use this to assign arbitrary date for testing.

    for i in range(30):
        formatted_time = today.strftime('%B %d, %Y').replace(" 0", " ")
        if formatted_time not in lsn_dates:
            today += datetime.timedelta(days=1)
            #print("Not correct: " + formatted_time)
        else:
            #print(formatted_time)
            return formatted_time
    
