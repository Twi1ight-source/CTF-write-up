Note lại bài này phần reverse cython còn phần giải mã thì chịu :v

Đầu tiên phần main logic nằm trong _pyx_pymod_exec_xxx với x là tên file 

+Thì mới vô nó import 1 số thư viện:

![1](https://user-images.githubusercontent.com/84214843/160855057-6f631099-a8ec-4613-a415-84433e9f69ff.png)

![2](https://user-images.githubusercontent.com/84214843/160855101-7335ab55-ad17-4c73-b634-5a0c02f83fcb.png)

![3](https://user-images.githubusercontent.com/84214843/160855122-0d12ed6b-4f7c-452a-bd66-30b386293632.png)

+Sau đó gọi hàm keygen()

![4](https://user-images.githubusercontent.com/84214843/160855191-96ac42cc-6ffe-4534-b5e0-d25caecbc427.png)

+Vô coi thử

![1](https://user-images.githubusercontent.com/84214843/160856032-d66ed371-d964-4e64-a135-95a06926eb02.png)

Nó gọi 2 tham số của hàm là dbit với nbit

![1](https://user-images.githubusercontent.com/84214843/160856499-3cb86297-0b48-496a-8dce-5eada4ddd1b9.png)

+nó định nghĩa dbit với nbit như trên, phải chuyển qua asm mới biết được

+Hàm so sánh:

![1](https://user-images.githubusercontent.com/84214843/160858388-47be5b38-c298-44ea-9b98-a8c893f8f0d6.png)

với tham số thứ 2 là 0 có nghĩa là < (theo thứ tự (<, <=, ==, !=, >, or >=) tính từ 0 tương ứng)

+lấy hàm getRandomNBitInteger():

![1](https://user-images.githubusercontent.com/84214843/160860804-d28eb3da-4b7a-496c-b83e-5a7dd4f6297f.png)










