Bài này dùng vmprotect nên dùng no-vmp để dump mấy cái function bị vmprotect ra thôi. Sau đó dùng vtil để đọc mấy hàm đó đó làm gì

Logic hàm check cũng đơn giản:

![1](https://user-images.githubusercontent.com/84214843/142714552-279e78f5-a7cc-45ba-bab0-6d673b7a7498.png)

Kết quả xuất ra từ hàm đó được so sánh với:

    check=['0x156556d', '0x9a37177f', '0x4baf7822', '0x49c476b8', '0x36515199', '0x1112c4f', '0x11b9e7ac', '0x77697b72', '0x7defa5c', '0x6a5da2f9', '0xefafefc', '0x1f46cec', '0xe5364262', '0x7ca1eb57', '0xbc83bf53', '0xef5e1120']


Trong đó có 2 hàm bị vmprotect: sub_16B0(sub_10E90C) và sub_1990(sub_C249)

nhưng mình chỉ đọc được của sub_C249:

![1](https://user-images.githubusercontent.com/84214843/142714633-5517a1d5-6d36-4dd9-8ab5-60cebc04e744.png)

Biên dịch ra python thì thế này:
    
    def sub_C249(a1,a2):
    t1=~(a1) +a2
    t2=(a1+a2)<<0x8
    t3=t1^t2
    t4=(a1+a2)>>0xf
    t5=t3&t4
    t6=a1-a2
    t7=t6^t2
    t8=~(t4) &0xffffffff
    t9=t7&t8
    t10=t5|t9
    return t10

-->Ngọn hơn nữa thì thế này: (a1-a2) ^ ((a1+a2)<<0x8) ^ ((a1+a2)>>0xf) dựa trên quy tắc: ~a&b | a& ~b = a^b

Còn hàm sub_10E90C thì lại ko dịch được: 

![1](https://user-images.githubusercontent.com/84214843/142714746-d8bf6f1b-ac4b-4bb7-b5b1-a5a8966446a2.png)

-->Cũng may là nó ko phụ thuộc vào input nên mình debug để dump ra giá trị thôi (khá là đau vì nhiều)

Cuối cùng thì quá trình enc --> python thì thế này:



     
