Mình dùng (wget http://mercury.picoctf.net:47240/qCCYI0ajpD -q -O web3.wasm) để download file wasm của trang web đó về 

file (web3.wasm)

Sau đó mình dùng công cụ wabt để chuyển sang file wat (~/wabt/build/wasm2wat --generate-names web3.wasm > web3.wat)

file (web3.wat)

Sau khi xem code một hồi mình quyết định decompiled file wasm ra mã giả để xem dễ hiểu hơn (dùng ~/wabt/build/wasm-decompile web3.wasm -o web3.dcmp)

file (web3.dcmp)

Xem qua một lượt, mình thấy chỉ cần tập trung vào 2 hàm check_flag() với copy():

![1](https://user-images.githubusercontent.com/84214843/121623809-934cf280-ca9a-11eb-9983-09497074b4a2.png)

hàm copy() về cơ bản lấy từng kí tự trong input sau đó thực hiện một vài encrypt rồi lưu vào mảng [1072]

Sau đó nó sẽ so sánh với mảng [1024] được cho sẵn ở hàm check_flag() 

Bây giờ mình chỉ việc viết script để mô tả lại thuậ toán encrypt và bruce-force từng kí tự để ra flag

(sol.py)


