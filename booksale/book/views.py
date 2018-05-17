from django.shortcuts import render, redirect
from .models import User, Book, Bill
from django.db.models import Q

# Create your views here.
def login(request):
    ctx = {}
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = User.objects.filter(username=username, password=password).first()

        if not user:
            ctx['error'] = '用户名密码错误'
            return render(request, 'login.html', ctx)

        request.session['user_id'] = str(user.id)
        request.session['name'] =  user.name

        return redirect(index)

    return render(request, 'login.html', ctx)

def index(request):
    ctx = {}
    ctx['newbooks'] = Book.objects.order_by('create_time')[::-1][0:3]
    ctx['hotbooks'] = Book.objects.order_by('count')[::-1][0:3]
    if 'user_id' in request.session:
        ctx['name'] = request.session['name']

    return render(request, 'index.html', ctx)

def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']

    return redirect(login)

def search(request):
    ctx = {}
    if 'user_id' in request.session:
        ctx['name'] = request.session['name']
    if request.method == "POST":
        q = request.POST.get('q','')
        ctx['books'] = Book.objects.filter(Q(name__icontains=q) | Q(author__icontains=q))


        return render(request, 'booklist.html', ctx)