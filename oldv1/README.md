Based on the given specification, here are the core classes, functions, and methods that will be necessary:

Core Classes:
- ResourceAssumptions: This class will hold the resource assumptions inputted by the user.
- Scheduler: This class will compute the number of diagnostic appointments needed per day based on the resource assumptions.

Core Functions/Methods:
- ResourceAssumptions.__init__(self, screening_appts, diagnostic_appts, radiologists, mammography_machines, screening_time, diagnostic_time): This method will initialize the ResourceAssumptions object with the inputted resource assumptions.
- Scheduler.__init__(self, resource_assumptions): This method will initialize the Scheduler object with the ResourceAssumptions object.
- Scheduler.compute_diagnostic_appts_needed(self): This method will compute the number of diagnostic appointments needed per day based on the resource assumptions.
- Scheduler.display_diagnostic_appts_needed(self): This method will display the computed number of diagnostic appointments needed per day.

Based on these classes and methods, we will need to create two Python files: `resource_assumptions.py` and `scheduler.py`.

`resource_assumptions.py`
