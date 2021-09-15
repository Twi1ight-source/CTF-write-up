Bài này là một kiến trúc mới là hexagon

Main:

![Ảnh chụp màn hình 2021-09-15 111602](https://user-images.githubusercontent.com/84214843/133369731-2fdc075c-8a96-44cc-a840-65680959c3bc.png)

+Hàm readflag() chỉ là read input mình nhập vào với len(input)=8

+Quan trọng là checkflag():

![Ảnh chụp màn hình 2021-09-15 111747](https://user-images.githubusercontent.com/84214843/133369911-35bd39be-ccb6-488b-9e84-d68fa8f0b33e.png)

![Ảnh chụp màn hình 2021-09-15 111826](https://user-images.githubusercontent.com/84214843/133369913-a6bf5bf4-7a6a-40e8-a38a-7fdc621d4d1f.png)

+Sau đây là một số instructions của kiến trúc này cần chú ý:

![Ảnh chụp màn hình 2021-09-15 111943](https://user-images.githubusercontent.com/84214843/133370027-9fe099ad-e2d7-4a67-a1e7-d8733da9afcc.png)

## r3:2 có nghĩa là r3 và r2 kết hợp lại và nó lưu memmory tại địa chỉ 0x3050D:

![Ảnh chụp màn hình 2021-09-15 112216](https://user-images.githubusercontent.com/84214843/133370197-29bb3f77-6b73-48ff-a3f7-2944d6842a31.png)

-->Đúng là nó lấy 8 bytes input -->mình nghĩ r3 giữ 4 bytes đầu và r2 giữ 4 bytes còn lại 

## Tiếp theo là lệnh nhóm: { r0 = r2  ,r2 = r0 } có nghĩa là nó thực hiện song song với nhau, tức là r0=r2 và r2 bằng giá trị r0 cũ(chứ ko phải là giá trị mới tức r2=r2, trong trường hợp này nó swap 2 giá trị)

+Sau đó nó thực hiện các biến đổi với 6 hàm hex() rồi so sánh với giá trị cuối cùng (trong đầu nghĩ đến z3)

+Hàm hex1():

![Ảnh chụp màn hình 2021-09-15 112758](https://user-images.githubusercontent.com/84214843/133370701-6f787838-c8bb-4eaf-88ff-eac735e86bd0.png)

## tstbit(a1,a2) trong tập kiến trúc này tương đương: return a1 &(1<<a2) !=0 (trong chương trình này vì a1,a2 đề cho cố định nên chương trình sẽ đi theo mọt nhánh thôi)

## not(r0) tương đương với: r0 ^0xffffffff

## còn khi xuất hiện hằng số âm , ví dụ như (r5 = ##-0x1644E844) thì đổi lại là: r5=0x100000000 - 0x1644E844

+Sau khi biến đổi xong thì check cuối cùng:

![2](https://user-images.githubusercontent.com/84214843/133398805-38fa0ba9-e8db-4e37-ad90-afea11b3f644.png)

+Tương tụ như r3:2, chương trình lấy r5:4 = memory tại địa chỉ 0x30515

+click vào thì thấy 8 bytes target cần so sánh

![Ảnh chụp màn hình 2021-09-15 153225](https://user-images.githubusercontent.com/84214843/133399200-927e5265-fff0-4c55-9d85-13e17a25ed36.png)

+Nhưng thấy rằng cái target này được sử dụng một lần tại start, click lên xem thử:

![image](https://user-images.githubusercontent.com/84214843/133399469-cbfb5f1a-81a4-4b94-b1fe-527212e78aac.png)

+Ta thấy rằng nó thực hiện một loop 0x50 lần lấy các giá trị từ r1(target) xor với r0 và r0+1 rồi lưu lại vào memory, tại đây 8 bytes cần so sánh đã thay đổi giá trị

+Dựa vào ở trên ta thấy sẽ so sánh r5 với r3 và r2 với r4

+Cuối cùng ta viết 1 script sử dụng z3 để tìm r2, r3 ban đầu và gộp lại thành input cần tìm
