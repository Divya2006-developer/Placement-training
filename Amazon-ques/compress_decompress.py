from collections import Counter
st=input()
counts = Counter(st)
output = "".join(f"{key}{value}" for key, value in counts.items())
print(f"This is the compressed string : {output}")

o="".join(key*value for key,value in counts.items())
print(f"This is the uncompressed string : {o}")
