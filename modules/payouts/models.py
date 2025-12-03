import uuid
from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator


class PayoutStatus(models.TextChoices):
    NEW = "new", "Новый"
    PROCESSING = "processing", "В процессе"
    COMPLETED = "completed", "Обработана"
    FAILED = "failed", "Ошибка"


class Payout(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        verbose_name="ID заявки",
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        validators=[
            MinValueValidator(Decimal("0.01")),
        ],
        verbose_name="Сумма выплаты",
    )
    currency = models.CharField(
        max_length=3,
        verbose_name="Валюта",
        help_text="Код валюты ISO 4217 (например, RUB)",
    )
    recipient = models.CharField(
        max_length=255,
        verbose_name="Реквизиты получателя",
    )
    status = models.CharField(
        max_length=20,
        choices=PayoutStatus.choices,
        default=PayoutStatus.NEW,
        verbose_name="Статус",
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Заявка на выплату"
        verbose_name_plural = "Заявки на выплату"

    def __str__(self) -> str:
        return f"Заявка {self.id}"
