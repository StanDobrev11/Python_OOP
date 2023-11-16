class Route:
    def __init__(self, start_point: str, end_point: str, length: float, route_id: int):
        self.start_point = start_point
        self.end_point = end_point
        self.length = length
        self.route_id = route_id  # represents the id of the route.
        self.is_locked = False  # status of the route.

    @property
    def start_point(self):
        return self.__start_point

    @start_point.setter
    def start_point(self, value: str):
        if value.strip() == '':
            raise ValueError("Start point cannot be empty!")
        self.__start_point = value

    @property
    def end_point(self):
        return self.__end_point

    @end_point.setter
    def end_point(self, value: str):
        if value.strip() == '':
            raise ValueError("End point cannot be empty!")
        self.__end_point = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value: float):
        if value < 1:
            raise ValueError("Length cannot be less than 1.00 kilometer!")
        self.__length = value

    @property
    def details(self):
        return self.start_point, self.end_point
