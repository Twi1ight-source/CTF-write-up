dùng lệnh file thấy dòng chữ 'no section header' có lẽ file đã bị packed

run chương trình bằng gdb rồi ctrl +c để interrupt, sau đó nhập gcore để lấy coredump của chương trình

Phân tích file core:

![1](https://user-images.githubusercontent.com/84214843/136487241-c09e8c7d-58bd-4181-8c2b-448c6ee8df60.png)

![2](https://user-images.githubusercontent.com/84214843/136487315-fdf6ef8e-a63a-48ae-b898-6ba8ce67aced.png)

+Ta thấy chương trình chỉ nhận 4 input là số và check nó, mỗi số đều có 2 điều kiện để check để chúng ta tìm ra

+Có một vài SIMD instructions nhưng lên mạng search cũng không khó( khuyên nên đọc assembly chứ đọc mã giả khó hiểu lắm)

-->Dùng z3 để tìm các số thỏa điều kiện của chương trình (z3 giải cũng khá lâu)
