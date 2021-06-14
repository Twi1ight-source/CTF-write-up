Load vào IDA:

Main:

![1](https://user-images.githubusercontent.com/84214843/121856954-49287300-cd1f-11eb-98fe-a7169ab8f3e1.png)
![2](https://user-images.githubusercontent.com/84214843/121856975-4ded2700-cd1f-11eb-9ce3-efee3ecfab2c.png)

Bài này binary nó load thư viện gmpz để thực hiện một số câu lệnh, phép biến đổi

Về cơ bản thì nó nhận file wtflag.txt rồi sau đó rồi sau đó thực hiện một vài encrypt rồi lưu lại trong file wtflag_enc

giờ mình sẽ đi phân tích kĩ chương trình hơn(mình cũng có comment ở hình trên)

+ Đầu tiên nó sẽ nhận input rồi biến đổi nó thành hex-string tại hàm sub_3706(mình debug chứ đọc chay ko được)

+ Sau đó hex-string sẽ được pad thêm 0 ở đằng sau trong trường hợp độ dài nó không đủ 256

![1](https://user-images.githubusercontent.com/84214843/121858233-9c4ef580-cd20-11eb-99f5-e6d23992a224.png)

+ Tiếp đến nó chuyển hex-string thành integer-string với base là 16 thông qua hàm sub_43B4 và lứu lại vào v19, v39 được tạo ra là một số random

+ Tiếp đến cho chia integer-string thành hai phần bằng nhau ( v16, v17) và sử dụng v39(random) để bù lại cho phần bị mất 

![1](https://user-images.githubusercontent.com/84214843/121859366-d240a980-cd21-11eb-80ec-56f343a75ea9.png)

+ Tiếp đến nó thực hiện 2 lần enc() tại hàm sub_3525() sử dụng v16, v17 , số random và số 2:

-->lần 1 là sub_3525(v17,v16, random,2)

-->lần 2 là sub_3525(v16, 2* v17, random,2)

![1](https://user-images.githubusercontent.com/84214843/121861850-67dd3880-cd24-11eb-9c49-eea85b96fc6a.png)


+ hàm sub_3525():

![1](https://user-images.githubusercontent.com/84214843/121860277-e5a04480-cd22-11eb-9511-5cbb1ca2c237.png)

(xem cũng dễ hiểu)

Qua đó ta thấy được nó thực hiện vòng lặp n lần với n là số random, vì vậy thực hiện bao nhiêu lần và ra số cụ thể ta ko thể biết được, nhưng để ý thấy các số tạo ra bởi vòng lặp sẽ hội tụ về (x+2y)/3 với n càng lớn thì nó càng gần --> số cuối cùng sẽ là (x+2y)/3

+ out_1, out_2 tạo ra từ 2 hàm enc() trên 

+ Sau đó chương trình sẽ check độ dài của out_1 và out_2 nếu là lẻ sẽ pad thêm 0

![1](https://user-images.githubusercontent.com/84214843/121861978-90fdc900-cd24-11eb-88e8-2d3882184960.png)

+ Cuối cùng thì từ hai cái đó nó chuyển thành byte rồi gộp lại và phân cách nhau bởi 'SSSS

>>>>mình viết 1 script để tách 2 cái out_1, out_2 ra rồi từ đó suy ngược lại v16,v17 rồi brute-force ra flag (sol.py)









