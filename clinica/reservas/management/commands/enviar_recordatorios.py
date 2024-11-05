from django.core.management.base import BaseCommand
from reservas.utils import enviar_recordatorios

class Command(BaseCommand):
    help = 'Envía recordatorios de citas un día antes'

    def handle(self, *args, **kwargs):
        enviar_recordatorios()
        self.stdout.write(self.style.SUCCESS('Recordatorios enviados correctamente'))
