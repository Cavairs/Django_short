from django.core.management.base import BaseCommand
from main.models import Phone
import csv


class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def handle(self, *args, **options):
        with open("phones.csv", encoding='utf-8') as r_file:
            file_reader = csv.DictReader(r_file, delimiter=";")
            for row in file_reader:
                # Создаем объект Phone для каждой строки
                phone = Phone(
                    name=row['name'],
                    image=row['image'],
                    price=row['price'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'],
                    slug=row['name']
                )
                # Сохраняем объект в базе данных
                phone.save()
