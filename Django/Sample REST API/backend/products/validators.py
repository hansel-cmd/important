from rest_framework import serializers

def validate_price(value):
    if value < 10:
        raise serializers.ValidationError(f"Value {value} should be greater than 10")
    return value