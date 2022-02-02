from entities.water_allotment import WaterAllotment
from constants.constants import TWO_BHK, THREE_BHK


class Apartment:
    def __init__(self, type, no_of_persons):
        self.apt_type = type
        self.no_of_persons = no_of_persons
        self.water = None  #
        # self._calculate_owner_consumption()
        self.guest_size = 0
        self.guest_stay_days = 0

    def allot_water(self, corp_water, bore_water):
        self.water = WaterAllotment(corp_water, bore_water)
        self.water.calculate_water_consumption(self.apt_type * 2)

    # def _calculate_owner_consumption(self):
    #     if self.apt_type == TWO_BHK:
    #         self.water.calculate_2bhk_cost()
    #     elif self.apt_type == THREE_BHK:
    #         self.water.calculate_3bhk_cost()

    def add_guests(self, guest_size, no_of_days):
        self.guest_size += guest_size
        self.guest_stay_days += no_of_days

    def get_bill(self):
        available_accomodation = self.apt_type * 2 - self.no_of_persons
        self.water.calculate_tanker_water_consumption(self.guest_size, self.guest_stay_days,
                                                      0 if available_accomodation <= 0 else available_accomodation)
        return self.water.get_bill()
