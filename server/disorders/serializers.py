from rest_framework import serializers

from .models import Symptom, Disorder


class DisordersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disorder
        fields = ('id', 'name')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SymptomsSerializer(serializers.ModelSerializer):
    disorders = DisordersSerializer(many=True)

    class Meta:
        model = Symptom
        fields = ('id', 'name', 'disorders')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
