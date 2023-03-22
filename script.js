function submitQuestion() {
    var userinput = document.getElementById("userinput").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/chat");
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        var chatlog = document.getElementById("chatlog");
        chatlog.innerHTML += "<
