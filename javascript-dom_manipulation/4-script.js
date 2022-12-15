document.getElementById("add_item").onclick = function() {
    let element = document.querySelector("ul");
    element.innerHTML = element.innerHTML + "\n" + "<li>Item</li>"
}