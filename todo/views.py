from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo, Member
from django.http import HttpResponse,  FileResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.hashers import make_password
from .models import Member
from datetime import datetime

# todo/views.py



def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('todo_item')
        if text:
            Todo.objects.create(text=text)
    return redirect('todo_list')

def update_todo(request, id):
    if request.method == 'POST':
        todo = Todo.objects.get(id=id)
        todo.completed = not todo.completed
        todo.save()
    return redirect('todo_list')

def delete_todo(request, id):
    if request.method == "POST":
        todo = get_object_or_404(Todo, id=id)
        todo.delete()
    return redirect('todo_list')


def index(request):
    return render(request, 'todo/index.html')

def register(request):
    return render(request, 'todo/register.html')

def validate_form_data(name, email, password, password2, age_str):
    if not all([name, email, password, password2, age_str]):
        return "請輸入完整的資料"
    
    if Member.objects.filter(user_name=name).exists():
        return "此名字已存在!"
    
    if Member.objects.filter(user_email=email).exists():
        return "信箱已被註冊!!"
    
    if password != password2:
        return "密碼不一樣!!"
    
    try:
        age = int(age_str)
        if age <= 0:
            return "年紀必須大於0"
    except (ValueError, TypeError):
        return "年紀請輸入數字"

    return None  # Validation passed

def register_check(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Guest')
        email = request.POST.get('email', 'Guest@company.com')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        age_str = request.POST.get('age', '30')

        error_message = validate_form_data(name, email, password, password2, age_str)
        if error_message:
            return HttpResponseBadRequest(error_message)

        avatar = request.FILES.get('avator')
        
        upload_file = None

        if avatar:
            fs = FileSystemStorage()
            upload_file = fs.save(avatar.name, avatar)

        Member.objects.create(
            user_name=name,
            user_password=make_password(password),
            user_age=int(age_str),
            user_email=email,
            user_avatar=upload_file,
            last_update=datetime.now()
        )

        return HttpResponse("已完成註冊!!")
    
    # Handle GET request or other methods
    return HttpResponse("請使用 POST 方法提交註冊表單", status=405)

        


def check_name(request):
    
    name = request.GET.get('name')
    cheName = Member.objects.filter(user_name=name).exists()
    if cheName:
        content = "此名字已存在!"
    else:
        content = "此名字可使用!"

    return HttpResponse(content, content_type='text/plain; charset=utf-8')



def travel(request):
    return render(request, 'todo/travel.html', {'title': 'Travel Data'})
