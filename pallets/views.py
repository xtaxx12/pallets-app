from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Pallet
from .serializers import PalletSerializer

class PalletViewSet(viewsets.ModelViewSet):
    queryset = Pallet.objects.all()
    serializer_class = PalletSerializer

    @action(detail=True, methods=['patch'])
    def cambiar_estado(self, request, pk=None):
        pallet = self.get_object()
        pallet.estado = 'RECIBIDO'
        pallet.save()
        return Response({'status': 'estado actualizado'})
