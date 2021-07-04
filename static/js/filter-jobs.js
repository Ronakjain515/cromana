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
    var part = $("#parttime").prop('checked')
    if (part){
        param += "&parttime=true";
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
    if (_search != "" && _search != " "){
        window.location.href = url + "?search=" + _search;
    }
}

