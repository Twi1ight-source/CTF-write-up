
Ta thu được file encryptor.exe

Quan sát hàm main ta thấy được có hàm Gin():

![Ảnh chụp màn hình 2021-10-01 082915](https://user-images.githubusercontent.com/84214843/135551822-3dd7a2fb-243f-4124-9485-3c2ed3f11fb3.png)
+Có vẻ nó khởi chạy thuật toán aes_128_ctr (đây có lẽ là thuật toán mà  chương trình này dùng để encrypt file)

Còn hàm encrypt là inkripshun():

+Mới vô ta thấy get_sha256_sum(), có lẽ là lấy shasum 256 của file cần encrypt

+Tìm shasum 256 của một file pdf thử (dùng lệnh shasum -a 256 file.pdf) thì nó ra tên của file đã encrypt mà đề cho
+

+Ta thấy đề cho 4 file pdf mà chỉ có 3 file encrypted-->có nghĩa file pdf còn thiếu là flag

+mà may là chương trình dùng thuật toán aes_128_ctr cũng dễ, cơ bản là:

file1 ^ key = file1_enc

file2 ^ key = file2_enc

-->flag= flag_enc ^ key

+vì thế chỉ cần tìm được key thì chỉ cần xor với key sẽ có flag, tìm key bằng cách xor file còn lại với enc của nó





