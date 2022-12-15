document.getElementById("toggle_header").onclick = function() {
    let element = document.querySelector("header");
    if (element.classList.contains("red")) {
        element.classList.add("green");
        element.classList.remove("red");
    } else if (element.classList.contains("green")) {
        element.classList.add("red");
        element.classList.remove("green");
    }
}