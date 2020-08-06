from rest_framework import serializers

from . models import Agregate


class AgregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agregate
        fields = '__all__'