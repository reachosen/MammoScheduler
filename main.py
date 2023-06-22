from resource_assumptions import ResourceAssumptions
from scheduler import Scheduler

def main():
    # Initialize resource assumptions
    ra = ResourceAssumptions(total_appointments=100, positive_screens=20, current_diagnostic_capacity=10, current_wait_times=5, resource_availability=3, no_show_rates=0.1, reschedule_rates=0.2)

    # Initialize scheduler
    scheduler = Scheduler(ra)

    # Schedule appointments
    scheduler.schedule_appointments()

    # Compute appointments needed per day
    appointments_needed_per_day = scheduler.compute_appointments_needed()

    # Print results
    print("Resource Assumptions:")
    print(f"Total Appointments: {ra.total_appointments}")
    print(f"Positive Screens: {ra.positive_screens}")
    print(f"Current Diagnostic Capacity: {ra.current_diagnostic_capacity}")
    print(f"Current Wait Times: {ra.current_wait_times}")
    print(f"Resource Availability: {ra.resource_availability}")
    print(f"No-Show Rates: {ra.no_show_rates}")
    print(f"Reschedule Rates: {ra.reschedule_rates}")
    print()
    print(f"Number of Diagnostic Appointments Needed per Day: {appointments_needed_per_day}")

if __name__ == "__main__":
    main()
