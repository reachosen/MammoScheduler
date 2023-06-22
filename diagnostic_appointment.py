from datetime import datetime

class DiagnosticAppointment:
    def __init__(self, patient_name, patient_id, appointment_date):
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.appointment_date = appointment_date

    def __str__(self):
        return f"Patient Name: {self.patient_name}, Patient ID: {self.patient_id}, Appointment Date: {self.appointment_date.strftime('%m/%d/%Y %I:%M %p')}"
