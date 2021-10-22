Bài này giống với bài Omen ở chỗ nó cũng thực thi 1 file PE khác trong chương trình, nhưng khác ở chỗ nó chạy file PE đó ngay từ đầu chứ không cần phải debug tới lúc sau mới thấy.

+Data của file PE nằm ở phần segment .data nên chỉ cần dùng x32 dbg để dump ra.

+Hàmm main:

![0](https://user-images.githubusercontent.com/84214843/138385550-bb7c6126-2002-4986-9a47-796304c52b25.png)

+Có vẻ như chương trình lấy tới 400 char input

+Xem hàm check() in pesuo-code có vấn đề nên chuyển qua asm coi thử:

![1](https://user-images.githubusercontent.com/84214843/138385783-33f3ac7b-6107-4777-99d6-ba374772a2bf.png)

+Ây dà là 1 loại anti-diassembling với jz và jnz

+Đã vậy thì dump byte chương trình ra rồi sửa byte code lại thôi (loại bỏ bytes của 2 câu lệnh đó)

![0](https://user-images.githubusercontent.com/84214843/138386143-b061fe0e-c17a-4149-a8ab-7eb514500b66.png)

+Thế là được file dump1.exe, quăng vô IDA coi tiếp

+Cái phần check không hiểu sao ko chuyển thành function để F5 được nên đành đọc ASM tiếp, và nó rất dài đúng để check 400 kí tự input(xem file res.txt)

![0](https://user-images.githubusercontent.com/84214843/138386498-44d6d085-659d-414a-8bf3-3d2ff32da630.png)

+Nó lấy input từ edi vô cx mà mình ko hiểu sao lại so sánh với 1, keo xuống dưới xem cũng chỉ toàn 0 với 1 và nhận thấy mỗi input cũng có block check 8 lần nên suy ra đó là bit của 1 byte input (1 byte = bit) -->Nó check bit và chỗ shr .... là chỉ vị trí của bit trong byte đó.

+Nếu cái này ngắn thì làm thủ công là dễ còn cái này quá dài tới 400, nên phải viết script để tự động thôi

solve.py






