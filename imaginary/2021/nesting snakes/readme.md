Bài này được compile bằng pyinstaller ver 3.9

-->Dùng pyintxtractor để extract nó 

Báo lỗi:

![Screenshot 2021-12-04 23^%11^%12](https://user-images.githubusercontent.com/84214843/144733169-925fc7cd-d8f1-49f4-9f08-d5b4246ad166.png)

-->Có lẽ có vài vấn đề ghi mở file stuff.pye 

-->Mở file pyintxtractor.py để patch lại

![1](https://user-images.githubusercontent.com/84214843/144733383-c420345d-3b71-4764-bc68-74d88dffa12d.png)

+Decompile main.pyc:

![1](https://user-images.githubusercontent.com/84214843/144733787-d4f7991e-276a-4661-b59d-8a772b63004e.png)

-->Ta thấy chương trình import stuff, tìm file thì thấy file stuff.pye(chưa gặp bao giờ), search gg file .pye thì thấy đó là file được encrypt bằng module pyconcrete ở python, khi chương trình chạy thì nó sẽ tự decrypt thành file pyc lại.

-->decrypt file stuff.pye thủ công bằng script sau:

![1](https://user-images.githubusercontent.com/84214843/144733944-92d96732-649e-4871-b0a0-b0497bd4b74a.png)

-->Thử decompile stuff.pyc bằng pycdc mà thấy sai sai vì một số yếu tố nêu ra mà ko được sử dụng, thế là mình dùng pycas để disassemble bytecode rồi vừa ngồi dịch vừa đối chiếu với cái ở trên

-->Kết quả là nó dịch thiếu hơi nhiều luôn :( 

+Sau khi dịch ra đầy đủ, mình gộp hàm stuff với hàm main lúc nãy luôn --> (main.txt)

+Có vể lấy input ở f rồi đem vô enc() rồi kết quả là ra mảng arr

+Nhận thấy enc() chỉ lấy sum của input rồi qua một loạt biến đổi để tạo ra mảng arr-->bruce-force sum để lấy mảng arr(tránh các trường hợp return False) --> (bruce flag-sum.txt)




