from rest_framework import viewsets
from .serialize import TodoSerializer
from ..models import Todo

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    

