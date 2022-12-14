class Aircraft:
    def __init__(self, make, code, typ, flight_range):
        self.make = make
        self.code = code
        self.type = typ
        self.flight_range = float(flight_range)

    def get_make(self):
        return self.make

    def get_flight_range(self):
        return self.flight_range

    def __repr__(self):
        return f"Aircraft Make: {self.make} Code: {self.code} Type : {self.type} Range : {self.flight_range} "
