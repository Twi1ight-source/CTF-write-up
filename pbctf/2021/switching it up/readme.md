Đề cho một file pyc của python 3.10, dùng pycas thấy lạ lạ nên mình install python 3.10 rồi dùng marshal, dis module để decompile bytecode của nó:

![1](https://user-images.githubusercontent.com/84214843/144732775-1c9652ba-757a-47b3-9029-146dcde1c94a.png)

-->bytecode.txt

+Ngồi dịch tay thì nó như sau:

![1](https://user-images.githubusercontent.com/84214843/144732830-8ec9dea7-8106-47fb-9a1b-6ae3a0e65310.png)
![2](https://user-images.githubusercontent.com/84214843/144732832-8d4f1936-8f19-4374-beb9-36f24d4a4e5c.png)

+Cơ bản là check input có bằng 32 ko (ko bao gồm pbctf{})

+Rồi check:

for x in range(len(inp)):
  if b(x*m)[x] ==y -->correct
  
+giờ chỉ việc tìm y thôi

