import django_filters
from .models import Payout

class PayoutFilter(django_filters.FilterSet):
    min_amount = django_filters.NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = django_filters.NumberFilter(field_name="amount", lookup_expr="lte")
    start_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="gte")
    end_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr="lte")

    class Meta:
        model = Payout
        fields = ["status", "currency", "min_amount", "max_amount", "start_date", "end_date"]
