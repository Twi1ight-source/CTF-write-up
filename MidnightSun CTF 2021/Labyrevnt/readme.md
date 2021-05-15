Decompiled hàm main:

![113](https://user-images.githubusercontent.com/84214843/118348126-53195380-b572-11eb-84b9-139b90636d6c.png)

 Ta thấy  if ( (unsigned __int8)walk_start() )  thì sẽ ra flag, có nghĩa là giả trị trả về của hàm đó phải bằng 1
 
 Đi vào hàm Walk_start():
 ![113](https://user-images.githubusercontent.com/84214843/118348199-e783b600-b572-11eb-9b33-a793e7af28c3.png)
 
 Ta thấy input đầu tiên phải bằng 97(là 'a') còn ko sẽ trả về 0 --> fail, mà nó là a  thì nó sẽ nhảy vô một hàm check khác
 và có mấy trăm hàm như thế và rẽ nhánh khác nhau, vì thế quá kinh khủng để làm tay truy path đến Walk_end :(((
 
 ![113](https://user-images.githubusercontent.com/84214843/118348303-91634280-b573-11eb-98d0-393a6c67c486.png)
 
 Ta sẽ sủ dụng Proximity_View của IDA để truy path dẫn đến walk_end
 -đầu tiên tại hàm main nhấ chuột phải và chọn Proximity_View
 -sau đó nhấn chuột phải chọn (add node by name) để thêm node Walk_end
-sau đó tại thẻ main nhấn chuột phải chọn (find path) và chọn Walk_end
Cuối cùng ta sẽ có đường dẫn thế này :)))))))

![113](https://user-images.githubusercontent.com/84214843/118348419-5f9eab80-b574-11eb-8e3e-894961f2b929.png)

sau đó mình sẽ viết một script dùng angr để lấy required input của mỗi function trong đó

(find output ....py)

nhưng để nhập tên từng hàm vô script khá là khoai vì thế mình viết một ghidra scrit để liệt kê từng hàm rồi copy-paste 
vào cho khỏe :))

(find_path.py)

sau khi nhận được input rồi thì viết một script để gửi đến server là xong



