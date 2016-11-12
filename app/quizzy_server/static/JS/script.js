
$(document).ready(function(){
    var code_mirrors = [];
    console.log("Initializing...");
    $(".free_response textarea").each(function(i, obj)
    {
        console.log("Adding text area: " + obj.name);
        code_mirrors.push(CodeMirror.fromTextArea(obj));
    });
});