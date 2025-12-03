from django.contrib import admin
from .models import Payout, PayoutStatus


@admin.register(Payout)
class PayoutAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "amount",
        "currency",
        "recipient",
        "status",
        "created_at",
    )
    list_filter = ("status", "currency", "created_at")
    search_fields = ("id", "recipient")
    readonly_fields = ("id", "created_at", "updated_at")
    fieldsets = (
        ("Основная информация", {
            "fields": ("amount", "currency", "recipient", "description")
        }),
        ("Статус", {
            "fields": ("status",)
        }),
        ("Служебная информация", {
            "fields": ("id", "created_at", "updated_at"),
        }),
    )
