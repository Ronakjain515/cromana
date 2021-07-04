function job_apply(job_id, url){
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify({
            "job": job_id
        }),
        success: function (data){
            if (data.result == "Done"){
                alert("you have successfully applied for this job.");
                $("#apply_button_" + job_id).html("Applied");
                $("#apply_button_" + job_id).prop('disabled', true);
            }
            else if(data.result == "Not"){
                alert("Please login to apply.");
            }
            else if(data.result == "Already"){
                alert("you have already applied for this job.");
            }
            else if(data.result == "permi"){
                alert("Company can not apply for jobs.");
            }
        },
        contentType: 'application/json',
    });
}
function job_saved(job_id, url){
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify({
            "job": job_id
        }),
        success: function (data){
            if (data.result == "Done"){
                alert("you have successfully Saved this job.");
                $("#saved_button_" + job_id).html("Saved");
                $("#saved_button_" + job_id).prop('disabled', true);
            }
            else if(data.result == "Not"){
                alert("Please login to Save.");
            }
            else if(data.result == "Already"){
                alert("you have already Saved this job.");
            }
            else if(data.result == "permi"){
                alert("Company can not save jobs.");
            }
        },
        contentType: 'application/json',
    });
}

$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});