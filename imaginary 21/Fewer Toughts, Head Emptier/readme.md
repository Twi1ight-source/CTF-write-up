Tương tự bài kia ,chuyển brainfuck code thành code c rồi compile thành file ELF rồi mở IDA lên xem

+Đặt breakpoint tại putchar() rồi bắt đầu debug, sau một hồi debug thì quan sát thấy thanh ghi rdi chịu trách nhiệm lưu kí tự char của flag, còn một thanh ghi gì đó ko nhớ chịu trách nhiệm lưu số lần lặp để in ra flag char liên tục dẫn đến chương trình in quá nhiều và bị crash

+Debug thêm một chút nữa thì mình thấy tại câu lệnh này thanh ghi đếm số lần giảm 1

![1](https://user-images.githubusercontent.com/84214843/128276882-9cc3b7ab-b722-47e9-abcd-fdda7941d1d0.png)

-->Có nghĩa là khi số lần giảm về 0 thì chương trình mới in kí tự kế tiếp

-->Mình chỉ việc patch cái thanh ghi đếm  lúc chương trình nhảy đến câu lệnh này bằng 0 là xong

-->Liên tục debug và patch lại như thế mình cứ từ từ gom được các kí tự của flag tại putchar(xem thanh ghi rdi)

Flag:ictf{th3_l3s5_th0ugh+_+he_b3teR}

