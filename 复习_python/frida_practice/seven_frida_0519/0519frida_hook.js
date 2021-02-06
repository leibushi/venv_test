function Login(){
    Java.perform(function(){
        Java.use("com.example.androiddemo.Activity.LoginActivity").a.overload("java.lang.String", "java.lang.String").implementation = function(str, str2){
            var result = this.a(str, str2);
            console.log("args0" + str + "args1" + str2 + " result:" + result);
            return result;
        }
    })
}
function challenge1(){
    Java.perform(function(){
        Java.use("com.example.androiddemo.Activity.FridaActivity1").a.implementation = function(bArr){
            console.log("inside Frida a function")
            return Java.use("java.lang.String").$new("R4jSLLLLLLLLLLOrLE7/5B+Z6fsl65yj6BgC6YWz66gO6g2t65Pk6a+P65NK44NNROl0wNOLLLL=");
    }
    })
}
function challenge2(){
    Java.perform(function(){
        var FridaActivity2 = Java.use("com.example.androiddemo.Activity.FridaActivity2");
        FridaActivity2.setStatic_bool_var();
        console.log(FridaActivity2.setStatic_bool_var.value);
        Java.choose("com.example.androiddemo.Activity.FridaActivity2",{
            onMatch:function(instance){
                instance.setBool_var();
                console.log(instance.setBool_var.value);

            },onComplete:function(){}
        })
    })
}

function challenge3(){
    Java.perform(function(){
        var frida3 = Java.use("com.example.androiddemo.Activity.FridaActivity3");
        frida3.static_bool_var.value = true;
        console.log("After set new value 1:" + frida3.static_bool_var.value);
    

        Java.choose("com.example.androiddemo.Activity.FridaActivity3",{
            onMatch:function(instance){
                instance.bool_var.value = true;
                console.log("After set new value 2:" + instance.bool_var.value);
                // 成员变量和方法重名了前面加加个_成员变量和方法重名了前面加加个_
                instance._same_name_bool_var.value = true;
                console.log("After set new value 3:" + instance.same_name_bool_var.value);

            },onComplete:function(){}
        })
    })
}

function challenge3_1(){
    Java.perform(function(){
        var Frida3 = Java.use("com.example.androiddemo.Activity.FridaActivity3");
        
        //静态成员变量可以直接设置结果
        Frida3.static_bool_var.value = true;
        console.log("After set new value 1:"+Frida3.static_bool_var.value);

        //动态成员变量需要找到实例，给实例设置结果；
        Java.choose("com.example.androiddemo.Activity.FridaActivity3",{
            onMatch:function(instance){
                instance.bool_var.value = true ;
                console.log("After set new value 2:"+instance.bool_var.value);
                instance._same_name_bool_var.value = true ;
                console.log("After set new value 3:"+instance._same_name_bool_var.value);
            },onComplete:function(){}
        })

    })
}
//         public static boolean check1() {
//     return false;
// }
// function challenge4(){
//     Java.perform(function(){
//         // com.example.androiddemo.Activity.FridaActivity4
//     //     var frida4 = Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses");
        
//     //     frida4.check1.implementation = function(){return true;}
//     //     frida4.check2.implementation = function(){return true;}
//     //     frida4.check3.implementation = function(){return true;}
//     //     frida4.check4.implementation = function(){return true;}
//     //     frida4.check5.implementation = function(){return true;}
//     //     frida4.check6.implementation = function(){
//     //         console.log("enter check6");
//     //         return true;}
//     // 
//         //内部类
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check1.implementation = function(){return true;}
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check2.implementation = function(){return true;}
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check3.implementation = function(){return true;}
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check4.implementation = function(){return true;}
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check5.implementation = function(){return true;}
//         Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check6.implementation = function(){
//             console.log("enter check6")
//             return true;
//         }
//     })
// }
function challenge4(){
    Java.perform(function(){
        //内部类
        console.log("enter start");
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check1.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check2.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check3.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check4.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check5.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check6.implementation = function(){
            console.log("enter check6");
            return true;
        }
        console.log("enter end")
    })

}

function challenge4_2(){
    Java.perform(function(){
        var class_name = "com.example.androiddemo.Activity.FridaActivity4$InnerClasses";
        // 内部类
        var InnerClass = Java.use(class_name);
        //java的反射获取所以的方法，是java的api 获取公告的方法
        var all_methods = InnerClass.class.getDeclaredMethods();
        // 打印所以内部类的所以方法
        console.log(all_methods);
        // for循环所以的方法
        for(var i = 0;i<all_methods.length;i++){
            var method = all_methods[i];
            console.log(method);
            // 方法变成字符串
            var methodStr = method.toString();
            // 方法字符串substr字符串截取(方法字符串，indexOf查找字符串类名称，+类名长度+1，如果，不加入+class_name.length+1
            var substring = methodStr.substr(methodStr.indexOf(class_name)+class_name.length+1);
            // 字符串截取，从下标0开始，查找到字符串
            var finalMethodString = substring.substr(0,substring.indexOf("("));
            console.log(finalMethodString);
            InnerClass[finalMethodString].implementation = function(){return true};
        }
    })
}

function challenge5(){
    Java.perform(function () {
        Java.choose("")
        })
}
setImmediate(challenge4_2);
