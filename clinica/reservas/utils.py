from twilio.rest import Client
from django.utils import timezone
from .models import Cita

def enviar_recordatorios():
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    client = Client(account_sid, auth_token)

    citas = Cita.objects.filter(recordatorio_enviado=False, fecha=timezone.now().date() + timezone.timedelta(days=1))
    for cita in citas:
        mensaje = f"Hola {cita.paciente.nombre}, le recordamos su cita mañana a las {cita.hora}."
        client.messages.create(
            from_='whatsapp:+14155238886',  # Número de Twilio
            to=f'whatsapp:{cita.paciente.telefono}',
            body=mensaje
        )
        cita.recordatorio_enviado = True
        cita.save()
