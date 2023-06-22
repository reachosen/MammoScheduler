class Scheduler:
    def __init__(self, resource_assumptions):
        """
        Initializes the Scheduler object with the ResourceAssumptions object.

        Args:
        - resource_assumptions (ResourceAssumptions): The ResourceAssumptions object containing the inputted resource assumptions.
        """
        self.resource_assumptions = resource_assumptions

    def compute_diagnostic_appts_needed(self):
        """
        Computes the number of diagnostic appointments needed per day based on the resource assumptions.

        Returns:
        - diagnostic_appts_needed (int): The number of diagnostic appointments needed per day.
        """
        screening_appts = self.resource_assumptions.screening_appts
        diagnostic_appts = self.resource_assumptions.diagnostic_appts
        radiologists = self.resource_assumptions.radiologists
        mammography_machines = self.resource_assumptions.mammography_machines
        screening_time = self.resource_assumptions.screening_time
        diagnostic_time = self.resource_assumptions.diagnostic_time

        total_screening_time = screening_appts * screening_time
        total_diagnostic_time = diagnostic_appts * diagnostic_time
        total_time = total_screening_time + total_diagnostic_time
        work_days_needed = total_time / (radiologists * mammography_machines * 480) # 480 minutes = 8 hours
        diagnostic_appts_needed = total_diagnostic_time / (work_days_needed * 480)

        return int(diagnostic_appts_needed)

    def display_diagnostic_appts_needed(self):
        """
        Displays the computed number of diagnostic appointments needed per day.
        """
        diagnostic_appts_needed = self.compute_diagnostic_appts_needed()
        print(f"Number of diagnostic appointments needed per day: {diagnostic_appts_needed}")
