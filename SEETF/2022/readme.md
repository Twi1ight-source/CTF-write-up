# Susware
Đây là một bài pe sử dụng một số kĩ thuật dùng trong malware

-Pe sử dụng một kĩ thuật process injection là [TLS callback](https://attack.mitre.org/techniques/T1055/005/)

> TLS callback vốn được dùng bởi os để setup/clean up các data của thread nhưng nó có thể tạo ra các memory space, hacker lợi dụng điều này để chèn mã độc vào các vùng nhớ và thực thi vùng nhớ đó một cách riêng biệt trước khi chuyển tới hàm main.

-Xem tab `export` trong IDA ta thấy nó sử dụng tổng cộng 4 `TLS callback`:

![1](https://user-images.githubusercontent.com/84214843/178108522-992c3925-c06b-45af-be25-02f4bbe13624.PNG)

-Sử dụng 1 `IDA plugin` là [findcrypt-yara](https://github.com/polymorf/findcrypt-yara) (sử dụng phím tắt `ctrl+alt+f`) xem thì thấy chương trình sử dụng thuật toán AES:

![1](https://user-images.githubusercontent.com/84214843/178108647-91663d7b-0c2e-4e62-85fd-9af16dce2720.PNG)

-Trace từ chỗ nó gọi lên thì nó sử dụng ở TLS_callback4:

![1](https://user-images.githubusercontent.com/84214843/178108816-274d040b-30e2-4dfc-9b6f-0bf9a3054572.PNG)

* Sử dụng BIN/139 trong resource 

![2](https://user-images.githubusercontent.com/84214843/178108886-86bd27fd-6f6d-42f3-8a41-738316f7900b.PNG)

* Tiến hành AES_decrypt vói key và iv được tính toán ở trên

![3](https://user-images.githubusercontent.com/84214843/178108917-c86c1768-9a86-489c-80e5-10f7f8154ec9.PNG)

* Sau đó lưu và đường dẫn như trên 

* Tới đây thì có 2 cách: một là debug tới chỗ nó write process để lấy file dump, hai là dùng `cff explorer` để dump section 139 ra rồi decrypt bằng `cyberchef`.

-Sau khi dump ra được file exe thì nó bị unpack (dùng `die` xem phần `entrpy` thì thấy nó packed nhưng nó ko nhận dạng được packer nào), mở lên IDA xem thử thì thấy có các lệnh như `pushad` và `popad` nên khá chắc là `UPX` nhưng có lẽ đã bị thay đổi để tool không nhận diện được

-Tới đây chỉ có thể unpack bằng tay: đặt bp tại `popad` rồi step đến khi gặp lên `jump` đó là `OEP` rồi dump hết memory segments ra

