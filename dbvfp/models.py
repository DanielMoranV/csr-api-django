from django.db import models


class Admisiones:
    def __init__(self, numero, fecha_atencion, nombre_paciente, empresa, hora_atencion, medico, tipo_atencion, monto_total, numero_historia):
        self.numero = numero,
        self.fecha_atencion = fecha_atencion,
        self.nombre_paciente = nombre_paciente,
        self.empresa = empresa,
        self.hora_atencion = hora_atencion,
        self.medico = medico,
        self.tipo_atencion = tipo_atencion,
        self.monto_total = monto_total,
        self.numero_historia = numero_historia

        def __repr__(self):
            return f"{self.numero} {self.fecha_atencion} {self.nombre_paciente} {self.empresa} {self.hora_atencion} {self.medico} {self.tipo_atencion} {self.monto_total} {self.numero_historia}"
