$('#InputEmail').on('input', function() {

    if ($('#InputEmail').val() == ""){

        $("#InputEmail").removeClass("is-valid");
        $("#InputEmail").addClass("is-invalid");
        $("#emailHelp").text("Email field can not empty");
    }
    else if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test($('#InputEmail').val())){
        
        $("#InputEmail").removeClass("is-invalid");
        $("#InputEmail").addClass("is-valid");
        $("#emailHelp").text("");
    }
    else if (!(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test($('#InputEmail').val()))){
        $("#InputEmail").removeClass("is-valid");
        $("#InputEmail").addClass("is-invalid");
        $("#emailHelp").text("Please enter valid Email");
    }
    loginButton();
});

$('#InputPassword').on('input', function() {
    if ($('#InputPassword').val() == ""){
        $("#InputPassword").removeClass("is-valid");
        $("#InputPassword").addClass("is-invalid");
        $("#passwordHelp").text("Password field can not empty");
    }
    if ($('#InputPassword').val() != ""){
        $("#InputPassword").removeClass("is-invalid");
        $("#passwordHelp").text("");
    }
    loginButton();
});


function loginButton(){

    if($("#passwordHelp").text() == "" && $("#emailHelp").text() == ""){
        $('#loginButton').prop('disabled', false);
    }
    else{
        $('#loginButton').prop('disabled', true);
    }
}