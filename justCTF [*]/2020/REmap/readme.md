Khi mở file exe trong IDA và xem string mình phát hiện nó được build bằng thư viện của python (python38.dll)

Dùng script pyinstxtractor.py để extract hết ra

Trong thư mục vừa extrat được có một file thú vị là (backup_decryptor.pyc)

Dùng decompile++ để decompile nó nhưng lại báo lỗi

-->Nhìn lại tên challenge thì là REmap nên đoán có lẽ sẽ RE mapping lại cái gì đó (có lẽ là opcode)

Thế là phải mở file opcode.pyc  (mình extract bằng python 3.9 trên linux nên có phần nó báo lỗi và ko extract hết được) nên phải cài lại python 3.8 trên máy tính và extract lại mới có được 

Tiếp đến là tìm file opcode.py trong lib của python 3.8 vừa cài rồi compile nó thành file pyc để so sánh qua dòng lệnh:
    
     import py_compile
     py_compile.compile('opcode.py')
 
-->Và nó xuất ra file opcode.cpython-38.pyc

-->Search thử trên mạng thì thấy có 1 post khá thú vị: https://medium0.com/tenable-techblog/remapping-python-opcodes-67d79586bfd5

-->Theo đó ta có thể xem opcode của pyc bằng cách dùng 

    import opcode
    opcode.opmap

![1](https://user-images.githubusercontent.com/84214843/142089456-86ba6089-785c-4450-82a6-8ff706766a37.png)

Sau đó ta có thể bỏ file python38.dll vừa extract được của chall rồi thay thế file python38.dll gốc rồi mở python và nhập lại dòng lệnh trên để xem opcode nhưng chả hiểu sao cứ crash

-->Nên đành so sánh header của 2 file opcode.cpython-38.pyc và opcode.pyc để xem opcode nào bị biến đổi 

Khi xem header của file đúng là opcode.cpython-38.pyc thì thấy 

![1](https://user-images.githubusercontent.com/84214843/142089915-d71cfe10-f806-4567-841d-36393c29bb58.png)

-->Có lẽ opcode bytes -> 0xe9 -> giá trị của opcode đó (so sánh với gia trị của opcode khi sử dụng opmap)->0x0,0x0,0x0

Xem đến header của file opcode.pyc:

![1](https://user-images.githubusercontent.com/84214843/142090215-3e51da17-1fe5-4b42-9c7e-bcb797050752.png)

-->Ta thấy giá trị của POP_TOP là 0x40(giá trị sau 0xe9) đúng là khác so với 0x1 (giá trị đúng của nó)

Tới đây thì ta cần mapping lại với mỗi opcode, dùng script sau (mapping.py)



    
 




