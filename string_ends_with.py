
"""
Complete the solution so that it returns true if the first
argument(string) passed in ends with the 2nd argument (also a string).
"""



def solution(string: str, ending: str) -> bool:
    return string[len(string)-len(ending)::] == ending


"""
Optimal solution
    Теперь буду знать про такую замечательную функцию)

def solution(string, ending):
    return string.endswith(ending)
"""
