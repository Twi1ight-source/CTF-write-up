Làm tương tự như bài 3 để lấy các file (web4.wasm, web4.wat, web4.dcmp)

Sau khi xem lướt qua mình thấy cũng chỉ cần quan tâm hai hàm là check_flag() với copy():

+copy() lấy input và lưu vào mảng [1072]

+check_flag()  lấy các kí tự từ mảng [1072] sau đó encrpyt và cuối cùng so sánh với mảng [1024] cho trước( ở đây mình sẽ chuyển mảng [1024] về  mảng số nguyên):

![1](https://user-images.githubusercontent.com/84214843/121625548-dc527600-ca9d-11eb-91e7-5e5fd147f206.png)


Nhận thấy dù xem mã giả của code nó cũng quá dài dòng và phức tạp, vì thế mình quyết định debug file wasm sử dụng công cụ developer để trace với hiểu flow dẽ dàng hơn (với lại cũng tập đọc hiểu wasm :)) )

Mình bắt đầu với input là picoCTF{12345 để debug:

-->nhận thấy sau một hồi debug khoảng 5 kí tự liên tiếp, nó thực hiện một vài phép xor với các điều kiện dựa theo i

-->mình thấy kết quả đầu tiên sau khi encrypt kí tự 'p' trả về là 106 nhưng nó lại nằm ở vị trí 1 chứ ko phải vị trí 0 của mảng như mình nghĩ, mình thấy lạ và debug tiếp và kết quả trả về lần thứ 2 là 24 lại nằm ở vị trí 0, rõ ràng là có sự trao đổi sau khi encypt, mình lại debug thêm một vài kí tự nữa và rút ra được kết luận: cứ mỗi hai kí tự thì nó đổi vị trí cho nhau của 2 kí tự trược đó 

-->toàn bộ quá trình encrypt như sau:

![1](https://user-images.githubusercontent.com/84214843/121625919-a235a400-ca9e-11eb-8e74-056812394be8.png)

Sau cùng mình viết một scipt dùng z3 để tìm toàn bộ kí tự thỏa yêu cầu  (solve.py)



