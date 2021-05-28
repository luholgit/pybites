class RecordScore:
    """Class to track a game's maximum score"""

    def __init__(self):
        self.current_record = None

    def __call__(self, new_score: int) -> int:
        if self.current_record is None or new_score > self.current_record:
            self.current_record = new_score
        return self.current_record
