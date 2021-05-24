$(document).ready(function(){
    // Prepare the preview for profile picture
    $("#logo").change(function(){
        showPreviewImage(this);
        checkLogo();
        registerButton();
    });
});
function showPreviewImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#wizardPicturePreview').attr('src', e.target.result).fadeIn('slow');
        }
        reader.readAsDataURL(input.files[0]);
    }
}

$('#InputCompanyName').on('input', function() {
    checkCompanyName();
    registerButton();
});
$('#InputCompanyRegisNo').on('input', function() {
    checkRegisNo();
    registerButton();
});
$('#InputMobile').on('input', function() {
    checkMobileNo();
    registerButton();
});
$('#InputSecMobile').on('input', function() {
    checkSecMobileNo();
    registerButton();
});
$('#InputAddress').on('input', function() {
    checkAddress();
    registerButton();
});
$('#InputFirstName').on('input', function() {
    checkFirstName();
    registerButton();
});
$('#InputLastName').on('input', function() {
    checkLastName();
    registerButton();
});
$('#InputGender').on('input', function() {
    checkGender();
    registerButton();
});

function registerButton(){
    if (!$("#InputCompanyName").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    console.log("done");
    if (!$("#InputCompanyRegisNo").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputMobile").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if ($("#InputSecMobile").hasClass("is-invalid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputAddress").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputFirstName").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputLastName").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }
    if (!$("#InputGender").hasClass("valid")){
        $('#registerButton').prop('disabled', true);
        return;
    }

    $('#registerButton').prop('disabled', false);
}


function checkLogo(){
    logo = $("#logo");
    FileUploadPath = logo.val();
    Extension = FileUploadPath.substring(FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
    
    if (FileUploadPath == ""){
        logo.removeClass("valid");
        logo.addClass("is-invalid");
        $("#logoHelp").text("Logo can not be Empty");
    }
    else if (!(Extension == "png" || Extension == "bmp" || Extension == "jpeg" || Extension == "jpg")){
        logo.removeClass("valid");
        logo.addClass("is-invalid");
        $("#logoHelp").text("Invalid Format");
    }
    else{
        logo.addClass("valid");
        logo.removeClass("is-invalid");
        $("#logoHelp").text("");
    }
}
function checkCompanyName(){
    companyname = $("#InputCompanyName");
    if (companyname.val() == ""){
        companyname.removeClass("valid");
        companyname.addClass("is-invalid");
        $("#companyNameHelp").text("Company Name can not be Empty");
    }
    else{
        companyname.addClass("valid");
        companyname.removeClass("is-invalid");
        $("#companyNameHelp").text("");
    }
}
function checkRegisNo(){
    regisno = $("#InputCompanyRegisNo");
    if (regisno.val() == ""){
        regisno.removeClass("valid");
        regisno.addClass("is-invalid");
        $("#companyRegisNoHelp").text("Registration number can not be Empty");
    }
    else if (regisno.val().match(/\s/)){
        regisno.removeClass("valid");
        regisno.addClass("is-invalid");
        $("#companyRegisNoHelp").text("Space are not allowed");
    }
    else{
        regisno.addClass("valid");
        regisno.removeClass("is-invalid");
        $("#companyRegisNoHelp").text("");
    }
}
function checkMobileNo(){
    mobileno = $("#InputMobile");
    mobilenosplit = mobileno.val().split(" ");
    if (mobileno.val() == ""){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. can not be Empty");
    }
    else if (mobilenosplit.length != 2){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should be in proper format");
    }
    else if (!mobilenosplit[1].match(/^[0-9]+$/)){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should Contains only Digits");
    }
    else if (mobilenosplit[1].length != 10){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#mobileHelp").text("Mobile No. Should Contains 10 Digits");
    }
    else {
        mobileno.removeClass("is-invalid");
        mobileno.addClass("valid");
        $("#mobileHelp").text("");
    }
}
function checkSecMobileNo(){
    mobileno = $("#InputSecMobile");
    mobilenosplit = mobileno.val().split(" ");
    if (mobilenosplit.length != 2){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#secMobileHelp").text("Mobile No. Should be in proper format");
    }
    else if (mobilenosplit[1] == ""){
        mobileno.removeClass("is-invalid");
        mobileno.addClass("valid");
        $("#secMobileHelp").text("");
    }
    else if (!mobilenosplit[1].match(/^[0-9]+$/)){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#secMobileHelp").text("Mobile No. Should Contains only Digits");
    }
    else if (mobilenosplit[1].length != 10){
        mobileno.removeClass("valid");
        mobileno.addClass("is-invalid");
        $("#secMobileHelp").text("Mobile No. Should Contains 10 Digits");
    }
    else {
        mobileno.removeClass("is-invalid");
        mobileno.addClass("valid");
        $("#secMobileHelp").text("");
    }
}
function checkAddress(){
    regisno = $("#InputAddress");
    if (regisno.val() == ""){
        regisno.removeClass("valid");
        regisno.addClass("is-invalid");
        $("#addressHelp").text("Address can not be Empty");
    }
    else{
        regisno.addClass("valid");
        regisno.removeClass("is-invalid");
        $("#addressHelp").text("");
    }
}
function checkFirstName(){
    firstname = $("#InputFirstName");
    if (firstname.val() == ""){
        firstname.removeClass("valid");
        firstname.addClass("is-invalid");
        $("#firstHelp").text("First Name can not be Empty");
    }
    else if (!(firstname.val().match(/^[A-Za-z]+$/))){
        firstname.removeClass("valid");
        firstname.addClass("is-invalid");
        $("#firstHelp").text("Please Enter only Letters");
    }
    else{
        firstname.addClass("valid");
        firstname.removeClass("is-invalid");
        $("#firstHelp").text("");
    }
}
function checkLastName(){
    firstname = $("#InputLastName");
    if (firstname.val() == ""){
        firstname.removeClass("valid");
        firstname.addClass("is-invalid");
        $("#lastHelp").text("Last Name can not be Empty");
    }
    else if (!(firstname.val().match(/^[A-Za-z]+$/))){
        firstname.removeClass("valid");
        firstname.addClass("is-invalid");
        $("#lastHelp").text("Please Enter only Letters");
    }
    else{
        firstname.addClass("valid");
        firstname.removeClass("is-invalid");
        $("#lastHelp").text("");
    }
}
function checkGender(){
    gender = $("#InputGender");
    if(gender.val() == ""){
        gender.removeClass("valid");
        gender.addClass("is-invalid");
        $("#genderHelp").text("Please Select Gender");
    }
    else{
        gender.removeClass("is-invalid");
        gender.addClass("valid");
        $("#genderHelp").text("");
    }
}
