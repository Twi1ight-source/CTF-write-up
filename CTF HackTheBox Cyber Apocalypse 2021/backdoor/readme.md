Decompiled bằng IDA 

xem strings ta thấy:

![113](https://user-images.githubusercontent.com/84214843/118421825-11acb380-b6ec-11eb-973b-d8ea7a818104.png)

Ta thấy được là chương trình đang chạy file PYC python, vì thế ta sẽ dùng (objcopy) để extract file PYC từ chương trình

( $objcopy --dump-section pydata=pydata.dump bd)

nó sẽ tạo dump file với extract data bên trong, ta sẽ dùng (pyinstxtractor) để extract file dump đó ($python3 pyinstxtractor/pyinstxtractor.py pydata.dump)

bây giờ ta sẽ xem bên trong thư mục pydata.dump_extracted:

![113](https://user-images.githubusercontent.com/84214843/118422261-14f46f00-b6ed-11eb-872f-80420a609fc6.png)

xem thư file bd.pyc bằng cách dùng decompyle3 ($decompyle3  bd.pyc)

![113](https://user-images.githubusercontent.com/84214843/118422417-5edd5500-b6ed-11eb-872a-39e0ca113ca6.png)

ta thấy được string (b's4v3_th3_w0rld') sẽ được chuyển sang md5 (e2162a8692df4e158e6fd33d1467dfe0)  và gửi đến server:

![113](https://user-images.githubusercontent.com/84214843/118422681-e32fd800-b6ed-11eb-9823-39da4f5a558b.png)

Nhưng mà khi ta sử dụng (command: cat flag.txt) nó lại xảy ra lỗi !!

Nhìn code lại lần nữa: Ta thấy đầy tiên nó chỉ recv 32 bytes 





