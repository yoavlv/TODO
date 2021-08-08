from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Todo
from  django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-pub_date")  # Take all the item from the DB and order by date
    return render(request, 'index.html', {"todo_items": todo_items})

@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    crated_obj = Todo.objects.create(pub_date=current_date, text = content)
    lenght_of_todos = Todo.objects.all().count()  #Check the lenght of the DB not realy relevent
    return HttpResponseRedirect("/polls/")    #מבצע את הפעולה ומציג את הדף מחדש כמו Refresh


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/polls/")



