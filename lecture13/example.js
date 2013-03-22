function init() {
    var div = document.getElementById("clickable");
    div.innerHTML = "<b>Changed by the script</b>";

    div.addEventListener("click", doStuff);
}

function doStuff(e) {
    e.target.innerHTML = "clicked!";
    console.log(e);
}

window.addEventListener("load", init);
