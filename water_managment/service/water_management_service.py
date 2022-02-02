from entities.apartment import Apartment
from constants.constants import ALLOT_WATER, ADD_GUESTS


class WaterManagement:
    def __init__(self):
        self.apt = None

    def _apartment(self, line):
        commands = line.split(" ")
        apt_type = int(commands[1])
        no_of_persons = int(commands[2])
        if apt_type*2 >= no_of_persons:
            self.apt = Apartment(apt_type, no_of_persons)

    def _allot_water(self, line):
        commands = line.split(" ")
        # apt_type = int(commands[1])
        water = commands[1].split(":")
        self.apt.allot_water(int(water[0]), int(water[1]))

    def _add_guests(self, line):
        commands = line.split(" ")
        self.apt.add_guests(int(commands[1]), int(commands[2]))

    def _bill(self, line):
        total_water, total_cost = self.apt.get_bill()
        print(total_water, total_cost, sep=" ")

    def execute_command(self, line):
        commands = line.split(" ")
        getattr(self, "_%s" % commands[0].lower())(line)

    def calculate_bill(self, file_path):
        with open(file_path, "r") as fp:
            content = fp.read()
        lines = content.split("\n")
        for lin in lines:
            self.execute_command(lin)
