import sys

from service.water_management_service import WaterManagement


def main():
    input_file = sys.argv[1]
    water_mng = WaterManagement()
    water_mng.calculate_bill(input_file)


if __name__ == '__main__':
    main()

