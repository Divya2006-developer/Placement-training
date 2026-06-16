from collections import Counter
import sys

st = sys.stdin.read()
counts = Counter(st)
sorted_freq = sorted(counts.items(), key=lambda x: (-x[1], x[0]))

k = "".join([pair[0] for pair in sorted_freq if pair[0] not in (' ', '\n', '\r', '\t')])

print(k)
