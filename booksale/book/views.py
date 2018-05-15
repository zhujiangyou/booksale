from django.shortcuts import render
from .models import User

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
        request.session['name'] = user.name

        return render(request, 'index.html', ctx)

    return render(request, 'login.html', ctx)
