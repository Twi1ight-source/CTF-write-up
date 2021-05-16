Đây là một bài Webassembly
![site](https://user-images.githubusercontent.com/84214843/118392020-7ff86400-b661-11eb-9b22-d6afef2adac2.png)

Js source code:

![113](https://user-images.githubusercontent.com/84214843/118392058-b2a25c80-b661-11eb-9ea6-3f5f3ef8a8d4.png)

Mình dump file wasm về dùng: wget http://challenges.ctfd.io:30039 -q -O watman.wasm
Sau đó dùng wasm2c để lấy header và souces C file(wasm2c watman.wasm -o wasm.c)
tiếp đến compiled thành C binary để dễ phân tích hơn: (gcc -O3 source.c wasm-rt-impl.c)

Decompiled in IDA:

![113](https://user-images.githubusercontent.com/84214843/118392232-be425300-b662-11eb-8fc9-41bdb9d06b85.png)

Tóm tắt lại bằng code python thì sẽ như thế này:

![113](https://user-images.githubusercontent.com/84214843/118392273-fd70a400-b662-11eb-9d2d-96da25965dc2.png)

Sau đó mình chỉ việc viết hàm để brute-force thôi:)) 

(sol.py)



