num=int(input())
binary_str=bin(num)[2:]
c=binary_str.count('1')
if c==0:
    print("Invalid input\n")
else:
    print(f"No of one's in the binary string is : {c}")
