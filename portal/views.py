from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest


def vista_inicio(request):
    return render(
        request,
        'portal/inicio.html',
        {
            'titulo': 'Incio',
            'fecha': datetime.now().year,
        }
    )


def vista_contactenos(request):
    return render(
        request,
        'portal/contacto.html',
        {
            'titulo': 'Contactenos',
            'mensaje': 'Envíenos sus comentarios.',
            'fecha': datetime.now().year,
        }
    )


def vista_acercade(request):
    return render(
        request,
        'portal/nosotros.html',
        {
            'titulo': 'About',
            'mensaje': 'MiApp tu asistente virtual.',
            'fecha': datetime.now().year,
        }
    )

