from datetime import datetime, timedelta
from random import random
from diagnostic_appointment import DiagnosticAppointment

class Scheduler:
    def __init__(self, resource_assumptions):
        self.resource_assumptions = resource_assumptions
        self.appointments = []

    def schedule_appointments(self):
        num_appointments = self.resource_assumptions.total_appointments
        num_screens = self.resource_assumptions.positive_screens
        current_capacity = self.resource_assumptions.current_diagnostic_capacity
        current_wait_times = self.resource_assumptions.current_wait_times
        resource_availability = self.resource_assumptions.resource_availability
        no_show_rates = self.resource_assumptions.no_show_rates
        reschedule_rates = self.resource_assumptions.reschedule_rates

        # Calculate the number of appointments that can be scheduled per day
        appointments_per_day = current_capacity * resource_availability

        # Calculate the number of days needed to schedule all appointments
        days_needed = num_appointments / appointments_per_day

        # Calculate the number of days needed to schedule all positive screens
        days_needed_screens = num_screens / appointments_per_day

        # Schedule appointments for positive screens first
        for i in range(int(days_needed_screens)):
            for j in range(int(appointments_per_day)):
                if len(self.appointments) >= num_screens:
                    break
                appointment_date = datetime.now() + timedelta(days=i, minutes=j*60/resource_availability)
                appointment = DiagnosticAppointment(f"Patient {len(self.appointments)+1}", f"ID{len(self.appointments)+1}", appointment_date)
                self.appointments.append(appointment)

        # Schedule remaining appointments
        for i in range(int(days_needed)):
            for j in range(int(appointments_per_day)):
                if len(self.appointments) >= num_appointments:
                    break
                appointment_date = datetime.now() + timedelta(days=i+int(days_needed_screens), minutes=j*60/resource_availability)
                appointment = DiagnosticAppointment(f"Patient {len(self.appointments)+1}", f"ID{len(self.appointments)+1}", appointment_date)
                # Check for no-shows and reschedules
                if random() < no_show_rates:
                    continue
                if random() < reschedule_rates:
                    appointment_date += timedelta(days=1)
                self.appointments.append(appointment)

    def compute_appointments_needed(self):
        num_appointments = self.resource_assumptions.total_appointments
        num_screens = self.resource_assumptions.positive_screens
        current_capacity = self.resource_assumptions.current_diagnostic_capacity
        current_wait_times = self.resource_assumptions.current_wait_times
        resource_availability = self.resource_assumptions.resource_availability
        no_show_rates = self.resource_assumptions.no_show_rates
        reschedule_rates = self.resource_assumptions.reschedule_rates

        # Calculate the number of appointments that can be scheduled per day
        appointments_per_day = current_capacity * resource_availability
        print(" appointments_per_day = current_capacity * resource_availability")
        print(f" appointments_per_day = {appointments_per_day} = {current_capacity} * {resource_availability}")
        print("----------------------------------------")
        # Calculate the number of days needed to schedule all appointments
        days_needed = num_appointments / appointments_per_day
        print(" days_needed = num_appointments / appointments_per_day")
        print(f" days_needed = {days_needed} = {num_appointments} / {appointments_per_day}")
        print("----------------------------------------")
    
        # Calculate the number of days needed to schedule all positive screens
        days_needed_screens = num_screens / appointments_per_day
        print(" days_needed_screens = num_screens / appointments_per_day")
        print(f" days_needed_screens = {days_needed_screens} = {num_screens} / {appointments_per_day}")
        print("----------------------------------------")
              

        # Calculate the total number of appointments needed
        appointments_needed = num_screens + (num_appointments - num_screens) * (1 - no_show_rates) * (1 + reschedule_rates) + current_wait_times * appointments_per_day
        print(" appointments_needed = num_screens + (num_appointments - num_screens) * (1 - no_show_rates) * (1 + reschedule_rates) + current_wait_times * appointments_per_day")
        print(f" appointments_needed = {appointments_needed} = {num_screens} + ({num_appointments} - {num_screens}) * (1 - {no_show_rates}) * (1 + {reschedule_rates}) + {current_wait_times} * {appointments_per_day}")
        print("----------------------------------------")
    

        # Calculate the number of appointments needed per day
        appointments_needed_per_day = appointments_needed / (7 - current_wait_times)
        print(" appointments_needed_per_day = appointments_needed / (7 - current_wait_times)")
        print(f" appointments_needed_per_day = {appointments_needed_per_day} = {appointments_needed} / (7 - {current_wait_times})")
        print("----------------------------------------")
        

        return round(appointments_needed_per_day)
