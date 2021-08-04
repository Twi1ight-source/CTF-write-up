Hàm main() :

![1](https://user-images.githubusercontent.com/84214843/128108943-2f191680-f15f-4811-986b-d7187ad3d4d3.png)

+Như đã thấy hàm lấy input khoảng 28 kí tự

+Rồi đi qua hàm check() (sub_1410), nếu giá trị trả về bằng 0 thì fail, còn khác 0 là success

Hàm sub_1410():

![1](https://user-images.githubusercontent.com/84214843/128109533-d3202e5f-f1b2-44fd-aded-57be49604c42.png)
![2](https://user-images.githubusercontent.com/84214843/128109538-c42bb1f4-76cc-4284-aa05-fc3c046ba090.png)
![3](https://user-images.githubusercontent.com/84214843/128109541-d6004bab-2920-4e9a-a218-fbf5200745a7.png)

+input là chỉ giới hạn trong 6 chữ: b,d,f,l,r,u

+Tùy vào một trong 6 chữ này là a3 + thêm 1 khoảng v8 khác nhau, rồi thêm một vài điều kiện cho a3

+Sau đó a3 sẽ đưa làm vị trí trong mảng byte_2080 (v10= byte_2080[a3]) -->nếu byte_2080[a3]==0 thì lập tức return result(result=0) -->fail

+Sau khi pass được mấy cái trên thì chuyển qua kí tự tiếp theo của input

+Nếu đi hết kí tụ cuối cùng của input (!v6) thì đi đến label_12

+Label_12: check xem v10=byte_2080[a3] có bằng 3 ko, nếu có -->success, ko -->fail

-->Vậy bây giờ ta sẽ extract mảng byte_2080 với các giá trị a3 cần thiết để byte_2080[a3] !=0

(extract.py)

+Đây là các giá trị a3 cần thiết để byte_2080[a3]!=0:

    +[84, 133, 134, 135, 136, 137, 141, 146, 152, 155, 156, 157, 159, 160, 161, 162, 163, 166, 168, 174, 177, 178, 179, 180, 181, 185, 188, 190, 192, 199, 200, 201, 203, 204, 205, 206, 207, 210, 212, 214, 216, 221, 223, 224, 225, 226, 227, 254, 262, 276, 278, 282, 320, 322, 328, 344, 375, 377, 379, 380, 381, 383, 386, 388, 392, 397, 398, 399, 400, 401, 403, 404, 405, 408, 410, 414, 419, 421, 423, 424, 425, 432, 434, 441, 442, 443, 444, 445, 446, 447, 448, 449, 452, 454, 463, 464, 465, 466, 467, 469, 496, 498, 502, 518, 520, 524, 540, 542, 546, 562, 564, 566, 568, 586, 588, 590, 617, 619, 621, 622, 623, 628, 630, 632, 639, 640, 641, 642, 643, 645, 646, 647, 650, 652, 658, 661, 663, 667, 669, 683, 685, 686, 687, 688, 689, 694, 698, 700, 705, 707, 709, 710, 711, 712, 713, 738, 742, 760, 764, 782, 804, 806, 826, 830, 859, 860, 861, 862, 863, 864, 865, 866, 867, 870, 872, 874, 881, 883, 885, 886, 887, 889, 894, 896, 898, 900, 903, 904, 905, 906, 907, 909, 911, 914, 918, 920, 922, 925, 927, 928, 929, 931, 932, 933, 936, 938, 940, 944, 947, 949, 950, 951, 952, 953, 955, 982, 1002, 1006, 1028, 1052, 1054, 1068, 1074, 1103, 1114, 1123, 1124, 1125, 1127, 1128, 1129, 1149, 1150, 1151, 1167, 1168, 1169, 1171, 1172, 1173, 1175, 1178, 1184, 1189, 1190, 1191, 1195, 1296]

+ a3 bắt đầu từ 84 và sau khi đi hết 28 kí tự input a3 phải bằng 1296 (vì byte_2080[1296]=3)

-->Tới đây mình viết script z3 để tìm các kí tự input phù hợp

(solve.py)
