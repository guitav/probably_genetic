import xml.etree.ElementTree as ET

from django.core.management import BaseCommand
from disorders.models import Disorder, Symptom

# Create many to many relationship between symptoms and disorders


class Command(BaseCommand):
    help = "Load data from data/en_product4_HPO.xml file into Disorder Model"

    def handle(self,  *args, **options):
        if Disorder.objects.exists():
            print("Disorders have already been loaded")
            return
        tree = ET.parse('./data/en_product4_HPO.xml')
        root = tree.getroot()
        for row in root.findall('.//Disorder'):
            disorder = Disorder()
            disorder.name = row.find('Name').text
            associations = row.findall('.//HPODisorderAssociation')
            disorder.save()
            for association in associations:
                name = association.find('.//HPOTerm').text
                symptom, created = Symptom.objects.get_or_create(name=name)
                symptom.disorders.add(disorder)
                symptom.save()
            disorder.save()
            print(f"Completed inserting data on {disorder.name}")
