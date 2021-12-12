Đoạn dịch của file 0a5n.pyc:

![1](https://user-images.githubusercontent.com/84214843/145698554-aa380d2b-986e-4a57-a4e1-1006ae4f7d56.png)

-->Thấy sử dụng các hàm và giá trị của file var.pyc và L.pyc

-->Nhận thấy file var.pyc bị encrypted (var.pyc.encrypted) -->Tiến hành decrypt

+Ở phiên bản pyinstaller này thì nó dùng tinyaes để encrypted, tham khảo (https://github.com/extremecoders-re/pyinstxtractor/wiki/Frequently-Asked-Questions#are-encrypted-pyz-archives-supported)

--> decrypt và sửa header của file lại bằng script sau:

![1](https://user-images.githubusercontent.com/84214843/145698684-d4ac1ae9-1280-4c39-b2a6-46476797de53.png)

+Dùng pycdc để decompile file var.pyc:

    # Source Generated with Decompyle++
    # File: var.pyc (Python 3.5)

    v1 = 0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFAC73L
    v2 = 0x1FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDFFFF58E3L
    v3 = 64
    v4 = 0xF6F8B692899E1B4C5C82580820C2C7CB5597E12EL
    v5 = 0xAFB7BE2AF28B649DAB76337B42EE310119413529L
    g1 = 0x4945E0D8DC57E88D5949F84BF09943F572DBEBB1L
    g2 = 0xB1BF040FE1939C7144341D3AF61F36D63F47E272L
    
+Tiếp đến là file L.pyc

+Ta thấy không dùng pycdc để decompile được, chuyển qua dùng pycas thử nhưng lỗi rất nhiều--> nghi bị thay đổi opcode

+Dịch file opcode.pyc(sau khi decrypt) bằng pycdc rồi so sánh với file opcode.py(sau khi tải python 5 về)

-->Một số opcode bị đổi (có nghĩa là file 0a5n.pyc đã dịch sai một vài chỗ -->sửa lại)

-->Tiến hành đổi lại opcode trong file map của pycdc, nhưng vẫn dịch ko được, đành phải dùng pycas để xem


