
$(document).ready(function(){
    var code_mirrors = [];
    console.log("Initializing...");
    $(".free_response textarea").each(function(i, obj)
    {
        console.log("Adding text area: " + obj.name + " of language " + language);
        var mirror = CodeMirror.fromTextArea(obj, {mode: {name: language}, lineNumbers: true});
        code_mirrors.push(mirror);
    });
});