import re

def solution(files):
    division_files = [re.split(r"([0-9]{1,5})", file) for file in files]
    division_files = sorted(division_files, key = lambda x : (x[0].lower(), int(x[1])))
    ans = ["".join(file) for file in division_files]
    return ans