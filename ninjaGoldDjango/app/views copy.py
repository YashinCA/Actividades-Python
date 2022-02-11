from pickle import NONE
from django.shortcuts import render, HttpResponse, redirect, reverse
# PARA EXTRAER FECHA Y HORA, FAVOR DE BORRAR EN CASO DE NO OCUPAR
from time import strftime, localtime
import datetime
import random


def index(request):
    context = {
        'saludo': 'Hola'
    }
    return redirect(reverse('presentacion:index'))


def process_money(request):
    print(request.POST)
    if request.POST.get('building') == None:
        request.session['activities'] = []
        request.session['winlost'] = ''
        request.session['goldstatus'] = 0
        request.session['contador'] = 0
        request.session['estado'] = False

    print(request.POST)

#####################################################

    green = 'green'
    red = 'red'
    date = datetime.datetime.now()
    datemoment = f'{date.strftime("%Y")}/{date.strftime("%m")}/{date.strftime("%d")} {date.strftime("%I")}:{date.strftime("%M")} {date.strftime("%p")}'
    diccionario = [{'name': 'farm', 'min': 10, 'max': 20}, {'name': 'cave', 'min': 5, 'max': 10}, {
        'name': 'house', 'min': 2, 'max': 5}, {'name': 'casino', 'min': -50, 'max': 50}]

    for i in range(4):
        numero = 0
        if diccionario[i]["name"] == request.POST.get('building'):
            numero = int(
                round(random.random()*(((diccionario[i]["max"])-(diccionario[i]["min"])))+(diccionario[i]["min"])))
            print(numero)
            request.session['goldstatus'] += numero
            request.session['contador'] += 1

            if (request.POST.get('building') == 'farm') or (request.POST.get('building') == 'cave') or (request.POST.get('building') == 'house'):
                form = request.POST.get('building')
                color = f'style = "color:{green} "'
                mensaje = f'<h5 {color}>Earned {numero} golds from the {form}! {datemoment}</h5>'
                request.session['activities'].append(mensaje)
            else:
                if((request.POST.get('building') == 'casino') and numero >= 0):
                    form = request.POST.get('building')
                    color = f'style = "color:{green} "'
                    mensaje = f'<h5 {color}>Entered a {form} and win {numero} golds...you are lucky! {datemoment}</h5>'
                    request.session['activities'].append(mensaje)
                else:
                    form = request.POST.get('building')
                    color = f'style = "color:{red} "'
                    mensaje = f'<h5 {color}>Entered a {form} and lost {numero} golds... Ouch... {datemoment}</h5>'
                    request.session['activities'].append(mensaje)

            if (request.session['goldstatus'] < 500):
                if((request.session['contador'] >= 0) and (request.session['contador'] < 5)):
                    request.session['estado'] = False
                else:
                    request.session['estado'] = True
                    color = f'style = "color:{red} "'
                    request.session['winlost'] = f'<h1 {color} >YOU LOST :(</h1>'
                print(request.session['estado'])
            if (request.session['goldstatus'] >= 200):
                if(request.session['contador'] == 5):
                    request.session['estado'] = False
                else:
                    request.session['estado'] = True
                    color = f'style = "color:{green} "'
                    request.session['winlost'] = f'<h1 {color} >YOU WIN</h1>'
                print(request.session['estado'])

    context = {
        'goldstatus': request.session['goldstatus'],
        'estado': request.session['estado'],
        'contador': request.session['contador'],
        'actividad': request.session['activities'],
        'winlost': request.session['winlost']
    }
    request.session['datos'] = context
    return render(request, 'app/index.html', context)


def farm(request):

    request.session['contador'] += 1
    context = {
        'goldstatus': request.session['goldstatus'],
        'estado': request.session['estado'],
        'contador': request.session['contador'],
        'actividad': request.session['activities'],
        'winlost': request.session['winlost']
    }
    print(request.session['datos']['contador'])
    return render(request, 'app/index.html', context)


def cave(request):
    pass


def house(request):
    pass


def casino(request):
    pass


# def second(request, name):
#     return HttpResponse('Hola ' + name)


# def redirigir(request):
#     return redirect('/')


# def time_display(request):
#     context = {
#         "fecha": strftime("%b %d, %Y", localtime()),
#         "hora": strftime("%H:%M %p", localtime()), }

#     return render(request, 'app/index.html', context)
