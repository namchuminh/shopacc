$(document).ready(function(){
    $("#addCart").click(function (e) { 
        $.get("http://127.0.0.1:8000/ajax/", function(data, status){
            if(data.addCart == true){
                alert("Sản phẩm đã có trong giỏ hàng!")
            }else{
                var number = data.number
                number += 1
                $(".checkout_items").text(number)
            }
        }); 
    });
});