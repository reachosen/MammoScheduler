class ResourceAssumptions:
    def __init__(self, screening_appts=0, diagnostic_appts=0, radiologists=0, mammography_machines=0, screening_time=0, diagnostic_time=0):
        """
        Initializes the ResourceAssumptions object with the inputted resource assumptions.

        Args:
        - screening_appts (int): The number of screening appointments per day.
        - diagnostic_appts (int): The number of diagnostic appointments per day.
        - radiologists (int): The number of radiologists available per day.
        - mammography_machines (int): The number of mammography machines available per day.
        - screening_time (int): The average time it takes to perform a screening appointment.
        - diagnostic_time (int): The average time it takes to perform a diagnostic appointment.
        """
        self.screening_appts = screening_appts
        self.diagnostic_appts = diagnostic_appts
        self.radiologists = radiologists
        self.mammography_machines = mammography_machines
        self.screening_time = screening_time
        self.diagnostic_time = diagnostic_time
