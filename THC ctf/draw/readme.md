-load tệp apk này vào một emulator để xem thử thì nó chỉ là một chương trình vẽ bình thường, sau khi vô thử phần setting mình thấy xuất hiện 
dòng chữ 'Bad Idea' ở phía dưới nên mình nghĩ ở phần setting phải có một cái gì đó 

-Mình mở bytecode-viewer để phân tích, sau khi xem ở main ko có gì quan trọng nên mình qua thẳng class Setting.Activity luôn, sau khi xem qua một hồi mình thấy chỉ có 2 hàm cận quan tâm là: decryptPayload() và loadServerFiles()

-Mình xem phần loadServerFiles() trước vì có thể load file từ ban tổ chức 

![1](https://user-images.githubusercontent.com/84214843/123189712-82ec3d00-d4c8-11eb-9fcc-0b494d4c74c9.png)

-Sau khi xem các string mình thấy thú vị và khoanh đỏ ở trên mình đoán đó là các file mà nó load từ server sau khi vô phần Setting trên app, về cơ bản hàm này sẽ thực hiện decryptPayload() đối với 2 file là (ExtClass.enc), (ExtClass.dex)

-Nhưng vẫn chưa biết cách làm sao lấy các file này nên mìnhh quyết định dùng apktool để extract file apk và xem file string 

+Ctrl + f để tìm các từ khóa như trên ví dụ như .zip thì wow mình tìm được :)) (https://challenges.thcon.party/reverse-jrjgjk-stI1gar-draw.per/cisc42M3HNc6tL3wOnJqjenvrihddn/files.zip) --> đó là đường dẫn tải file zip từ server

+Mình tiếp tục tìm kiếm đối với .enc và .dex nhưng ko có kết quả gì còn đối với 'url' thì mình cũng chả có gì ngoài đường dẫn file zip trên

+Tải về file zip và giải nén ra gồm 3 file (inf.enc), (ExtClass.enc) và một file ảnh (hóa ra file ExtClass.enc lại nằm trong tệp zip)

--> Mở 2 file (inf.enc) và (ExtClass.enc) thì toàn chữ trung quốc mà điều mình thấy lạ là phân tích chương trình nãy giờ nhưng hoàn toàn ko có sự xuất hiện hay thao tác nào đối với file (inf.enc) 

--> Mình nghĩ cũng như bài mision impossible nên chắc sẽ có cái gì đó trong file ảnh này nên mình dùng binwalk để kiểm tra thử và cũng ko có cái gì đặc biệt

-->Mình đoán hàm này sử dụng decryptPayload()  để decrypt file (ExtClass.enc) và lưu vào file ((ExtClass.enc))

+Tiếp tục xem hàm decryptPayload(): 

-->Rõ ràng là hàm này sử dụng thật toán  AES-CBC với key và IV tương ứng

![1](https://user-images.githubusercontent.com/84214843/123191516-9220ba00-d4cb-11eb-88bc-069ecfbd3d26.png)

-->Sau khi từ dò ngược lên từ key là var11 và IV là var13 thì key là v3 và IV là var4 ban đầu nhưng sau đó key được hash bằng sha256 (nhưng làm sao tìm được key và IV thì mình tiếp dò trong file string với từ khóa 'settings_1' và 'settings_2' và nó ra string thật :)))

![1](https://user-images.githubusercontent.com/84214843/123192414-11fb5400-d4cd-11eb-9550-aa176229fdb8.png)

-->Đúng như mình nghĩ sau khi decrypt file (ExtClass.enc) thì nó sẽ 'writebytes' vào file (ExtClass.enc)

![1](https://user-images.githubusercontent.com/84214843/123192150-88e41d00-d4cc-11eb-9b54-6c30c5fdbde2.png)

+Giờ đã có đầy đủ thì tới đây thì mình viết python để làm điều đó thôi

![1](https://user-images.githubusercontent.com/84214843/123192544-5a1a7680-d4cd-11eb-8f31-8c3a947fac44.png)

+Sau khi xong thì nó xuất ra file (ExtClass.dex) mình đem nó jadx-gui để phân tích: 

![1](https://user-images.githubusercontent.com/84214843/123192743-b67d9600-d4cd-11eb-9518-dd333a9638e8.png)

-->Nó thực hiện y chang ở trên nhưng chỉ khác key, iv và dùng file (inf.enc) để devrypt thôi các bạn chỉ việc thế vào script trên là ra kết quả 

Flag: THCon21{Dyn@m1c_c0d3_l0@d1ng_1s_$c@ry}









