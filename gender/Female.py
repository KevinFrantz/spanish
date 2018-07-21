from .Gender import Gender
class Female(Gender):
    """
        Represents the female gender
    """
    def __init__(self):
        super(Female, self).__init__()
        self.setFemale()
