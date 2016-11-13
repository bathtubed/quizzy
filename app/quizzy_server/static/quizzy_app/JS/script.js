
$(document).ready(function(){
    var code_mirrors = [];
    console.log("Initializing...");
    $(".free_response textarea").each(function(i, obj)
    {
        console.log("Adding text area: " + obj.name + " of language " + language);
        var mirror = CodeMirror.fromTextArea(obj, {mode: {name: language}, lineNumbers: true});
        mirror.on("change", function(instance, changeObj)
        {
            console.log("Updating qustion " + instance.getInputField().name);
            $.ajax("/quizzy_app", {
                "examID": examID,
                "questionID": instance.getInputField().name,
                "answer": instance.getValue()
            }).done(function(data, textStatus, jqXHR)
            {
                console.log("Update returned with " + textStatus);
            });
        });
        code_mirrors.push(mirror);
    });
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