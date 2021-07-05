+Sau khi mở app lên thì cơ bản là nó check username và password 

+Ko có gì đặc biệt nên mở source lên xem thử:

![1](https://user-images.githubusercontent.com/84214843/124407534-59f06580-dd6e-11eb-9733-0536e68ac3eb.png)

+Tại onClick(), thấy được nó sẽ check pass và username nếu 1 trong 2 ô trống thì báo lỗi, còn nếu sai thì báo lỗi nốt

+Ta quan tâm trường hợp còn lại thấy có 2 chỗ cần quan tâm như đã khoanh đỏ ở trên, kéo xuống xem thử:

+Tại hàm dh7645oi():

![1](https://user-images.githubusercontent.com/84214843/124407861-2104c080-dd6f-11eb-9f67-f671c7c34933.png)

-->Ta thấy rằng nó load cái gì đó từ hàm initFromJNI() sau đó hash nó bằng SHA-256 rồi cuối cùng sử dụng nó như một key cho một thuật toán AES

+Kéo lên xem thử coi hàm  initFromJNI() làm gì:

![1](https://user-images.githubusercontent.com/84214843/124408034-8d7fbf80-dd6f-11eb-949a-3f34f15b2ee0.png)

-->Hóa ra hàm initFromJNI() là một hàm được sử dụng trong libnative của app

+Xem tiếp hàm còn lại là wr9452tb():

![1](https://user-images.githubusercontent.com/84214843/124408224-f6ffce00-dd6f-11eb-8362-5e4d3964efd0.png)

-->Password sau khi được encrypted với key và thuật toán AES (cuối cùng chỉ thấy nó sử dụng key nên mình đoán đó là AES-ECB) sẽ được encode bằng base64 (thông qua hàm fg8461gs() )

-->Cuối cùng nó sẽ mở file "uw7289nv" tại asset lên để so sánh ("uw7289nv" : r6EszdHWf8TkNrC+BLfiXILGelpBPHw7koCOeLpBv8w= )

-->Vậy ta chỉ cần decode base64 cái của "uw7289nv" và decrypt AES-ECB là ra 

-->Việc phải làm bây giờ là tìm key để decrypt AES

+Mở libnative load vào IDA xem thử (ở đây dùng bản x86 vì emulator cũng dùng bản đó), initFromJNI():

![1](https://user-images.githubusercontent.com/84214843/124433971-853e7900-dd9d-11eb-8d33-fb9970c08ccb.png)

![2](https://user-images.githubusercontent.com/84214843/124433985-8a032d00-dd9d-11eb-9f15-06108afd6a1d.png)

+Thì thấy nó thực hiện một loạt phép toán, phân tích tĩnh một hồi nhức đầu quá với lại hàm ko nhận tham số nên mình chỉ cần quan tâm tới giá trị trả về của hàm là được ---> mình quyết định debug bằng gdb để xem giá trị trả về của hàm là gì

+Sau khi set up các kiểu thì mình bắt đầu debug thôi:
![1](https://user-images.githubusercontent.com/84214843/124434707-6391c180-dd9e-11eb-8d91-afcc83ae6e48.png)

![2](https://user-images.githubusercontent.com/84214843/124435597-575a3400-dd9f-11eb-975f-9b9fe2e1d3ca.png)

+Tới đó là đã load được thành công native-library của app

-->Bây giờ là lúc tính toán địa chỉ vì app sử dụng ASLR, như hình trên ta thấy base-address của libnative-lib.so là 0xbe319ff0

-->Bây giờ cần tính toán địa chỉ để đặt breakpoint sao cho đúng, ta thấy instruction ở gần cuối có địa chỉ là 0xF5BC (ta cần đặt breakpoint tại địa chỉ này)

-->Còn địa chỉ của start là ở tab export của IDA là 0xEFF0

-->Địa chỉ cần tính là: 0xbe319ff0 + 0xF5BC - 0xEFF0 = 0xbe31a5bc

+Và wow được rồi:

![1](https://user-images.githubusercontent.com/84214843/124438390-524ab400-dda2-11eb-9015-d775ce15d776.png)

--> Chuỗi cần tìm tại edi("MfVLoHWWiAyeaTl") mình ko biết tại sao lại ở đó vì ban đầu mình nhìn code còn tưởng ở eax hoặc esp cơ, thử một hồi 5 cái từ trên xuống ko có mình tính bỏ rồi may mà thử cho hết 

-->Giờ có hết rồi thì bắt đầu decrypt ra pass thôi 

![2](https://user-images.githubusercontent.com/84214843/124439996-4e1f9600-dda4-11eb-9b3e-382c0a04114a.png)

Vậy pass cần tìm là: Th!$_!$_$uPp0s3d_t0_63_$3cur3

+Nhập vào app với pass như trên và username tùy ý thì được( đúng là app chỉ check pass) 

+Xem tiếp cái hàm ava_io_peykar_watercolor_bj9704hd_extraInfo() còn lại: 

![1](https://user-images.githubusercontent.com/84214843/124440312-b2daf080-dda4-11eb-88e5-9a6d851f6211.png)

Đúng là hàm này in ra username đúng, mình để ý thấy cụm __android_log_print có thể liên quan đến logcat -->nhập password và username bất kì rồi mở logcat (search theo 'username' xem thử) và wao:

![1](https://user-images.githubusercontent.com/84214843/124440906-56c49c00-dda5-11eb-99b6-5bbf84f72c50.png)

+Nhưng mình thắc mắc tìm đúng username hay ko thì cũng pass app được thôi nên ko biết để làm gì, sau khi pass app được thì xuất hiện một trò chơi:

![1](https://user-images.githubusercontent.com/84214843/124441243-b02ccb00-dda5-11eb-91bb-f26223b1403b.png)

+Chơi một hồi mình cũng ko tìm hiểu được qui luật của nó, và mình nhớ khi đọc main source ko có phần nào phụ trách phần trò chơi này, vì thế mình quyết định xem thử các class khác của chương trình thì thấy có hàm solvedPuzzleUI():

![1](https://user-images.githubusercontent.com/84214843/124442496-00f0f380-dda7-11eb-8015-a19525d0461e.png)

-->Đọc hàm thì đúng là phải lấy đúng username mới lấy flag được, đọc mấy cái string bên dưới nữa thì thấy "Failure in sending request", có nghĩa là send request tới chương trình với username và pass sao ?, nhưng ko biết tới địa chỉ nào

-->mở file string lên xem thử thì thấy: hostname">https://water-color.peykar.io vậy chắc là nó rồi 

-->Giờ có đầy đủ rồi thì post request thôi: 

curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"!@W@t3RC^l3r&$3cr3t!U53R#","password":"Th!$_!$_$uPp0s3d_t0_63_$3cur3"}' \
  https://water-color.peykar.io
  
  
Flag: S4CTF{W4t3r_C0l0r_is_Beaut1fu1_But_Danger0u5_B3_C4r3ful!!}






















