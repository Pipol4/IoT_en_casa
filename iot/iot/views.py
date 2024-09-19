from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
import serial, time


def index(request):

    return render(request, 'index.html')

def nosotros(request):

    return render(request, 'nosotros.html') 


def contacto(request):

    return render(request, 'contacto.html') 


def iluminacioninstantanea(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "a" + "," +  "1" 
        elif respuesta == 'b':
            envio = "a" + "," +  "2"
        elif respuesta == 'c':
            envio = "a" + "," +  "3"
        elif respuesta == 'd':
            envio = "a" + "," +  "4"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'iluminacioninstantanea.html')

def iluminacionprogramada(request):
    if request.method=='POST':
        hora = request.POST['hora']
        horados = request.POST['horados']
        horatres = request.POST['horatres']
        horacuatro = request.POST['horatres']
        enviodos = "b" + hora + "," + horados + "," + horatres + "," + horacuatro
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviodos.encode('ascii'))
        dev.close()
    return render(request, 'iluminacionprogramada.html')

def iluminacionsensor(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            enviotres = "c" + "," +  "1" 
        elif respuesta == 'b':
            enviotres = "c" + "," +  "2"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviotres.encode('ascii'))
        dev.close()

    return render(request, 'iluminacionsensor.html') 

def temperaturainstantanea(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "d" + "," +  "1" 
        elif respuesta == 'b':
            envio = "d" + "," +  "2"
        elif respuesta == 'c':
            envio = "d" + "," +  "3"
        elif respuesta == 'd':
            envio = "d" + "," +  "4"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'temperaturainstantanea.html')

def temperaturaprogramada(request):
    if request.method=='POST':
        hora = request.POST['hora']
        horados = request.POST['horados']
        enviodos = "d" + hora + "," + horados 
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviodos.encode('ascii'))
        dev.close()
    return render(request, 'temperaturaprogramada.html')


def temperaturasensor(request):
    if request.method=='POST':
        respuesta = request.POST.get('numero')
        enviotres = "e" + "," +  respuesta
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviotres.encode('ascii'))
        dev.close()

    return render(request, 'temperaturasensor.html') 


def riegoinstantaneo(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "f" + "," +  "1" 
        elif respuesta == 'b':
            envio = "f" + "," +  "2"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'riegoinstantaneo.html')

def riegoprogramado(request):
    if request.method=='POST':
        hora = request.POST['hora']
        horados = request.POST['horados']
        horatres = request.POST['horatres']
        horacuatro = request.POST['horatres']
        enviodos = "g" + hora + "," + horados + "," + horatres + "," + horacuatro + "," + horatres + "," + horacuatro + "," + horacinco + "," + horaseis 
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviodos.encode('ascii'))
        dev.close()
    return render(request, 'riegoprogramado.html')

def riegosensor(request):
    if request.method=='POST':
        hora = request.POST['porcentaje']
        hora = request.POST['porcentajedos']
        enviotres = "h" + "," +  porcentaje + "," +  porcentajedos
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviotres.encode('ascii'))
        dev.close()

    return render(request, 'riegosensor.html') 

def alarmainstantanea(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "i" + "," +  "1" 
        elif respuesta == 'b':
            envio = "i" + "," +  "2"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'alarmainstantanea.html')

def alarmaprogramada(request):
    if request.method=='POST':
        hora = request.POST['hora']
        horados = request.POST['horados']
        enviodos = "j" + hora + "," + horados 
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(enviodos.encode('ascii'))
        dev.close()
    return render(request, 'alarmaprogramada.html')

def aperturapuerta(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "i" + "," +  "1" 
        elif respuesta == 'b':
            envio = "i" + "," +  "2"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'aperturapuerta.html')

def general(request):
    if request.method=='POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'a':
            envio = "j" + "," +  "1" 
        elif respuesta == 'b':
            envio = "j" + "," +  "2"
        dev = serial.Serial("COM7",9600)
        time.sleep(2)
        dev.write(envio.encode('ascii'))
        dev.close()
    return render(request, 'general.html')

