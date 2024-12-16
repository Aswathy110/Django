from django.shortcuts import render, redirect
from .models import Book, Register
from django.contrib import messages




# Create your views here.
def home(request):
    if 'userid' in request.session:
        user = Register.objects.get(userid=request.session['userid'])
        print(user.userid)
        book_obj = Book.objects.all()
        return render(request, 'home1.html', {'data': book_obj,'obj':user})
    else:
        return redirect('/')


def add(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        book_obj = Book()
        book_obj.book_name = request.POST.get('book_name')
        book_obj.author = request.POST.get('author')
        book_obj.price = request.POST.get('price')
        book_obj.image = request.FILES.get('image')
        book_obj.save()
        return redirect('/home1')
    return render(request, 'content.html')


def delete(request, id):
    obj = Book.objects.get(book_id=id)
    obj.delete()
    return redirect('/')


def update(request, id):
    obj = Book.objects.get(book_id=id)
    if request.method == 'POST':
        print(request.POST)
        book_obj = Book.objects.get(book_id=id)
        book_obj.book_name = request.POST.get('book_name')
        book_obj.author = request.POST.get('author')
        book_obj.price = request.POST.get('price')
        book_obj.save()
        return redirect('/')
    return render(request, 'update.html', {'data': obj})


def view(request, id):
    obj = Book.objects.get(book_id=id)
    return render(request, 'viewmore.html', {'data': obj})


def register(request):
    if request.method == 'POST':
        obj = Register()
        obj.name = request.POST.get('name')
        obj.userid = request.POST.get('userid')
        obj.email = request.POST.get('email')
        obj.image = request.FILES.get('image')
        obj.save()
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        userid = request.POST.get('userid')
        name = request.POST.get('name')
        user = Register.objects.filter(userid=userid, name=name)
        print(user)
        if user:
            request.session['userid'] = userid
            messages.success(request, "You have successfully logged in.")
            return redirect('/home1/')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')


def logout(request):
    if 'userid' in request.session:
        del request.session['userid']
        return redirect('/')
