from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int

movie = Movie(name="John Wick", year=2014)
print()
print(movie, "\n")
