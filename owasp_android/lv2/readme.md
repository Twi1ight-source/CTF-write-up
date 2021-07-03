3 cách : phân tích tĩnh và frida (dùng frida để hook hàm strncmp trong native library để xem input của mình được so sánh với cái gì ) và debug bằng gdb

* PP gdb:

+Đầu tiên khi mở app lên ta thấy được app check root nếu nhấn OK thì sẽ out chương trình

+Mở sources lên xem thử thì ta thấy: 

![1](https://user-images.githubusercontent.com/84214843/124350259-d0318280-dc1d-11eb-8492-80a734099017.png)

![2](https://user-images.githubusercontent.com/84214843/124350264-d4f63680-dc1d-11eb-823e-f8cb8ff0fb58.png)

-->Lúc mới mở app (onCreate() ), app check root và check xem có bị debug ko và thực hiện out app tại hàm a (nếu nhấn OK), vì thế ta chỉ cần patch lại hàm a tức là nếu nhấn OK cũng sẽ ko out app nên dù có bị root detected cũng ko hề gì.

+Vì thế ta sẽ mở code smali của MainActivity để patch , kiếm hàm a() và sau đó xóa hàm các instructions trong hàm là xong

![1](https://user-images.githubusercontent.com/84214843/124350439-fdcafb80-dc1e-11eb-8f80-baf5714aa336.png)

+Xóa hết chỉ chừa:

![1](https://user-images.githubusercontent.com/84214843/124350474-1d622400-dc1f-11eb-9e6b-f4358de88d50.png)

+Sau đó save lại và dùng apktool để batch lại, tiếp đó sign apk vừa tạo ra và cài lại vào app thôi 

![1](https://user-images.githubusercontent.com/84214843/124350574-95304e80-dc1f-11eb-96e9-b15b1c9f4488.png)

-->Ko còn out app nữa :))

Tiếp đến là xem native library mà app load vì check input sẽ diễn ra ở đó:

+Ta thấy một hàm quan trọng là Java_sg_vantagepoint_uncrackable2_CodeCheck_bar():

![1](https://user-images.githubusercontent.com/84214843/124350638-ed675080-dc1f-11eb-99f7-70ff671bfbe6.png)

-->Dễ dàng thấy "thanks for the fish" là input cần tìm rồi nhưng mình muốn debug bằng gdb để sau này áp dụng vào những bài khó hơn

-->Ta thấy được nó check độ dài input là 23 và dùng hàm strncmp để so sánh input mình nhập với chuỗi trên 

-->Theo đó mình sẽ đặt breakpoint tại hàm strncmp để xem cái mà input cần so sánh 

+Xem lại phía trên thì mình chợt thấy ptrace() (một kĩ thuật anti-debug) --> vậy muốn debug phải nop mấy cái này đã 

+ptrace được gọi 2 lần -->nop bằng cách patch 4 byte đầu bằng (1F 20 03 D5)

![1](https://user-images.githubusercontent.com/84214843/124350840-1dfbba00-dc21-11eb-9bff-08be91d6f89c.png)

+Giờ thì debug được rồi

+Cách attach gdb vô android: https://simoneaonzo.it/gdb-android/?fbclid=IwAR0DiiVPLZ8lvJJM4onGMeiVv6tIgUBbadhBFgyCgguLuWVZ55c8myJU0qM











