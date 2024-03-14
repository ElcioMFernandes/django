from rest_framework import viewsets
from api.models import Cedente, Banco
from api.serializer import CedenteSerializer, BancoSerializer

class CedentesViewSet(viewsets.ModelViewSet):
    queryset = Cedente.objects.all()
    serializer_class = CedenteSerializer

class BancosViewSet(viewsets.ModelViewSet):
    queryset = Banco.objects.all()
    serializer_class = BancoSerializer