from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Sonn
from .forms import konfi, gd
from time import sleep as wait
import logging
import datetime

# Create your views here.
def zeige(request):
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(7)
    end_week1= start_week + datetime.timedelta(7)
    end_week2= start_week + datetime.timedelta(208)
    kawo = datetime.date.today().strftime("%V")
    gd1 = Sonn.objects.filter(datum__range=[start_week, end_week]).order_by('datum')
    dg2 = Sonn.objects.filter(datum__range=[end_week1, end_week2]).order_by('datum')
    return render(request, 'chat/test.html', {'kawo':kawo, 'gd1':gd1, 'gd2':dg2, })

def add(request):
    if request.user.is_authenticated():
        gd = Sonn.objects.all().order_by('datum')
        return render(request, 'chat/add.html', {'gd': gd, })
    else:
        return HttpResponseRedirect('/login')


def edit(request):
    if request.user.is_authenticated():
        id = request.GET.get('id')
        gd = Sonn.objects.filter(id=id)
        return render(request, 'chat/edit.html', { 'gd':gd})
    else:
        return HttpResponseRedirect('/')


def get_name(request):
    if request.user.is_authenticated():
        id = request.GET.get('id')
        b = Sonn.objects.filter(id=id).first()
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = konfi(request.POST)
        # check whether it's valid:
            if form.is_valid():
                konfis = form.cleaned_data['konfiname']
                b1 = Sonn.objects.get(id=id)
                b1.konfi = konfis
                b1.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

                return HttpResponseRedirect('/add/')

    # if a GET (or any other method) we'll create a blank form
        else:
            form = konfi()

        return render(request, 'chat/edit.html', {'form': form, 'b':b})
    else:
        return HttpResponseRedirect('/')

def addgd(request):
    if request.user.is_authenticated():
    # if this is a POST request we need to process the form data
        if request.method == 'POST':
        # create a form instance and populate it with data from the request:
            form = gd(request.POST)
        # check whether it's valid:
            if form.is_valid():
                kirche = form.cleaned_data['kirche']
                Datum = form.cleaned_data['datum']

                b2 = Sonn(kirche=kirche, datum=Datum,konfi="")
                b2.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

                return HttpResponseRedirect('/add/')

    # if a GET (or any other method) we'll create a blank form
        else:
            form = gd()

        return render(request, 'chat/addgd.html', {'form': form})
    else:
        return HttpResponseRedirect('/')