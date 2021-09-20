Trong quá trình phân tích và debug bằng IDA thì mình thấy một số exception(có lẽ là anti-debug) và dường như chương khởi tạo một process file PE và thực thi với nó 

Vì thế mình chuyển qua debug bằng x32dbg để dump file, dùng Debug > Advanced > Run (pass exceptions) để bypass hết anti-debug

Cuối cùng mình debug thôi, cho chương trình chạy tại lúc hỏi flag, nhìn qua dump 2 thì thấy:

![2](https://user-images.githubusercontent.com/84214843/133975776-cb41f3e5-4477-4842-b0b9-675ef6fe796b.png)

-Dùng hiển thị trong memory-map thì thấy có 1 section ko có tên với protection và initial đều là EWR--(đây là file cần tìm)

![Ảnh chụp màn hình 2021-09-20 154011](https://user-images.githubusercontent.com/84214843/133976199-3e3d667b-0d76-43a5-a3a5-0af97014aa63.png)


Tiến hành dump nó ra rồi quăng vào IDA thì thấy có hàm check, dùng z3 để giải

Flag: FWORDctf{Wh4t_4b0ut_th1s_w31rd_L0ng_fL4g_th4t_m4k3_n0_s3ns3_but_st1LL_w1LL_g1v3\y0u_s0m3_p01ntz}

