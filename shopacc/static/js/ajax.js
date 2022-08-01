$(document).ready(function(){
    $("#addCart").click(function (e) { 
        var accname = $("#accname").text();
        var number = parseInt($(".checkout_items").text());
        $.post("http://127.0.0.1:8000/ajax/", 
        {accname: accname, csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()}, 
        function(result){
            if(result == "True"){
                number += 1;
                $(".checkout_items").text(number);
                alert("Thêm vào giỏ hành thành công!")
            }

            if(result == "isset"){
                alert("Sản phẩm đã có trong giỏ hàng!")
            }

            if(result == "False"){
                alert("Có lỗi khi thêm sản phẩm vào giỏ hàng!")
            }
        });
    });

    $(".deleteProduct").click(function (e) { 
        var id = $(this).attr('value')
        var number = parseInt($(".checkout_items").text());
        $.post("http://127.0.0.1:8000/ajax/", 
        {id: id, csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()}, 
        function(result){
            if(result != "False"){
                $("#"+ id +"").remove()
                number -= 1;
                $("#number-product").text(number)
                $("#total-product").text(result)
                $(".checkout_items").text(number)
                alert("Đã xóa tài khoản khỏi giỏ hàng!")
            }

            if(result == "False"){
                alert("Có lỗi khi xóa tài khoản khỏi giỏ hàng!")
            }
        });
    });

});