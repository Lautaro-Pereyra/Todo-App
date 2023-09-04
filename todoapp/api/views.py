from django.shortcuts import render
from .serializer import TareaSerializer
from .models import Tarea

from rest_framework import generics

# Create your views here.

class TareaList(generics.ListAPIView):
    queryset = Tarea.objects.all()
    lookup_url_kwarg = 'tarea_id'
    serializer_class = TareaSerializer



class TareaCreate(generics.CreateAPIView):
    queryset = Tarea.objects.all()
    lookup_url_kwarg = 'tarea_id'
    serializer_class = TareaSerializer


class TareaUpdate(generics.RetrieveUpdateAPIView):
    queryset = Tarea.objects.all()
    lookup_url_kwarg = 'tarea_id'
    serializer_class = TareaSerializer


class TareaDelete(generics.RetrieveDestroyAPIView):
    queryset = Tarea.objects.all()
    lookup_url_kwarg = 'tarea_id'
    serializer_class = TareaSerializer

