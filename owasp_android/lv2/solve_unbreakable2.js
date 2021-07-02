function rootDetectionBypass(){

	
	var sys= Java.use("java.lang.System")
	sys.exit.overload("int").implementation = function(x) {
		console.log("we are avoiding exit the app :)")
	}

}


function extractSecret(){
	console.log()
	setTimeout(function(){
		Interceptor.attach(Module.findExportByName('libfoo.so', 'strncmp'),{

			onEnter: function(args){

				if( Memory.readUtf8String(args[1]).length == 23 && Memory.readUtf8String(args[0]).includes("I want your secret asap")){
					console.log("*******SECRET********")
					console.log(Memory.readUtf8String(args[1]))
					console.log("*******SECRET********")
				}

			},
    onLeave: function (retval) {
    }
});
	},2000);
}


//calling directly the root detection bypass, executed when Frida runs

rootDetectionBypass()
extractSecret()