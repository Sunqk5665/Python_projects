bsys_a,num_a = input().split()
bsys_b,num_b = input().split()
if bsys_a in ("b","B"):
    add_a = int(num_a,2)
if bsys_a in ("o","O"):
    add_a = int(num_a,8)
if bsys_a in ("d","D"):
    add_a = int(num_a)
if bsys_a in ("x","X"):
    add_a = int(num_a,16)
if bsys_b in ("b","B"):
    add_b = int(num_b,2)
if bsys_b in ("o","O"):
    add_b = int(num_b,8)
if bsys_b in ("d","D"):
    add_b = int(num_b)
if bsys_b in ("x","X"):
    add_b = int(num_b,16)
x = add_a + add_b
print(bin(x).replace("0b","")) # bin()返回值为字符转