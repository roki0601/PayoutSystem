from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PayoutFilter
from .models import Payout
from .serializers import PayoutSerializer
from .tasks import process_payout_task

class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all().order_by("-created_at")
    serializer_class = PayoutSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PayoutFilter
    
    def perform_create(self, serializer):
        payout = serializer.save()
        process_payout_task.delay(str(payout.id))