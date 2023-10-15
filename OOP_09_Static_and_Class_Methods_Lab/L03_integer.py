class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def is_roman_numeral(numeral):
        try:
            Integer.convert_roman_to_int(numeral)
            return True
        except KeyError:
            return False

    @staticmethod
    def convert_roman_to_int(numeral):
        # VII = 7 (5 + 2 = 7), LXXX = 80 (50 + 10 + 10 + 10 = 80), MCCC = 1300 (1000+100 + 100 + 100 = 1300)
        # CM = 900 (1000 – 100 = 900), IX = 9 ( 10 – 1 = 9 ), XC = 90 (100 – 10 = 90)
        mapper = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result_value = 0
        for i in range(len(numeral)):
            if i > 0 and mapper[numeral[i]] > mapper[numeral[i - 1]]:
                result_value += mapper[numeral[i]] - 2 * mapper[numeral[i - 1]]
            else:
                result_value += mapper[numeral[i]]
        return result_value

    @classmethod
    def from_float(cls, float_value: float) -> "Integer" or str:
        if isinstance(float_value, float):
            return cls(int(float_value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value: str) -> "Integer" or str:
        if Integer.is_roman_numeral(value):
            return cls(Integer.convert_roman_to_int(value))

    @classmethod
    def from_string(cls, value: str) -> "Integer" or str:
        if isinstance(value, str):
            return cls(int(value))
        else:
            return "wrong type"

# first_num = Integer(10)
# print(first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num.value)
# print(Integer.from_float("2.6"))
# print(Integer.from_string(2.6))
