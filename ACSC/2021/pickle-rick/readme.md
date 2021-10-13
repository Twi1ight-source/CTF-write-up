Phân tích file python đề cho:

+check python vesion có phải 3.9 không

+rick_says là input nhập vào

+len(input) ==21

+dùng pickle để load một file pickle

--->Ta dùng pickletools.dis của python để disassemble file đó (out.txt)

Và bây giờ là lúc phân tích pickle bytecode:

![1](https://user-images.githubusercontent.com/84214843/137061797-43de91eb-0b21-4448-9c20-9df8afdee040.png)

+Mới vô chương trình tạo tuple từ các số đã cho (TUPLE 1 nhóm 1 số, TUPLE2 nhóm 2 số, ...)

-->Ví dụ đối với một số số trên hình trên là: ( ((115,), (99,)) , ((97,) ,(162,)) ).... (nói chung cái mảng số hơi bị dài nên viết lại hết cũng tốn cả đống thời gian)

+Tiếp theo có vẻ chương tạo function là search() trong file 'something_suspicious.py' dùng BINBYTES như là bytecode của chương trình

+Và thế là tiếp tục phân tích python bytecode( khá đau khi phân tích bằng tay) -->dùng dis.dis() trong python:

      import dis 
      a= bytecode cần phân tích
      dis.dis(a)
    
Phần đầu trong file bytecode.txt (lưu ý khi phân tích chỉ quan tâm với số trong ngoặc, số ko trong ngoặc ko cần quan tâm với _CONST là các hằng số đề cho theo thứ tự từ trên xuống tương tứng với vị trí 0,1,2.... tương tự với _FAST là các biến đề cho)

-->Sau khi phân tích xong thì kết quả như này:

![1](https://user-images.githubusercontent.com/84214843/137063734-6ba78f4e-bcd6-44c9-8daa-9753b5a82e5c.png)

+Tiếp đến là khởi tạo hàm mix(), phân tích tương tự thì ta có:

![1](https://user-images.githubusercontent.com/84214843/137063956-c009e9f9-b3ec-462c-85e5-c26d6a0c0290.png)

Phân tích tiếp theo nưa thì chương trình:

    ar=[]
    for x in mix(pickle_rick):
      arr.append(search(tuple,x))
    
 Và kết quả của arr được so sánh với mảng số chương trình đã cho:
 
 ![1](https://user-images.githubusercontent.com/84214843/137065239-cb6c0d42-a921-4ff6-ad40-897ff35985a2.png)
 
    for x in range(21):
      if (arr[x] != check[x]):
        print('wrong')
  
 +Về cơ bản thì ta có thể dựa vào mảng check để bruce-force ngược lại hàm search để tìm mảng sau khi mix(pickle_rick):
 
 ![1](https://user-images.githubusercontent.com/84214843/137065847-5e16848c-fc29-479f-a525-aabdceb58a67.png)
 ![1 1](https://user-images.githubusercontent.com/84214843/137065853-f547a9fd-1d2a-4769-a655-7956bc47a266.png)

Kết quả là:

    [98, 59, 114, 85, 203, 16, 155, 94, 218, 48, 235, 18, 189, 14, 117, 73, 138, 209, 91, 104, 28]
    
+Giờ chỉ còn cách tìm pickle_rick từ mix() nữa thôi

+Ban đầu định dùng z3 để tìm nhưng có lẽ qá phức tạp nên đới lâu quá

+Nhìn kĩ hàm mix() lên một chút thì chương trình khởi tạo hệ phương trình 21 ẩn và bắt giải :))

--->Dùng sagemath để giải (coi script của người khác)  (solve.sage)

Flag: ACSC{YEAH!I'm_pickle-RICK!}







        

  



