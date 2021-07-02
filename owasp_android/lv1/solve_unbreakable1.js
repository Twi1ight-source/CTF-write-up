Java.perform( function() {
	console.log("Starting hook...")
	var sys= Java.use("java.lang.System")
	sys.exit.overload("int").implementation = function(x) {
		console.log("we are avoiding exit the app :)")
	}
	
	console.log("Done !!!")

//cái này để khi nhấn nút ok ko bi out 

	console.log("Finding password...")
	var classAA =Java.use("sg.vantagepoint.a.a");
	classAA.a.implementation= function(x1,x2) {
		var raw=this.a(x1,x2);			//xem giá trị trả về của function
		var output=""
		for (var i=0;i<raw.length;i++) {
			output+=String.fromCharCode(raw[i]);	//nó trả về dưới dạng byte nên phải chuyển qua kí tự 
													//mới xem được 
		}
		console.log("===>" + output);
		return raw;
	};
});
	