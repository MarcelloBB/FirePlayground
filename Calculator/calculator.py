import fire

class Calculator:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def sum(self) -> float:
        return self.a + self.b

    def minus(self) -> float:
        return self.a - self.b

    def times(self) -> float:
        return self.a * self.b

    def div(self) -> float:
        return self.a / self.b

    def intdiv(self) -> int:
        return self.a // self.b

    def pow(self) -> float:
        return self.a ** self.b


if __name__ == "__main__":
    fire.Fire(Calculator)