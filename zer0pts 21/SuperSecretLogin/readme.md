Bỏ vào IDA xem thử, xem strings thấy câu "This is a third-party compiled AutoIt script"

Vì thế mình bỏ vào AutoIt Extractor(https://gitlab.com/x0r19x91/autoit-extractor) để xem thử:

![1](https://user-images.githubusercontent.com/84214843/128449226-03a095d6-1acc-4bc0-a35b-098eed9a7292.png)

+Save cái Autoit script ra một file, cuối từ từ đến cuối xem thử thì thấy có phần quan trọng:

![1](https://user-images.githubusercontent.com/84214843/128449837-81225d00-50fd-4a06-ad2f-b29cd6330384.png)
![2](https://user-images.githubusercontent.com/84214843/128449843-de307c1f-2dc3-4cf6-b37c-b2aeb9a40dad.png)

Tại Func ONCLICK():

+input được lưu ở text, sau đó input cùng với mserverkey đi qua hàm FUCKIT() và kết quả được lưu ở $fuck

+Cuối cùng so sánh $fuck với $fuckpython = "7188bb1563e5702342e22a856ad3df1cfa9729b4115d8cfb1f07a0c6fc916477f02f77d656834379b32e"

+Nếu bằng thì "Good Job!", ko thì ":(", "You have a long way to go buddy!"

Phân tích hàm FUCKIT():

+Nó chạy một chuỗi opcode mà mình đoán là shellcode, vì thế mình dùng 1 script sử dụng unicorn để phân tích nó cho tiện

![1](https://user-images.githubusercontent.com/84214843/128450289-b84f5430-e274-48cd-9f30-3837725cf4de.png)

Và đây là kết quả:

(out.txt)

+Phân tích một lúc thì hàm FUCKIT() khởi chạy RC4 cipher -->Để tìm input thì dùng cyberchef để devrypt RC4 thôi:

![1](https://user-images.githubusercontent.com/84214843/128450577-62e65614-b300-4c07-97dc-8b86e3e877c3.png)

+Nhưng khi nhập vào app lại ko đúng (đọc writeup thấy sử dụng cheat engine gì đó mà làm biếng quá nên kệ luôn)



