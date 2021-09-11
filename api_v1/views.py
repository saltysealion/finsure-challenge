from rest_framework.viewsets import ModelViewSet
from finsure.models import Lender
from .serializers import LenderSerializer


class LenderViewSet(ModelViewSet):
    queryset = Lender.objects.all()
    serializer_class = LenderSerializer
    filterset_fields = {
        'active': ('exact', ),
    }
    search_fields = (
        'id',
        'code',
    )
