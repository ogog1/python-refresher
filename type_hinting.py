from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
