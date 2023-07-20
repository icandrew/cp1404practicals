class ProgrammingLanguage:
    def __init__(self, name="", typing="", reflection="Yes", year=0):
        #  set default for reflection to Yes
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        if self.reflection:
            reflection_string = "Yes"
        else:
            reflection_string = "No"
        return f"{self.name}, {self.typing} Typing, Reflection={reflection_string}, First appeared in {self.year}"







