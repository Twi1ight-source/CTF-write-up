Bài này được compile bằng pyinstaller ver 3.9

-->Dùng pyintxtractor để extract nó 

Báo lỗi:

![Screenshot 2021-12-04 23^%11^%12](https://user-images.githubusercontent.com/84214843/144733169-925fc7cd-d8f1-49f4-9f08-d5b4246ad166.png)

-->Có lẽ có vài vấn đề ghi mở file stuff.pye 

-->Mở file pyintxtractor.py để patch lại

![1](https://user-images.githubusercontent.com/84214843/144733383-c420345d-3b71-4764-bc68-74d88dffa12d.png)

-->Thử decompile main.pyc bằng pycdc mà thấy sai sai vì một số yếu tố nêu ra mà ko được sử dụng, thế là mình dùng pycas để disassemble bytecode rồi vừa ngồi dịch vừa đối chiếu với cái ở trên

-->Kết quả là nó dịch thiếu hơi nhiều luôn :( 

-->file main sau khi dịch đầy đủ (main.txt)





