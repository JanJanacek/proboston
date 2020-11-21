from django.shortcuts import render, HttpResponseRedirect
from web.forms import UserForm


def index(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form})