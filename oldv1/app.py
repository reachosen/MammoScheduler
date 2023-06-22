from resource_assumptions import ResourceAssumptions
from scheduler import Scheduler

def main():
    screening_appts = int(input("Enter the number of screening appointments per day: "))
    diagnostic_appts = int(input("Enter the number of diagnostic appointments per day: "))
    radiologists = int(input("Enter the number of radiologists available per day: "))
    mammography_machines = int(input("Enter the number of mammography machines available per day: "))
    screening_time = int(input("Enter the average time it takes to perform a screening appointment (in minutes): "))
    diagnostic_time = int(input("Enter the average time it takes to perform a diagnostic appointment (in minutes): "))

    resource_assumptions = ResourceAssumptions(screening_appts, diagnostic_appts, radiologists, mammography_machines, screening_time, diagnostic_time)
    scheduler = Scheduler(resource_assumptions)
    scheduler.display_diagnostic_appts_needed()

if __name__ == "__main__":
    main()
