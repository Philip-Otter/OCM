//  ||======================================||
//  || Copyright 2023 Philip Otter          ||
//  ||                                      ||
//  || Handles the main page interactions   ||
//  ||======================================||

console.log("LOADED main.js");

// Import localhost port
const port = document.getElementById("port").innerHTML;
console.log("port value loaded as:"+port);


// Clicking the load button
const  loadButton = document.getElementById("loadButton");
loadButton.addEventListener("click", post_button);

function post_button() {
    var xhrPost = new XMLHttpRequest();
    xhrPost.open("POST", localhost)
}
