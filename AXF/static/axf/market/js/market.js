var type_down = true;
var sort_down = true;

$(function () {
    $("#all_types").click(all_type_even);
    $("#c_control").click(all_type_even);
    $("#all_sort").click(all_sort_even);
    $("#s_control").click(all_sort_even);

    // 加按钮添加点击事件
    $(".addShopping").click(function () {
        // 拿到商品
        var g_id = $(this).attr("g_id");
        var $current_btn = $(this);
        $.ajax({
            url:"/axf/cartapi",
            data:{
                g_id:g_id,
                op_type:"add"
            },
            method:"post",
            success:function (res) {
                // 修改商品的数量
                // console.log(res)
                if(res.code == 2){
                    window.open(res.data,target="_self");
                }else if(res.code == 1){
                    // 操作成功，需要更新商品数量
                    $current_btn.prev().html(res.data);
                }else {
                    alert(res.msg);
                }
            },
            error:function () {
                alert("请求失败")
            }
        })
    });

    $(".subShopping").click(function () {
        // 拿到商品
        var g_id = $(this).attr("g_id");
        var $current_btn = $(this);
        var current_num = $current_btn.next().html();
        // 判断如果当前数量都是0了  那就不发送请求了
        if (current_num == 0){
            return;
        }
        $.ajax({
            url:"/axf/cartapi",
            data:{
                g_id:g_id,
                on_type: "sub"
            },
            method:"post",
            success:function (res) {
                // 修改商品的数量
                if (res.code == 2){
                    window.open(res.data,target="_self");
                }else if(res.code == 1){
                    // 操作成功，需要更新商品数量
                    $current_btn.next().html(res.data);
                }else {
                    alert(res.msg);
                }
            },
            error:function () {
                alert("请求失败")
            }
        })
    });

})

function all_type_even() {
    // 状态取反
    $("#c_control").toggle();
    var type_span = $("#all_types").find("span").find("span");
    if (type_down == true){
        // 如果向上则修改
        type_span.removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        type_down = false;
    }else {
        type_span.removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        type_down = true;
    }
}


function all_sort_even() {
    // 状态取反
    $("#s_control").toggle();
    var type_span = $("#sort_down").find("span").find("span");
    if (sort_down == true){
        // 如果向上则修改
        type_span.removeClass("glyphicon glyphicon-chevron-down").addClass("glyphicon glyphicon-chevron-up");
        sort_down = false;
    }else {
        type_span.removeClass("glyphicon glyphicon-chevron-up").addClass("glyphicon glyphicon-chevron-down");
        sort_down = true;
    }
}
