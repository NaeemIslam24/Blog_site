from django.shortcuts import render,redirect
from .models import Register
from .form import StudentRegister


def register(request):
    template = "register.html"
    form = StudentRegister()
    result = Register.objects.all()
    if request.method == 'POST':
        sform = StudentRegister(request.POST)
        if sform.is_valid():
            sform.save()
            return redirect('/register/')

    context = {

        'form': form,
        'results': result,

    }

    return render(request, template_name=template,context=context)


def delete(request,rm_number):
    if request.method == 'POST':
        data = Register.objects.get(id=rm_number)
        data.delete()
        return redirect('/register/')

def edit(request,data_number):

    template = 'edit.html'
    data = Register.objects.get(id=data_number)
    if request.method == 'POST':
     form = StudentRegister(request.POST,instance=data)
     if form.is_valid():
        form.save()
        return redirect('/register/')
    context = {
        'form':form,
    }
    return render(request, template_name=template,context=context)


