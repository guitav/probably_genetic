import xml.etree.ElementTree as ET

from django.core.management import BaseCommand
from disorders.models import Disorders, Symptom, Disorder, Symptoms


class Command(BaseCommand):
    help = "Load data from xml file into Disorder Model"

    def handle(self,  *args, **options):
        if Symptoms.objects.exists():
            print("Symptoms have already been loaded")
            return
        tree = ET.parse('./data/en_product4_HPO.xml')
        root = tree.getroot()
        for row in root.findall('.//Disorder'):
            disorder = Disorder()
            disorder.name = row.find('Name').text
            disorders = Disorders()
            disorders.name = row.find('Name').text
            associations = row.findall('.//HPODisorderAssociation')
            disorder.save()
            disorders.save()
            for association in associations:
                name = association.find('.//HPOTerm').text
                freq = association.find('.//HPOFrequency/Name').text
                symptom, created = Symptoms.objects.get_or_create(name=name)
                symptom.disorders.add(disorder)
                symptom.save()
                symptoms = Symptom(name=name, frequency=freq)
                symptoms.save()
                disorders.symptoms.add(symptoms)
            print ("Insertion")
            disorder.save()
            disorders.save()
