from project.software.software import Software


class Hardware:
    name: str
    hardware_type: str
    capacity: int
    memory: int

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: list = []

    def install(self, software: Software):
        if self.memory < software.memory_consumption or \
                self.capacity < software.capacity_consumption:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if self.software_installed(software):
            self.software_components.remove(software)

    def software_installed(self, software) -> bool:
        if software in self.software_components:
            return True
        return False
