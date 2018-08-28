$(function () {
    $(".confirm").click(function () {
        var $current_bth = $(this);
        var c_id = $current_bth.parents("li").attr("c_id");
        // console.log(c_id)
        $.ajax({
            url:"/axf/cart_status",
            method:"put",
            data:{
                c_id:c_id
            },
            success:function (res) {
                // console.log(res);
                if (res.code == 1){
                    // 第一个要改当前商品的选中状态
                    if (res.current_item_status){
                        $current_bth.find("span").find("span").html("√");
                    }else {
                        $current_bth.find("span").find("span").html("");
                    }
                    // 改总价
                    $("#money").html(res.sum_money);
                    // 全选按钮的状态
                    if(res.is_select_all){
                        $(".all_select>span>span").html("√");
                    }else {
                        $(".all_select>span>span").html("");
                    }
                }else {
                    alert(res.msg);
                }
            }
        })
    });

    $(".all_select").click(click_all_select);

    $(".subBtn").click(sub_item_num);

    $(".addBtn").click(add_item_num);
})

function click_all_select() {
    $.ajax({
        url:"/axf/select_all_api",
        data:{},
        method:"put",
        success:function (res) {
            console.log(res);
            if (res.code == 1){
                // 修改全部商品的状态

                // 全选按钮状态
                if (res.data.is_select_all){
                    $(".all_select>span>span").html("√");
                    $(".confirm").each(function () {
                        $(this).find("span").find("span").html("√");
                    })
                }else {
                    $(".all_select>span>span").html("");
                    $(".confirm").each(function () {
                        $(this).find("span").find("span").html("");
                    })
                }
                // 总价
                $("#money").html(res.data.sum_money);
            }
        }
    })
}

function sub_item_num() {
    var $current_btn = $(this);
    var c_id = $current_btn.parents("li").attr("c_id");
    $.ajax({
        url:"/axf/cartitem_api",
        data:{
            c_id:c_id,
            op_type:"sub"
        },
        method:"post",
        success:function (res) {
            // console.log(res);
            if (res.code == 1){
                // 更新总价
                $("#money").html(res.data.sum_money)
                // 更新商品数量
                if (res.data.item_num == 0){
                    // 是0则修改标签
                    $current_btn.parents("li").remove();
                    if (res.data.is_select_all){
                        // 修改全选按钮
                        $(".all_select>span>span").html("√")
                    }
                }else {
                    // 不是0,则减数量
                    $current_btn.next().html(res.data.item_num)
                }
            }else {
                alert(res.msg)
            }
        },
        error:function () {
            alert("请求失败")
        }
    })
}

function add_item_num() {
    var $current_btn = $(this)
    var c_id = $current_btn.parents("li").attr("c_id");
    $.ajax({
        url:"/axf/cartitem_api",
        data:{
            c_id:c_id,
            op_type:"add"
        },
        method:"post",
        success:function (res) {
            // console.log(res);
            if (res.code == 1){
                // 更新总价
                $("#money").html(res.data.sum_money)
                // 更新商品数量
                if (res.data.item_num == 0){
                    // 是0则修改标签
                    $current_btn.parents("li").remove();
                }else {
                    // 不是0,则减数量
                    $current_btn.prev().html(res.data.item_num)
                }
            }else {
                alert(res.msg)
            }
        },
        error:function () {
            alert("请求失败")
        }
    })
}