import sys


def read():
    return sys.stdin.readline().strip()


st = str(read())
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    st = st.replace(i, ".")

print(len(st))
