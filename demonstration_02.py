"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes:int) -> int:
    return minutes * 60

def convert_s(seconds:int) -> float:
    return seconds / 60

print("sec", convert(5));
print("sec ",convert(3));
print("sec",convert(2));

print("min", convert_s(300));
