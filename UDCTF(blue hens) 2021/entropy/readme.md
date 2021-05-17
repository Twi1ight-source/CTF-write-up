Decompiled hàm main bằng IDA:

![113](https://user-images.githubusercontent.com/84214843/118420390-ed030c80-b6e8-11eb-9ee0-265d6b9c4c1e.png)

Nhìn vào ta thấy input được nhập vào dưới dạng char sau đó chuyển qua int là v6[0]

Sau đó v6[0] đi qua hàm sub_6FA và output được so sánh với 0xFD94E6E84A0A

Giờ ta chỉ việc tìm v6[0]

Mình viết một script sử dụng z3 để tìm v6[0]

(Solve.py)

kết quả trả về là: 79427706059334 giờ ta sẽ chuyển qua dạng char

79427706059334 sang hex là 0x483d34347a46, vì là little endian nên ta tách ra là: 0x46, 0x7a, 0x34, 0x34, 0x3d, 0x48
---> Fz44=H

Mở lại chương trình với input là Fz44=H ta được flag

