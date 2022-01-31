import unittest
import os

from service.water_management_service import WaterManagement


class TestWaterManagement(unittest.TestCase):
    def test_case1(self):
        file_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
        # print(file_path)
        ws = WaterManagement()
        ws.calculate_bill(f"{file_path}\\water_managment\\tests\\case1")

    def test_case2(self):
        file_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
        ws = WaterManagement()
        fp = f'{file_path}\\water_managment\\tests\\case2'
        ws.calculate_bill(fp)

    def test_case3(self):
        file_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
        ws = WaterManagement()
        ws.calculate_bill(f"{file_path}\\water_managment\\tests\\case3")

    def test_case4(self):
        file_path = "\\".join(os.path.dirname(__file__).split("\\")[:-1])
        ws = WaterManagement()
        ws.calculate_bill(f"{file_path}\\water_managment\\tests\\case4")
