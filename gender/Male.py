from .Gender import Gender
class Male(Gender):
    """
        Represents the male gender
    """
    def __init__(self):
        super(Male, self).__init__()
        self.setMale()
