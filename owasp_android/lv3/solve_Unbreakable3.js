function bypassAllCheck() {

var system= Java.use("java.lang.System");
system.exit.implementation= function(var0) {
	console.log("Not today...");
};

console.log("Overloading fgets() to avoid frida detection");
var fgetsPtr= Module.findExportByName("libc.so", "fgets");
var fgets=new NativeFunction(fgetsPtr, 'pointer',['pointer', 'int', 'pointer']);

Interceptor.replace(fgetsPtr, new NativeCallback(function (buffer, size, fp) {	//buffer, size,sp la
												//minh tu dinh nghia theo cac tham so trong ham fegts()
	var retval= fgets(buffer,size,fp);
	var bufstr=Memory.readUtf8String(buffer);	//doc buffer o day la v3
	if (bufstr.indexOf('frida')>-1) {			
		Memory.writeUtf8String(buffer, 'bye Frida');
	}
	return retval;
}, 'pointer', ['pointer', 'int', 'pointer']));

console.log("Now safety you can click OK");

}

//vi emulator su dung x86 nen phai lay dia chi cua libfoo.so ben muc x86
function extract() {
	setTimeout(function() {
		var base_address= Module.findBaseAddress('libfoo.so');
		var extract_function= base_address.add(0xFA0); // tim dia chi cua ham bang cach lay base_address 
												//cong them dia chi xem trong IDA
		Interceptor.attach(extract_function, {
			onEnter(args) {
				console.log("Base address: " + base_address);
				console.log("extract_function address: " + extract_function);
				console.log("Reading buffer args[0]");
				this.buf= args[0];			//doc v7
				console.log("Reading complete");
			},
			
			onLeave(result) {
				console.log("--------------");
				var numBytes=24;
				var buff =Memory.readByteArray(this.buf, numBytes);
				console.log("[+] Secret key hexdump: ");
				console.log(hexdump(buff, {length: numBytes, ansi:true})); //de duoi dang hexdump
														//lay 24 byte do dai cua v7
			}
		});
	},2000);
}
		

bypassAllCheck()	
extract()
	