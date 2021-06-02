Decompiled bằng IDA , hàm main:
![113](https://user-images.githubusercontent.com/84214843/119290838-89905600-bc77-11eb-8f5f-b633b5c97d62.png)

đọc sơ qua thì ta thấy nó đọc data từ unk_1040

sau đó nó gọi hai functions, bấm vào sub_93A xem thử : 
Well:
![113](https://user-images.githubusercontent.com/84214843/119291098-0d4a4280-bc78-11eb-9294-149f428c3658.png)
![114](https://user-images.githubusercontent.com/84214843/119291124-12a78d00-bc78-11eb-9907-d030b0698991.png)
![116](https://user-images.githubusercontent.com/84214843/119291137-1804d780-bc78-11eb-94fc-a19bdb0ae8cf.png)

Ta thấy nó chia ra tới 14 trường hợp với sưitch() cộng thêm dữ kiện nó đọc 1 lượng lớn byte từ unk_1040, ta có thể kết luận 
đây là một VM 

Hàm sub_DA0:

![113](https://user-images.githubusercontent.com/84214843/119291347-8053b900-bc78-11eb-8e0a-014e7fbf0fc8.png)

tới đây mình vẫn chưa thể hiểu rõ cách hoạt động của VM( các registers và instructions) vì thế mình quyết địng debug 
Thông qua debug mình thấy được nó lấy data dưới dạng nhị phân của unk_1040:6 0 0 6 1 1 6 2 2 ..... và  nó lấy 3 số với mỗi lần lăp:

+[6.0.0]  thì nó nhảy vô trường hợp 6 và lấy byte 0xba

+3 số tiếp theo [6,1,1] cũng nhảy vô trường hợp 6 và lấy byte 0x91

Debug thêm nhiều cái nữa mình đưa ra kết luận:

  ->trong chuỗi 3 số mỗi lần lấy thì số đầu tiên là trường hợp, số thứ hai,ba là thứ tự thanh ghi (riêng trường hợp 4,6,12,13  thì số thứ ba là giá trị byte thứ 2048+ số thứ ba)
  
  ->vì thế ta có thể nói rằng trong data của unk_1040 thì 2048 bytes đầu để tạo instructions và các bytes còn lại là giá trị cho các thanh ghi
  
  -> tổng có 4 thanh ghi là R0, R1 ,R2, R3
  
  Biết được cách hoạt động rồi mình sẽ viết disassembler để tự động phân tích hết các bytes trong unk_1040
  
  (disass.py) và kết quả output (data.txt)
  
  phân tích một vài instructions đầu:
  
  ![113](https://user-images.githubusercontent.com/84214843/119294163-08888d00-bc7e-11eb-88f6-701a42f43bbd.png)
  
  ->Ta thấy mỗi block lấy R0 băng getc() và kết thúc bằng R3, tình cờ mình tính được nếu cho R3=0 thì R0=0x63(chính là 'c')
  
  ->block thứ 2, lấy R3 bằng 0 -> thì R0= 0x8b ^ 0xff= 0x74(chính là 't')  
  
  Đó là khới đầu ctf{  :)))))))) , tới đây mình có thể kết luận với mỗi block R0 lấy mỗi chữ trong input với getc và check xem R3 có bằng 0 không.
  
 Tới đây mình chỉ việc viết script bruce-force R0 với mỗi block là được flag =)))
 
 (sol.py)





