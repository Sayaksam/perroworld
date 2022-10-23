from rest_framework import serializers
from .models import Clinics


class ClinicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinics
        fields = ["id", "name", "owner", "address"]
