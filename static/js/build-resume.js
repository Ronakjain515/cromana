function personalDetails(){
    var first_name = $("#first-name-input").val();
    console.log(first_name);
}

$( "#first-name-input" ).keyup(function() {
    var name = $( "#first-name-input" ).val();
    if(name.length  <= 15){
        $("#first-name-out").text(name);
    } 
});
$( "#last-name-input" ).keyup(function() {
    var name = $( "#last-name-input" ).val();
    if(name.length  <= 15){
        $("#last-name-out").text(name);
    } 
});
$( "#birth-date-input" ).change(function() {
    $("#birth-date-out").text($( "#birth-date-input" ).val());
});
$( "#marital-status-input" ).change(function() {
    $("#marital-status-out").text($( "#marital-status-input" ).val());
});
$( "#linguistic-input" ).change(function() {
    var selected = [];
    for (var option of document.getElementById("linguistic-input").options)
    {
        if (option.selected) {
            selected.push(option.text);
        }
    }
    $("#linguistic-out").text(selected.join(", "));
});
$( "#contact-number-input" ).keyup(function() {
    $("#contact-number-out").text($( "#contact-number-input" ).val());
});
$( "#email-input" ).keyup(function() {
    $("#email-out").text($( "#email-input" ).val());
});
$( "#resume-headline-input" ).keyup(function() {
    $("#resume-headline-out").text($( "#resume-headline-input" ).val());
});
$( "#key-skills-input" ).change(function() {
    var selected = "";
    for (var option of document.getElementById("key-skills-input").options)
    {
        if (option.selected) {
            selected = selected + "<div class='col-6 key-skill-col'>&#8226; " + option.text + "</div>";
        }
    }
    $("#key-skill-out-div").html(selected);
    console.log("ss")
});
