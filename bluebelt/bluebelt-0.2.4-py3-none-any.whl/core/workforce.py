# 

class WorkforceGroup:
    # e.g.
    # Full-Time Employees.
    # Part-Time Employees.
    # Seasonal Employees.
    # Temporary Employees.
    
    def __init__(self, name, count, hours, hours_min, hours_max, period, **kwargs):

        self.name = name
        self.count = count
        self.hours = hours
        self.hours_min = hours_min
        self.hours_max = hours_max
        self.period = period

    def __repr__(self):
        return f'{self.__class__.__name__}(name={self.name}, count={self.count}, hours={self.hours}, hours_min={self.hours_min}, hours_max={self.hours_max}, period={self.period})'
        

class Workforce:
    def __init__(self, types, **kwargs):

        self.types = types