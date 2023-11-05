from project.software.software import Software


class Hardware:
    name: str
    hardware_type: str
    capacity: int
    memory: int
    software_components: list = []

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory

    def install(self, software: Software):
        if self.memory < software.memory_consumption or \
                self.capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
