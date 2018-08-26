$(function () {
    $("form").submit(function () {
        var uname = $("#name_id").val();
        var pwd = $("#pwd_id").val();
        var c_pwd = $("#c_pwd_id").val();

        // 验证用户名
        if (uname.length < 3){
            alert("用户名过短");
            return false;
        }

        // 判断密码长度
        if (pwd.length<3){
            alert("密码过短")
            return false;
        }

        // 判断密码和确认密码
        if (pwd != c_pwd){
            alert("两次密码输入不一致");
            return false;
        }

        // 通过校验后  加密密码和确认密码
        var pwd_md5 = md5(pwd);
        var c_pwd_md5 = md5(c_pwd);

        // 将加密的值设置回去
        $("#pwd_id").val(pwd_md5);
        $("#c_pwd_id").val(c_pwd_md5);



    })
})

// // 验证用户名
// function myFunction() {
//     // 验证用户名
//     var uname = $("#name_id").val();
//     if (uname.length <= 3){
//         alert("用户名必须大于3位");
//         return false;//用户名不合法，返回，代码不往下运行，暂时不验证其他输入项，表单不能提交
//     }
// }
//
// // 密码
// function password() {
//     var pwd = $("#pwd_id").val();
//     if (pwd <= 3){
//         alert("密码不能低于3位数")
//     }
// }
//
// // 验证密码
// function conpwd() {
//     var pwd = $("#pwd_id").val();
//     var c_pwd = $("#c_pwd_id").val();
//     if(pwd == c_pwd){
//         $("#pwd_id").val(md5(pwd));
//         $("#c_pwd_id").val(md5(pwd_confirm));
//     }else {
//         alert("密码和确认密码必须一致");
//         return false;
//     }
// }
//
// // 验证邮箱
// function email(){
//     var email = $("#email_id").val();
//     if(email<=3){
//         alert("请输入正确的邮箱");
//     }
//
// }