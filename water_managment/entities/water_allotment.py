from constants.constants import INITIAL_AMNT, CORP_WATER, TWO_BHK_WATER_CONS, BORE_WATER, THREE_BHK_WATER_CONS, \
    WATER_ALLOTED_FOR_INDIVIDUAL, TOTAL_DAYS, SLAB1_COST, SLAB2_COST, SLAB3_COST, \
    SLAB1_UPPER, SLAB2_UPPER, SLAB3_UPPER, SLAB2_LOWER, SLAB3_LOWER, SLAB4_LOWER, SLAB4_COST
import math

class WaterAllotment:
    def __init__(self, corp_water, bore_water):
        self.corp = corp_water
        self.bore = bore_water
        self.total_cost = INITIAL_AMNT
        self.total_water = INITIAL_AMNT

    def calculate_2bhk_cost(self):
        self.total_cost += math.ceil(TWO_BHK_WATER_CONS * self.corp * CORP_WATER) / (self.corp + self.bore) + \
                           math.ceil(TWO_BHK_WATER_CONS * self.bore * BORE_WATER) / (self.corp + self.bore)
        self.total_water += TWO_BHK_WATER_CONS

    def calculate_3bhk_cost(self):
        self.total_cost += math.ceil((THREE_BHK_WATER_CONS * self.corp * CORP_WATER) / (self.corp + self.bore)) + \
                           math.ceil((THREE_BHK_WATER_CONS * self.bore * BORE_WATER) / (self.corp + self.bore))
        self.total_water += THREE_BHK_WATER_CONS

    def _is_slab1(self, water_req):
        return INITIAL_AMNT < water_req <= SLAB1_UPPER

    def _get_slab1_cost(self, water_req):
        return water_req * SLAB1_COST

    def _is_slab2(self, water_req):
        return SLAB2_LOWER <= water_req <= SLAB2_UPPER

    def _get_slab2_cost(self, water_req):
        return SLAB1_UPPER * SLAB1_COST + (abs(water_req - SLAB1_UPPER) * SLAB2_COST)

    def _is_slab3(self, water_req):
        return SLAB3_LOWER <= water_req <= SLAB3_UPPER

    def _get_slab3_cost(self, water_req):
        return SLAB1_UPPER * SLAB1_COST + ((SLAB2_UPPER - SLAB1_UPPER) * SLAB2_COST) + (
                abs(SLAB2_UPPER - water_req) * SLAB3_COST)

    def _is_slab4(self, water_req):
        return water_req >= SLAB4_LOWER

    def _get_slab4_cost(self, water_req):
        return SLAB1_UPPER * SLAB1_COST + ((SLAB2_UPPER - SLAB1_UPPER) * SLAB2_COST) + \
               ((SLAB3_UPPER - SLAB2_UPPER) * SLAB3_COST) + (abs(water_req - SLAB3_UPPER) * SLAB4_COST)

    def calculate_tanker_water_consumption(self, guest_size):
        total_water_req = guest_size * WATER_ALLOTED_FOR_INDIVIDUAL * TOTAL_DAYS
        self.total_water += total_water_req
        if self._is_slab1(total_water_req):
            self.total_cost += self._get_slab1_cost(total_water_req)
        elif self._is_slab2(total_water_req):
            self.total_cost += self._get_slab2_cost(total_water_req)
        elif self._is_slab3(total_water_req):
            self.total_cost += self._get_slab3_cost(total_water_req)
        elif self._is_slab4(total_water_req):
            self.total_cost += self._get_slab4_cost(total_water_req)

    def get_bill(self):
        return self.total_water, int(self.total_cost)
