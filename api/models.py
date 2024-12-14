from django.db import models

# Create your models here.


class Settlement (models.Model):
    admission_numer = models.CharField(max_length=20, null=True, blank=True)
    biller = models.CharField(
        max_length=255, null=True, blank=True)  # Facturador
    received_file = models.BooleanField(default=False)  # Expediente Recibido
    reception_date = models.DateTimeField(
        null=True, blank=True)  # Fecha de Recepción
    settled = models.BooleanField(default=False)  # Liquidado
    settled_date = models.DateTimeField(
        null=True, blank=True)  # Fecha de Liquidación
    audited = models.BooleanField(default=False)  # Auditoría
    audited_date = models.DateTimeField(
        null=True, blank=True)  # Fecha de Auditoría
    billed = models.BooleanField(default=False)  # Facturado
    last_invoice = models.CharField(
        max_length=20, null=True, blank=True)  # Última Factura
    shipped = models.BooleanField(default=False)  # Enviado
    shipment_date = models.DateTimeField(
        null=True, blank=True)  # Fecha de Envío
    paid = models.BooleanField(default=False)  # Pagado
    payment_date = models.DateTimeField(null=True, blank=True)  # Fecha de Pago
    status = models.CharField(max_length=20, choices=[
        ('Pendiente', 'Pendiente'),
        ('Liquidado', 'Liquidado'),
        ('Auditoría', 'Auditoría'),
        ('Facturado', 'Facturado'),
        ('Enviado', 'Enviado'),
        ('Pagado', 'Pagado')
    ], default='Pendiente')
    period = models.CharField(max_length=255, null=True, blank=True)  # Periodo
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de Creación
    updated_at = models.DateTimeField(
        auto_now=True)    # Fecha de Actualización

    def __str__(self):
        return f"Settlement {self.id} - {self.status}"
