from rest_framework import serializers

class UserPublicDataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    username = serializers.CharField(read_only = True)
    email = serializers.CharField(read_only = True)