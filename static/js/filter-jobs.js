function filter(url, pageno){
    // exp
    var Experience = $("#Experience :selected").val();
    param = "?"
    if (Experience != ""){
        param += ("exp=" + Experience);
    }

    // location
    var location = $('#searchLocation').val();
    if (location != ""){
        param += ("&location=" + location);
    }

    // Salary
    var Salary = $('#Salary').val();
    if (Salary != ""){
        param += ("&salary=" + Salary);
    }
    
    // part time
    var part = $("#parttime").val();
    if (part != ""){
        param += ("&type=" + part);
    }

    // Company
    var Company = $('#searchCompany').val();
    if (Company != ""){
        param += ("&company=" + Company.replace(" ", "-"));
    }

    // page no
    param += ("&page=" + pageno);

    window.location.href = url + param;

}

function search_job(url){
    _search = $("#search").val();
    _location = $("#locationinput").val();
    param = url;
    if (_search != "" && _search != " "){
        param = "?search=" + _search + "&";
    }
    else{
        param += "?";
    }
    if (_location != "" && _location != " "){
        param = param + "location=" + _location;
    }
    window.location.href= param;
}