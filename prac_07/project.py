class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self):
        return (f"{self.name} ({self.start_date}) - priority: {self.priority}, "
                f"cost: {self.cost_estimate}, completion: {self.completion}%")

    def is_completed(self):
        return self.completion == 100