from datetime import datetime as dt
from django.template import Template, Context
from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola que tal")

def alejandro(request):
    texto = "Soy alejandro<br>pelotudeando en la pagina"
    return HttpResponse(texto)

def dia_de_hoy(request):
    dia = dt.now()
    texto = f"puta que lo pario, hoy es <br>{dia}"
    return HttpResponse(texto)

def probando_template(request):
    nombre = "Matias"
    apellido = "Henquin"
    diccionario = {
        "nombre": nombre,
        "apellido": apellido,
        "notas": [4, 8, 9, 10, 7, 8]
    }
    mi_html = open('./Clases_coder/plantillas/index.html')
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
 