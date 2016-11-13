$(document).ready(function(){
    var code_mirrors = [];
    console.log("Initializing...");
    $(".free_response textarea").each(function(i, obj)
    {
        console.log("Adding text area: " + obj.name + " of language " + language);
        var mirror = CodeMirror.fromTextArea(obj, {mode: {name: language}, lineNumbers: true});
        mirror.on("change", function(instance, changeObj)
        {
            console.log("Updating question " + obj.name);
            $.ajax("/quizzy_app/", {
                method: "POST",
                data: {
                    examID: examID,
                    questionID: obj.name,
                    answer: instance.getValue()
                }
            }).always(function(data_or_jqXHR, textStatus, jqXHR_or_error)
            {
                console.log("Update returned with " + textStatus + ":");
                if(textStatus != "error")
                {
                    obj.parentElement.nextElementSibling.innerHTML = jqXHR_or_error.responseText;
                    console.log(jqXHR_or_error.responseText);
                }
                else
                {
                    console.log(data_or_jqXHR.responseText);
                }
            });
        });
        code_mirrors.push(mirror);
    });
});


// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*
var update_question = function(elem)
{
    console.log("Updating " + elem.name);
    $.ajax("quizzy_app", {
        "examID": examID,
        "questionID": elem.name,
        "answer": elem.
    }).done(function(data, textStatus, jqXHR)
    {
        console.log("Update returned with " + textStatus);
    });
    
};
*/