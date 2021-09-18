Đây là một bài find shorted path in maze

Hàm chứa hàm lấy input và chứa hàm check() tại sub_9900():

Kiếm hoài ko ra hàm nào nhận input nên mình debug luôn, mỗi lần trace đến lệnh call mình nhập input luôn 

Hàm sub_9590() check input (tìm mãi mới thấy):

+ Ở đây chương trình chỉ nhận 4 giá trị input là: h,j,k,l (kinh nghiệm mấy lần trước có thể đây là một bài maze)

+ Sau một hồi debug thì biết được:

  -Thanh ghi r8 chứa content của maze(debug mới thấy được và mình dump ra luôn)
  
  -[r8+13A0h] :  chứa tọa độ y của maze (nghĩa là cột) rồi so sánh với 0x19(25) nếu lớn hơn là fail -->có 25 cột
  
  -[r8+1398h] :  chứa tọa độ x của (nghĩa là hàng) rồi so sánh với 0x18(24) nếu lớn hơn là fail -->có 24 hàng
  
  ==>Đây là một 24x25 maze
  
  -case h: lấy [r8+13A0h]-1 (y-1) --> turn left
  
  -case j: lấy [r8+1398h]-1 (x-1) -->go up
  
  -case k: lấy [r8+1398h]+1 (x+1) -->go down
  
  -case l: lấy [r8+13A0h]+1 (y+1) --> turn right
  
  -Cuối cùng nó lấy giá trị tại tọa độ (x,y) đó, nếu giá trị đó khác 0 thì check xem có bằng 2 ko nếu ko fail rồi out --> 2 là điểm đích
  
  -Còn vị trí bắt đầu là (1,13) (debug mới biết được) và sau khi dump maze ra rồi thì ta suy ra vị trí của 2 là (24,19)
  
+Tới đây thì mình dùng bfs để giải (script java lụm trên mạng ở đây https://techiedelight.com/compiler/?~lee_algo_print_shortest_path_java) rồi một script để convert lại thành 4 kí tự (h,j,k,l)

Kết quả:

![2](https://user-images.githubusercontent.com/84214843/133883824-1ae7de2e-3f44-421c-8a51-56eb172f0eee.png)

