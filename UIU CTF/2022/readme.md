# 1.Reject to in inject

**Load file dll**

```c
# include <stdio.h> 
# include <windows.h>

int main() {
	HMODULE lib = LoadLibraryA("IV.dll");
	system("pause");
}
```

# 2. vast_cornfields

**Bài không có gì khó chỉ là luyện tập viết gdb**

```python
import gdb
dict={}
for a in [n for n in range(97,122+1) if n!=113]:
    for b in [n for n in range(97,122+1) if n!=113]:
        gdb.execute("file ./vast_cornfields")
        gdb.execute(f"break *{0x0000555555554000+0x1a54}")
        gdb.execute(f"r <<< $(echo '{chr(a)}{chr(b)}')")

        for i in range(2):
            gdb.execute('n')
        reg=str(gdb.parse_and_eval("$rax"))
        val=gdb.inferiors()[0].read_memory(int(reg,16),2).tobytes()
        dict[val.decode()]=f'{chr(a)}{chr(b)}'
```
