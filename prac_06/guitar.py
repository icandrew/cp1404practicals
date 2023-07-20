current_year = 2023


class Guitar:
    def __int__(self, name="", year=0, cost=0.00):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}({self.year}) : {self.cost}"

    def get_age(self):
        return current_year - self.year
