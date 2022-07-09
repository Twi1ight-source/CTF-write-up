# Susware
Đây là một bài pe sử dụng một số kĩ thuật dùng trong malware

-Pe sử dụng một kĩ thuật process injection là [TLS callback](https://attack.mitre.org/techniques/T1055/005/)

> TLS callback vốn được dùng bởi os để setup/clean up các data của thread nhưng nó có thể tạo ra các memory space, hacker lợi dụng điều này để chèn mã độc vào các vùng nhớ và thực thi vùng nhớ đó một cách riêng biệt trước khi chuyển tới hàm main.


