const = 0xc6a4a7935bd1e995
def encode(a):  
  b = 1
  c = 0x1337  

  temp = c ^ (b * const)

  j = b
  

  
  if b & 0x7 == 1:
    temp = ((temp ^ a[0]) * const) & 0xFFFFFFFFFFFFFFFF

  uVar2 = ((temp ^ (temp >> 0x2f)) * const) & 0xFFFFFFFFFFFFFFFF
  return (uVar2 ^ (uVar2 >> 0x2f)) & 0xFFFFFFFFFFFFFFFF


import string

flag = [
0x188CF31A079D66FC,
0xA12C8AF2572DFA48,
0x1FF01EBC0C7408CB,
0xD58E3BA2FBEF9D8C,
0x5674B7653639CB87,
0x3EB8B6A6F0753E49,
0x1FF01EBC0C7408CB,
0xF9DFA617052DFD5E,
0x34514C558BA5E73B,
0xF9DFA617052DFD5E,
0x3A9C8840CEBAEA9E,
0xB13E0ECBEBA2478F,
0x827AEE59DF4BCCE8,
0x3A9C8840CEBAEA9E,
0xB13E0ECBEBA2478F,
0x827AEE59DF4BCCE8,
0x7641DBD6CD9D79AF,
0x7641DBD6CD9D79AF,
0x7641DBD6CD9D79AF]

res = []
for out in flag:
  for c in string.printable:
    v = encode([ord(c)])
    if v == out:
      res.append(c)
      break
print(''.join(res))