"""
URL configuration for iot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from iot.views import index
from iot.views import nosotros
from iot.views import iluminacioninstantanea
from iot.views import contacto
from iot.views import iluminacionprogramada 
from iot.views import iluminacionsensor 
from iot.views import temperaturainstantanea
from iot.views import temperaturaprogramada
from iot.views import temperaturasensor
from iot.views import riegoinstantaneo
from iot.views import riegoprogramado
from iot.views import riegosensor
from iot.views import alarmainstantanea
from iot.views import alarmaprogramada
from iot.views import aperturapuerta
from iot.views import general

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('index/nosotros.html', nosotros),
    path('index/iluminacioninstantanea.html', iluminacioninstantanea),
    path('index/index.html', index),
    path('index/contacto.html', contacto),
    path('index/iluminacionprogramada.html', iluminacionprogramada),
    path('index/iluminacionsensor.html', iluminacionsensor),
    path('index/temperaturainstantanea.html', temperaturainstantanea),
    path('index/temperaturaprogramada.html', temperaturaprogramada),
    path('index/temperaturasensor.html', temperaturasensor),
    path('index/riegoinstantaneo.html', riegoinstantaneo),
    path('index/riegoprogramado.html', riegoprogramado),
    path('index/riegosensor.html', riegosensor),
    path('index/alarmainstantanea.html', alarmainstantanea),
    path('index/alarmaprogramada.html', alarmaprogramada),
    path('index/aperturapuerta.html', aperturapuerta),
    path('index/general.html', general),
]
