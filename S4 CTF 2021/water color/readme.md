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

+Mở 









