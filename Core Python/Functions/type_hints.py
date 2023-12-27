"""
To enable type hinting, go to:
1. ctrl + shift + p
2. settings.json via user preference
3. add "python.analysis.typeCheckingMode": "basic"
"""

def average(a : int, b : int, c : int) -> float:
    return a + b + c  / 3

print(average(1, 5, 7))