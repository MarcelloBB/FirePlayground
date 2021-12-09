import fire

class Str:
    def __init__(self, char="-") -> None:
        self.char = char

    def print(self, size) -> str:
        return self.char * size

if __name__ == "__main__":
    fire.Fire(Str)