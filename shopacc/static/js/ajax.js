$(document).ready(function(){
    $("#addCart").click(function (e) {
        var accName = $(".accname").text()
        var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/ajax/",
            data: {
                accName: accName,
                csrfmiddlewaretoken:csrftoken
            },
            cache: true,
            success: function (data, status) {
                console.log(data)
            }
        });
    });
});