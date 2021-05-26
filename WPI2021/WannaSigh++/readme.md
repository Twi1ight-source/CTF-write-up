Decompiled in IDA

hàm main():

![113](https://user-images.githubusercontent.com/84214843/119587098-2d087480-bdf8-11eb-9d6d-2e8eba4b95a2.png)

và ta thấy một hàm thú vị encrypt():

![113](https://user-images.githubusercontent.com/84214843/119587835-b8363a00-bdf9-11eb-8260-ec33240dd219.png)

từ hàm encrypt() ta thấy được hàm lấy tham số đưa vô hàm srand() như một seed từ đó rand() sinh ra các bộ số và lấy các số đó xor với data đọc từ flag.txt rồi ghi kết quả vào file your-flag.ransomed 

--> Vậy ta chỉ cần lấy data từ file ransomed đề cho rồi đem xor với các số từ rand() là ra được flag ban đầu

Mục tiêu bây giờ là phải tìm seed, quay lại hàm main() 

Ta thấy hàm getIPStr():

![113](https://user-images.githubusercontent.com/84214843/119592323-7493fe00-be02-11eb-98f4-9ae22bb40b59.png)

Quan sát ta thấy nó kết nối với một địa chỉ thông curl, mình thử kết nối trên linux và nó trả về một địa chỉ ip

Phân tích thêm mình thấy tiếp đến nó gửi cái gì đó đến địa chỉ wannasigh109fn10fn48vh.wpictf.xyz ở port 18610, vì thế mình dùng netcat để thử gửi một cái bất kì đến địa chỉ trên: 

![113](https://user-images.githubusercontent.com/84214843/119592672-1fa4b780-be03-11eb-964a-110d112e0c56.png)

và nó trả về một chuỗi có lẽ là gửi sai

Quan sát thêm mình thấy có một cấu trúc kết hợp chuỗi "Baahhhh_" với địa chỉ ip mình nhận được ở trên, vì thế mình kết hợp lại và thử gửi lại địa chỉ wannasigh109fn10fn48vh.wpictf.xyz ở port 18610,   well:)) kết quả trả về là một số (1618617746)---> co thể nó là seed mà mình cần tìm 

tới đây thì mình viết scipt solve được rồi :)))

![113](https://user-images.githubusercontent.com/84214843/119594500-1a953780-be06-11eb-83bb-125b85bbdac4.png)

Flag : WPI{backup-your-files}





