import sqlite3
from django.shortcuts import redirect, render, reverse
from scovilleapp.models import ScovilleScale
from ..connection import Connection


def scovillescale_list(request):
    if request.method == 'GET':
        scale_list = ScovilleScale.objects.all()

        template = 'scoville_scale/sslist.html'
        context = {
            'scale_list': scale_list
        }
        return render(request, template, context)
