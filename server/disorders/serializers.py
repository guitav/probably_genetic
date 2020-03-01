from rest_framework import serializers

from .models import Disorders, Symptom, Disorder, Symptoms


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ('id', 'name', 'frequency')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


class DisorderSerializer(serializers.ModelSerializer):
    symptoms = SymptomSerializer(many=True)

    class Meta:
        model = Disorders
        fields = ('id', 'name',  'symptoms')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data


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
        model = Symptoms
        fields = ('id', 'name', 'disorders')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return data
