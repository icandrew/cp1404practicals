class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __repr__(self):
        return (f"{self.name}, start:{self.start_date}, priority={self.priority}, estimate={self.cost_estimate}, "
                f"completion={self.completion}")

