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
});