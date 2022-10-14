class gProductionHeader:
    def __init__(self):
        self.scattering_model_name = ''
        self.anisotropy            = 0
        self.n_events              = 0

    def set_scattering_model_name(self,name):
        self.scattering_model_name = name

    def set_anisotropy(self,g):
        self.anisotropy = g

    def set_n_events(self,n):
        self.n_events = n    
