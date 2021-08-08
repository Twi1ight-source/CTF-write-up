Bỏ vào IDA thì thấy hàm vuln:

![1](https://user-images.githubusercontent.com/84214843/128617811-47f5e0ef-e433-45e1-84a7-333796d55a71.png)

+Quan sát thì mình thấy hàm  __stack_chk_fail() mới là hàm cần phân tích, nhưng khi hàm vuln() lấy input tại fgets()

+nhập thử thì thấy ko làm sao mà nó nhảy vào  __stack_chk_fail() được

+Thủ dài một chút (khoảng 30 kí tự) thì lại vào được

Phân tích hàm  __stack_chk_fail():

+Nhìn thôi thì cũng chưa thấy gì nên mình quyết định debug

![1](https://user-images.githubusercontent.com/84214843/128617930-ace6865f-5348-4fe4-8544-9785cfef3897.png)

Qua debug thì thấy:
+loop 3 lần

+Đầu tiên nó lấy 8 kí tự tiếp theo từ vị trí thứ 10 trở đi của input tại [rbp+var_18] và lưu dưới dạng hex big-endian tại rax

+Sau đó nhân với hex tại [rbp+var_30] (debug sẽ biết giá trị) 

+tiếp đó cộng với 8 kí tự tiếp theo nữa (dưới dạng hex big-endian)

+Rồi cuối cùng so sánh với rax(debug sẽ biết)

+Nếu bằng nhau thì kết quả đúng sẽ lưu tại [rbp+var_30]

+ỏ lần loop thứ hai thì lấy 8 kí tự từ vị trí thứ 10 trở đi như cũ rồi nhân với [rbp+var_30] cộng với 8 kí tự tiếp theo nữa

+rồi so sánh với giá trị rax(debug sẽ biết)

+Còn lần lặp thứ ba nữa nhưng ko quan tâm vì đủ 2 phương trình 2 ẩn để giải rồi 

+Còn một loop 6 lần tiếp theo nữa nhưng debug cũng thấy ko check gì nữa

+Tới đây mình script z3 để giải thôi (solve.py)


