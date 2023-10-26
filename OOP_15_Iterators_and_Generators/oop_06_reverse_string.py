def reverse_text(text: str):
    current_idx = len(text) - 1
    while current_idx >= 0:
        yield text[current_idx]
        current_idx -= 1


if __name__ == '__main__':
    for char in reverse_text("step"):
        print(char, end='')
