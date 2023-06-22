from dataclasses import dataclass

@dataclass
class ResourceAssumptions:
    total_appointments: int = 0
    positive_screens: int = 0
    current_diagnostic_capacity: int = 0
    current_wait_times: int = 0
    resource_availability: int = 0
    no_show_rates: float = 0.0
    reschedule_rates: float = 0.0

    def set_total_appointments(self, num_appointments):
        self.total_appointments = num_appointments

    def set_positive_screens(self, num_screens):
        self.positive_screens = num_screens

    def set_current_diagnostic_capacity(self, num_capacity):
        self.current_diagnostic_capacity = num_capacity

    def set_current_wait_times(self, wait_times):
        self.current_wait_times = wait_times

    def set_resource_availability(self, avail):
        self.resource_availability = avail

    def set_no_show_rates(self, no_show):
        self.no_show_rates = no_show

    def set_reschedule_rates(self, reschedule):
        self.reschedule_rates = reschedule
