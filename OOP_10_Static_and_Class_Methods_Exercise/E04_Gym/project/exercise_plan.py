class ExercisePlan:
    id = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        next_id = ExercisePlan.id
        ExercisePlan.id += 1
        return next_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> "ExercisePlan":
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    def __repr__(self) -> str:
        return f"Plan <{self.equipment_id}> with duration {self.duration} minutes"
