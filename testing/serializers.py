from rest_framework import serializers
from .models import  Expand


class ExpandSerializer(serializers.Serializer):
    class Meta:
        model = Expand
        field = ('expression')