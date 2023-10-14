class Integer:
    def __init__(self, value: int) -> None:
        self.value = value

    @staticmethod
    def is_roman_numeral(numeral):

        Integer.convert_roman_to_int(numeral)
        return True

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
        numeral = list(numeral)[::-1]
        for idx, current_letter in enumerate(numeral):
            try:
                previous_letter_idx = idx - 1 if idx > 0 else idx
                previous_letter = numeral[previous_letter_idx]
                next_letter = numeral[idx + 1]
                if mapper[current_letter] < mapper[previous_letter]:
                    continue

                if mapper[current_letter] <= mapper[next_letter]:
                    result_value += mapper[current_letter]
                else:
                    result_value += mapper[current_letter] - mapper[next_letter]
            except IndexError:
                if mapper[current_letter] < mapper[numeral[idx - 1]]:
                    pass
                else:
                    result_value += mapper[current_letter]

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


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
