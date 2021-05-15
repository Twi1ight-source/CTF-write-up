đây là một file viết bằng golang nên việc tìm hàm main cũng ko dễ 
Hên là dùng radare2 nó định nghĩa được hàm main nên mình copy địa chỉ của hàm main() rồi dùng G ở IDA để tìm địa chỉ đó

Khi biết được hàm main() rồi thì chỉ việc debug và sửa một số cờ nhảy để nó nhảy vào block in ra flag là  xong :)))
