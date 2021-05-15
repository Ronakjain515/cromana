$('#InputFirstName').on('input', function() {
    checkFirstName();
    registerButton();
});
$('#InputLastName').on('input', function() {
    checkLastName();
    registerButton();
});
$('#InputEmail').on('input', function() {
    checkEmail();
    registerButton();
});
$('#InputMobile').on('input', function() {
    checkMobileNo();
    registerButton();
});
$('#InputGender').on('input', function() {
    checkGender();
    registerButton();
});
$('#InputPassword').on('input', function() {
    checkPassword();
    registerButton();
});
$('#InputConformPassword').on('input', function() {
    checkConformPassword();
    registerButton();
});

function registerButton(){
    if (!$("#InputFirstName").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputLastName").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputEmail").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputMobile").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputGender").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputPassword").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputConformPassword").hasClass("is-valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    $('#registerButton').prop('disabled', false);
}

function checkFirstName(){
    firstname = $("#InputFirstName");
    if (firstname.val() == ""){
        firstname.removeClass("is-valid");
        firstname.addClass("is-invalid");
        $("#firstHelp").text("First Name can not be Empty");
    }
    else if (!(firstname.val().match(/^[A-Za-z]+$/))){
        firstname.removeClass("is-valid");
        firstname.addClass("is-invalid");
        $("#firstHelp").text("Please Enter only Letters");
    }
    else{
        firstname.addClass("is-valid");
        firstname.removeClass("is-invalid");
        $("#firstHelp").text("");
    }
}
function checkLastName(){
    firstname = $("#InputLastName");
    if (firstname.val() == ""){
        firstname.removeClass("is-valid");
        firstname.addClass("is-invalid");
        $("#lastHelp").text("Last Name can not be Empty");
    }
    else if (!(firstname.val().match(/^[A-Za-z]+$/))){
        firstname.removeClass("is-valid");
        firstname.addClass("is-invalid");
        $("#lastHelp").text("Please Enter only Letters");
    }
    else{
        firstname.addClass("is-valid");
        firstname.removeClass("is-invalid");
        $("#lastHelp").text("");
    }
}

function checkEmail(){
    email = $("#InputEmail");
    if (email.val() == ""){

        email.removeClass("is-valid");
        email.addClass("is-invalid");
        $("#emailHelp").text("Email field can not be Empty");
    }
    else if (!(email.val().match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/))){
        email.removeClass("is-valid");
        email.addClass("is-invalid");
        $("#emailHelp").text("Please enter valid Email");
    }
    else {
        email.removeClass("is-invalid");
        email.addClass("is-valid");
        $("#emailHelp").text("");
    }
}
function checkMobileNo(){
    mobileno = $("#InputMobile");
    mobilenosplit = mobileno.val().split(" ");
    if (mobileno.val() == ""){
        mobileno.removeClass("is-valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. can not be Empty");
    }
    else if (mobilenosplit.length != 2){
        mobileno.removeClass("is-valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should be in proper format");
    }
    else if (!mobilenosplit[1].match(/^[0-9]+$/)){
        mobileno.removeClass("is-valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should Contains only Digits");
    }
    else if (mobilenosplit[1].length != 10){
        mobileno.removeClass("is-valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should Contains 10 Digits");
    }
    else {
        mobileno.removeClass("is-invalid");
        mobileno.addClass("is-valid");
        $("#mobileHelp").text("");
    }
}
function checkGender(){
    gender = $("#InputGender");
    if(gender.val() == ""){
        gender.removeClass("is-valid");
        gender.addClass("is-invalid");
        $("#genderHelp").text("Please Select Gender");
    }
    else{
        gender.removeClass("is-invalid");
        gender.addClass("is-valid");
        $("#genderHelp").text("");
    }
}
function checkPassword(){
    password = $("#InputPassword");
    if (password.val() == ""){
        password.removeClass("is-valid");
        password.addClass("is-invalid");
        $("#passwordHelp").text("Password can not be Empty");
    }
    else if (!password.val().match( /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/)){
        password.removeClass("is-valid");
        password.addClass("is-invalid");
        $("#passwordHelp").text("Password Should Contains atleast 1 letter and 1 special character");
    }
    else{
        password.removeClass("is-invalid");
        password.addClass("is-valid");
        $("#passwordHelp").text("");
    }
}
function checkConformPassword(){
    conformpassword = $("#InputConformPassword");
    if (conformpassword.val() != $("#InputPassword").val()){
        conformpassword.removeClass("is-valid");
        conformpassword.addClass("is-invalid");
        $("#conformPasswordHelp").text("Conform password should be same password");
    }
    else {
        conformpassword.removeClass("is-invalid");
        conformpassword.addClass("is-valid");
        $("#conformPasswordHelp").text("");
    }
}