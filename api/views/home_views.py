#home.views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from api.models import ToDoItem
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def home(request):
    shared_data = request.session.get('shared_data', None)
    if shared_data is not None :
        print("my_token.exists")
        print(shared_data)
        todos = ToDoItem.objects.all()
        if len(todos) == 0:
            todos = {}
        return render(request, 'home.html', {'todos': todos, 'shared_data': shared_data})
    else:
        print("notexists") 
        print(shared_data)  # Properly indented
        todos = ToDoItem.objects.all()
        if len(todos) == 0:
            todos = {}
        return render(request, 'home.html', {'todos': todos})





	
	
		
	

def create_todo(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		due_date = request.POST.get('due_date')
		ToDoItem.objects.create(title=title, description=description,due_date=due_date)

	return redirect('home')

def complete_todo(request,todo_id):
	todo = ToDoItem.objects.get(id=todo_id)
	todo.completed = True
	todo.save()
	return redirect('home')

def delete_todo(request,todo_id):
	todo = ToDoItem.objects.get(id=todo_id)
	todo.delete()
	
	return redirect('home')
