from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str,
                                  name: str,
                                  capacity_consumption: int,
                                  memory_consumption: int):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str,
                                name: str,
                                capacity_consumption: int,
                                memory_consumption: int):

        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
        except IndexError:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [x for x in System._hardware if x.name == hardware_name][0]
            software = [x for x in System._software if x.name == software_name][0]
        except IndexError:
            return "Some of the components do not exist"

        if hardware.software_installed(software):
            hardware.uninstall(software)
            System._software.remove(software)

    @staticmethod
    def analyze():
        software_mem = sum(software.memory_consumption for software in System._software)
        hardware_mem = sum(hardware.memory for hardware in System._hardware)
        software_capacity = sum(software.capacity_consumption for software in System._software)
        hardware_capacity = sum(hardware.capacity for hardware in System._hardware)

        text = (f"System Analysis\n"
                f"Hardware Components: {len(System._hardware)}\n"
                f"Software Components: {len(System._software)}\n"
                f"Total Operational Memory: {software_mem} / {hardware_mem}\n"
                f"Total Capacity Taken: {software_capacity} / {hardware_capacity}")
        return text

    @staticmethod
    def system_split():
        result_text = ''
        for hardware in System._hardware:
            text = (
                f"Hardware Component ‐ {hardware.name}\n"
                f"Express Software Components: {len([x for x in hardware.software_components if x.software_type == 'Express'])}\n"
                f"Light Software Components: {len([x for x in hardware.software_components if x.software_type == 'Light'])}\n"
                f"Memory Usage: {sum(soft.memory_consumption for soft in hardware.software_components)} / {hardware.memory}\n"
                f"Capacity Usage: {sum(soft.capacity_consumption for soft in hardware.software_components)} / {hardware.capacity}\n"
                f"Type: {hardware.hardware_type}\n"
                f"Software Components: {', '.join(x.name for x in hardware.software_components) if hardware.software_components else None}\n"
            )
            result_text += text

        return result_text.strip()
