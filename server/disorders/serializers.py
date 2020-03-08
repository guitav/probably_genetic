from rest_framework import serializers

from .models import Symptom, Disorder


class SymptomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = ('id', 'name', 'disorders',)
        depth = 1

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class SymptomsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symptom
        fields = ('id', 'name',)
        depth = 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class DisordersSerializer(serializers.ModelSerializer):
    symptom_list = SymptomsSerializer(many=True)

    class Meta:
        model = Disorder
        fields = ('id', 'name', 'symptom_list')
        depth = 0

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
