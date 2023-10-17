class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(class_instance):
    return class_instance.play()


guitar = Guitar()
print(start_playing(guitar))
print()
