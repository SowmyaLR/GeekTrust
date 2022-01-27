from entities.water_allotment import WaterAllotment
from constants.constants import TWO_BHK, THREE_BHK


class Apartment:
    def __init__(self, type, corp_water, bore_water):
        self.apt_type = type
        self.water = WaterAllotment(corp_water, bore_water)
        self._calculate_owner_consumption()
        self.guest_size = 0

    def _calculate_owner_consumption(self):
        if self.apt_type == TWO_BHK:
            self.water.calculate_2bhk_cost()
        elif self.apt_type == THREE_BHK:
            self.water.calculate_3bhk_cost()

    def add_guests(self, guest_size):
        self.guest_size += guest_size

    def get_bill(self):
        self.water.calculate_tanker_water_consumption(self.guest_size)
        return self.water.get_bill()
