class Software:
    name: str = ""
    software_type: str = ""
    capacity_consumption: int = 0
    memory_consumption: int = 0

    def __init__(self, name: str, software_type: str, capacity_consumption: int, memory_consumption: int):
        self.name = name
        self.software_type = software_type
        self.capacity_consumption = capacity_consumption
        self.memory_consumption = memory_consumption
