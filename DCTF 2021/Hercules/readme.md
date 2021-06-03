Thử chạy thông qua netcat :

![1](https://user-images.githubusercontent.com/84214843/120599004-266da300-c471-11eb-8608-ee21af9806bb.png)

Ta thấy được flag đã bị encrypted và 1 dãy gồm 3 số

Thử thêm 1 vài lần nữa thì nó xuất ra những encrypted flag và bộ 3 số khác nhau

Load binary vào IDA xem thử:

Main:

![1](https://user-images.githubusercontent.com/84214843/120601236-e2c86880-c473-11eb-9f49-59d464ce9158.png)

Ở đây ta chỉ thấy có một hàm duy nhất là sub_E0C() với 2 tham số đầu vào 25 và một chuỗi dctf{semper_sursum_:)} :

![1](https://user-images.githubusercontent.com/84214843/120601606-5e2a1a00-c474-11eb-9072-8e56fe89495a.png)
![1](https://user-images.githubusercontent.com/84214843/120601703-7d28ac00-c474-11eb-9303-cb7f498024a5.png)

Sau một hồi phân tích mấy cái hàm trong đó thì chương trình hoạt động đại khái như sau:

->v9 được lưu dưới một mảng gồm 9 kí tự rồi sau đó đi qua 3 hàm sub_C22(), sub_CE5(), sub_AFB() tùy thuộc vào v5=rand()%3

->v9 sau khi đi qua các hàm đó được xử lí như một ma trận 3x3 là:
      (1,2,2)
      (2,1,2)
      (2,2,3)
   
   với:
      
 +sub_C22() ko làm gì cả
 
 +sub_CE5() chuyển cột thứ nhất của ma trận sang âm
 
 +sub_ÀB() chuyển cột thứ hai của ma trận sang âm
 
Sau đó hàm sub_A41() thực hiện nhân 2 ma trận là v9 sau khi được biến đổi thành 1 trong 3 cái ở trên với v6 là ma trận 3x1:

   (3)
   (4)
   (5)
 
kết quả sau khi nhân 2 ma trận được lưu vào v6(là một mảng gồm 3 số), sau đó hàm sub_8EA() mảng đó để encrypt flag

Quá trình đó lặp lại 25 lần và đó là là kết quả nhận được cuối cùng sau khi ta net cat gồm encrypt flag và một mảng gồm 3 số

--> Vậy mục tiêu của chúng ta là từ kết quả cuối cùng đó sau cho quay lại ban đầu( tức là quay lại flag và mảng ban đầu là (3,4,5))

môt phép nhân 2 ma trận ví dụ: A x B =C, với C là kết quả và A là một trong 3 ma trận sau khi đổi ở trên. Suy ra tìm mản trước= C x A^(-1)

Kết quả 3 ma trận sau khi đổi và nghịch đảo( mũ -1):

![1](https://user-images.githubusercontent.com/84214843/120604561-5fa91180-c477-11eb-80da-fd086f0d6c86.png)

thử lấy một kết quả từ binary nhân với cả 3 trường hợp trên:

![1](https://user-images.githubusercontent.com/84214843/120604754-8b2bfc00-c477-11eb-8d6f-fac83a2a6db4.png)

Ta thấy được trong cả ba trường hợp trên nó ra kết quả giống nhau chỉ khác dấu mà thôi, xem kĩ hơn 1 chút với trường hợp thứ hai thì ma trận trước sau luôn là số dương, để cho tiện(kết quả luôn là số dương) ta sẽ dùng trường hợp 2 cho toàn bộ quá trình(25 lần) và chỉ cần thêm điều kiện nếu có phần tử nào trong ma trận âm thì chuyển nó thành số dương

Mình viết một script bằng C để đảo ngược toàn bộ quá trình(khôi phục kết quả về mảng ban đầu là (3,4,5))

code C thì hầu như viết lại theo decompilation của IDA chỉ khác một chỗ là nhân với trường hợp 2 mũ (-1) và thêm điều kiện nhứ ở trên 

![1](https://user-images.githubusercontent.com/84214843/120606159-13f76780-c479-11eb-9ade-38debd32e605.png)
![2](https://user-images.githubusercontent.com/84214843/120606173-18238500-c479-11eb-88d4-2cf32f065ec6.png)

Và kết quả: 

![3](https://user-images.githubusercontent.com/84214843/120606204-207bc000-c479-11eb-8ddc-8a107ebe7423.png)

Thực sự là có thể khôi phục lại mà chỉ dùng trường hợp 2 :)))

tiếp theo mình chỉ cần viết một hàm đảo ngược của hàm encrypt(sub_8EA()) rồi chèn vào code trên thôi, cũng dựa trên code của IDA và viết ngược lại:

![1](https://user-images.githubusercontent.com/84214843/120606916-e19a3a00-c479-11eb-9319-218fd28307f3.png)

và thêm vào đây:

![1](https://user-images.githubusercontent.com/84214843/120607132-18705000-c47a-11eb-8ec5-f845d8972654.png)


và kết quả cuối cùng:

![1](https://user-images.githubusercontent.com/84214843/120607239-30e06a80-c47a-11eb-99fa-e35925520933.png)

Flag: dctf{x_p3de_h3rc00lem}













