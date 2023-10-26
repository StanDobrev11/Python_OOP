class vowels:
    _vowels = {'a', 'o', 'e', 'i', 'u', 'y'}

    def __init__(self, text: str):
        self.text = text
        self.current_idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.current_idx += 1
            current_char = self.text[self.current_idx]
            if current_char.lower() in vowels._vowels:
                return current_char
            else:
                return self.__next__()  # this is done through recursion
        except IndexError:
            raise StopIteration

    # def __next__(self):
    #     try:
    #         self.current_idx += 1
    #         vowels_in_text = self.filter_vowels()
    #         return vowels_in_text[self.current_idx]
    #     except IndexError:
    #         raise StopIteration
    #
    # def filter_vowels(self):
    #     vowels_in_text = []
    #     for i in range(len(self.text)):
    #         current_char = self.text[i]
    #         if current_char.lower() in vowels._vowels:
    #             vowels_in_text.append(current_char)
    #
    #     return vowels_in_text


if __name__ == "__main__":
    my_string = vowels('Abcedifuty0o')
    for char in my_string:
        print(char)
