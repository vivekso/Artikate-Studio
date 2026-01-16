from rest_framework import serializers

class AttributesSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    country = serializers.CharField()
    account_age_days = serializers.IntegerField()
    monthly_volume = serializers.FloatField()
    kyc_verified = serializers.BooleanField()

class EvaluationRequestSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    attributes = AttributesSerializer()
