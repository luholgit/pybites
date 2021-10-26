from dataclasses import dataclass, field


@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: str = field(default="Beginner")

    def __post_init__(self):
        self.title = self.title.capitalize()
