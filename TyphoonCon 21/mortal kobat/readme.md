Hàm main:

![main](https://user-images.githubusercontent.com/84214843/126894370-ae98438b-59cb-477c-8b22-7134a584f179.png)

+Ta thấy rằng hàm dùng memcpy để copy 0x3EB0 bytes từ unk_F20 và dest và đưa và hàm sub_B6C

sub_B6C gồm hai hàm nữa:

+sub_97E:

![RC4 1](https://user-images.githubusercontent.com/84214843/126894445-fa49d58d-0251-42b7-835e-fff419ff1002.png)

+sub_A57:

![RC4 2](https://user-images.githubusercontent.com/84214843/126894451-b9dc27f9-9701-4af6-9d50-a46beba89c1b.png)

+Qua phân tích nhứ trên ta thấy rằng sub_B6C sử dụng RC4 cipher, tham khảo ở đây:

![RC4 3](https://user-images.githubusercontent.com/84214843/126894498-f94dbdb1-af55-42f1-862e-0ecfd15ac1ba.png)

+Xem tiếp hàm sử dụng memfd_create(), fexecve() có lẽ để tạo một file gì đó, mình đoán nó tạo một file rồi dùng RC4 decrypt data từ unk_F20 rồi ghi vào file vừa tạo 

-->Vì vậy bây giờ mình viết script để thục hiện điều trên 

![1](https://user-images.githubusercontent.com/84214843/126894653-09adc215-dfac-44bc-8dfc-ad8608547deb.png)

+Nó tạo ra một file ELF khác: 

+Phân tích MortalKombat.dec:

+cái cần phân tích nằm trong hàm sub_C4D()(ở trong init chứ ko phải main):

+Ta thấy được đây là một nanomites(nghĩa là gồm hai quá trình: chương trình cha và chương trình con, trong đó khi chương trình con đang chạy khi đến một đoạn sẽ raise một signal đến chương trình cha và chương trình cha sẽ gửi cách xử lí về chương trình con)

+Phân tích chương trình cha trước:

![1](https://user-images.githubusercontent.com/84214843/126894972-318c5ced-b58e-4182-aae6-76cba5e1d5e6.png)

![2](https://user-images.githubusercontent.com/84214843/126894978-7cae16d2-7f5f-4c99-8745-f72e23b5c905.png)

+Ta thấy được với mỗi signal khác nhau thì chương trình cha sẽ gửi cách xử lí khác nhau

+quay lại chương trình con:

![1](https://user-images.githubusercontent.com/84214843/126895060-e1f344d3-65ac-4e63-ba8a-c29d76026649.png)

+Ta thấy được tại chỗ qword_203020 chính là shellcode của chương trình con, dùng make code của IDA để chuyển hết thành asm code

![1](https://user-images.githubusercontent.com/84214843/126895146-b35b9aca-e3b0-4323-b05a-812970a6726e.png)

+Quan sát môt chút phần đầu của chương trình:

-->Ta thấy input lưu tại rdi được chuyển vào r9, sau đó thực hiện một số phép biến đổi đối với r12b, sau đó input[0] chuyển vào r11b, cuối cùng ud2 (chúng ta biết khi gặp ud2 con sẽ raise SIGILL tới cha và ta xem lại chương trình cha sẽ thực hiện ror(v16,v17), mình đoán nó sẽ thực hiện ror(input[0], r10=0x1c)

-->Rồi nó sẽ so sánh với r12b

+Mình viết một script bruce-force thử xem:

![1](https://user-images.githubusercontent.com/84214843/126895344-6ae44ac7-45f0-415a-bc0d-3092b8ee0a9d.png)

+Và nó ra S (chữ cái đầu của S3D{ ) , vậy có lẽ nghĩ theo cách này là đúng

+Đến block tiếp theo , inc r9 có lẽ là chuyển tiếp qua inp[1] --> với mỗi block nó check 1 kĩ tự trong input

-->Từ đó ta map lại các signal như sau:

    +ud2 --> ror(v16,v17)
    
    +mov 0x1c
     syscall   -->ror(v14, v17^68)
     
    +int 3 -->rol(v16,v17)
    
    +mov rax, qword ptr ds:dword_0 -->xor(v16,v17)
    
    +idv -->add(v6,v17)
    
    +mov 0x12
     syscall  -->rol(v14, v17 ^65)
     
 +Tới đây thì brute-force theo từng block để tìm ra input thôi
 
 FLAG: S3D{Th3r3_4r3_F4t3s_W0rs3_Th4n_D34th!}










