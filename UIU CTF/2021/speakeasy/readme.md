+Check bằng DIE thì thấy chương trình dùng Vmprotect

+Hàm main:

![0](https://user-images.githubusercontent.com/84214843/138536856-2c1fe245-3d29-43f5-8fd6-b05976d2489b.png)

+Hàm check:

![1](https://user-images.githubusercontent.com/84214843/138536956-262b2ca2-c5eb-46f1-ac48-d9959d6463da.png)

-->Chỗ đó IDA có dịch sai một chút nên đã sửa lại (ở phần comment) sau khi xem qua asm (nhưng cũng chỉ đúng phần i<len(a1) nhưng không hề có vòng lặp, chả hiểu)

+hàm sub_1400014C0, bấm vô thì nó nhảy đến loc_140028270:

![1](https://user-images.githubusercontent.com/84214843/138537076-f52b31ff-1126-423d-9985-8ee6c86ac0ef.png)

-->Có vẻ hàm này đã được encrypt bằng Vmprotect

-->Dùng NoVmp để dump hàm sử dụng Vmprotect ra:

![1](https://user-images.githubusercontent.com/84214843/138537150-cffdbdfd-8f50-4bab-bf98-2ac69914129b.png)

+Nhìn sơ qua thì thấy có file 0000000000028270.optimized.vtil có 28270 giống cái loc_loc_140028270 

-->Dùng Vtil-Util để disassemble ra thử: (dùng vtil dump 0000000000028270.optimized.vtil)

![1](https://user-images.githubusercontent.com/84214843/138537310-128ec16e-1ce8-497b-b5d6-ded07086fd0d.png)

-->Có vẻ như hàm này: inp[i] ^  (0x14378 + &&base) -->Mình đoán tại địa chỉ 0x14378 là một mảng số -->thế là mình jump đến địa chỉ đó (lúc này rebase chương trình lại bằng 0x0 cho đỡ phiền)

-->Dump ra thôi (chỉ lấy 0x28 số vì hồi nãy vòng lặp là 0x28 lần):

    [0x45,0x33,0x75,0xA7,0xA2,0xD9,0x64,0xE5,0xE2,0xC6,0x88,0xF9,0xD2,0xFA,0x0F,0x15,0x7C,0xBA,0xD0,0xC4,0xF4,0xB4,0x2D,0x42,0x79,0xF5,0xFB,0x03,0x56,0x54,0xC0,0xC8,0x0F,0x04, 0x0,0x0,0x0,0x0,0x0,0x0]
    
+Quay lại hàm sub_14F0 thì nó nhảy đến sub_262C9 (hàm này cũng bị encrypt)

-->Dùng vtil-util dump ra nữa:

![1](https://user-images.githubusercontent.com/84214843/138537585-0b9f08ea-eb2f-4367-96a9-1631e2107e47.png)

-->Lấy cái kết quả xor lúc trên tiếp tục xor với (inp[i] >>1)

+Cuối cùng là hàm sub_15D0: hàm này nhảy đến sub_12B360

+Dump ra thì rất lơn luôn rất khó đọc mà nó gần vùng RVA của vmprotect nên mình kéo xuống xem thử thì thấy có hàm memcmp tại vùng 0x2690

+Debug xem thử xem nó so sánh sao thì thấy kết quả sau 2 cái xor trên được so sánh với một mảng của chương trình(rốt cuộc hàm kia nhiều thế cũng chỉ có cái này đáng xem)

-->Tới đây thì viết script xor ngược lại là ra flag:

Flag: uiuctf{D0nt_b3_@_W3T_bl4nK3t_6n7a}





