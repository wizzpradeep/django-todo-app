from django.shortcuts import redirect, render, get_object_or_404
from .models import TodoModel
from django.views import View
from datetime import datetime

class ToDoView(View):
    def get(self, request):
        todos = TodoModel.objects.all()
        context = {
            'todos': todos
        }
        return render(request, 'todo.html', context=context)
    
    def post(self, request):
        todoname = request.POST.get('todoName')
        todotime = request.POST.get('todoTime')
        try:
            todotime = datetime.strftime(todotime,'%H:%M').time()
        except:
            pass

        TodoModel.objects.create(todo= todoname, time= todotime)


        return redirect('todo')


def clear_all(request):
    TodoModel.objects.all().delete()
    return redirect('todo')


def delete_todo(request, id):
    todo = get_object_or_404(TodoModel, id=id)
    todo.delete()
    return redirect('todo')