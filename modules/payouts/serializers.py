from rest_framework import serializers
from .models import Payout, PayoutStatus

class PayoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payout
        fields = '__all__'
        read_only_fields = ["id", "created_at"]

    def validate_currency(self, value):
        """Валюта должна быть ISO кодом из 3 символов"""
        if len(value) != 3 or not value.isalpha():
            raise serializers.ValidationError("Валюта должна быть 3-буквенным ISO кодом.")
        return value.upper()
    
    def validate_recipient(self, value):
        if not value.strip():
            raise serializers.ValidationError("Реквизиты получателя обязательны.")
        if len(value) > 255:
            raise serializers.ValidationError("Реквизиты получателя слишком длинные (макс 255).")
        return value
    
    def validate_description(self, value):
        if value and len(value) > 255:
            raise serializers.ValidationError("Описание слишком длинное (макс 255 символов).")
        return value
    
    def validate_status(self, value):
        """Статус должен быть валидным"""
        if value not in PayoutStatus.values:
            raise serializers.ValidationError("Некорректный статус заявки.")
        return value