** Reject to in inject **

*** Load file dll ***

```c
# include <stdio.h> 
# include <windows.h>

int main() {
	HMODULE lib = LoadLibraryA("IV.dll");
	system("pause");
}
```
