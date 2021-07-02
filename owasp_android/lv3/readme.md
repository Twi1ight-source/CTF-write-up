Chương trình sử dụng native code

Phân tích một hồi thì mình thấy có hai hàm quan trọng là Java_sg_vantagepoint_uncrackable3_CodeCheck_bar() và __fastcall __noreturn start_routine() chứa hàm goodbye() trong đó

Xem hàm thứ hai trước:

![2](https://user-images.githubusercontent.com/84214843/124243272-e2d98800-db47-11eb-851f-b826e2c79127.png)

Ta chú ý 2 hàm strstr() ,nghĩa là nó tìm kiếm chuỗi 'frida' hay 'xposed' xem có xuất hiện trong v3 ko nếu có thì báo lỗi 

-->Mình đoán đây là cái anti debug (anti-frida) của app 

Xem ngược lên trên thì nó nhận v3 với fgets() nên mình sẽ dùng frida để overload fgets() và trả check frida về null để bypass

![1](https://user-images.githubusercontent.com/84214843/124246991-a871ea00-db4b-11eb-948c-66f2897542a9.png)

Sau khi bypass được hết rồi, tiếp đến là hàm Java_sg_vantagepoint_uncrackable3_CodeCheck_bar():

![1](https://user-images.githubusercontent.com/84214843/124247248-e3741d80-db4b-11eb-9422-549cfe368391.png)

+Ở đây chú ý thấy các biểu thức so sánh với xor, mình đoán rằng dest chính là xor_key ban đầu đề cho ('pizzapizzapizzapizzapizz')

+Nhưng 2 cái còn lại v7 và v4 thì ko biết, mình đoán v4 là cái cần tìm còn cái còn lại là v7

+Để ý thấy hàm sub_12C0(v7) lấy tham số là v7 vì thế mình chỉ cần biết tham số đầu vào của hàm đó là biết được v7

--->Sử dụng frida để tìm 

![2](https://user-images.githubusercontent.com/84214843/124251182-d5c09700-db4f-11eb-9640-5b7abe90155c.png)

Và kết quả là: 

![1](https://user-images.githubusercontent.com/84214843/124251294-f557bf80-db4f-11eb-81d6-51af05474b14.png)

Sau khi có được v7 và dest thì xor thôi

![1](https://user-images.githubusercontent.com/84214843/124251413-13bdbb00-db50-11eb-9605-3da566520ab8.png)

Flag: making owasp great again

