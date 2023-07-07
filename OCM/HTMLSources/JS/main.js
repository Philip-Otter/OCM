//  ||======================================||
//  || Copyright 2023 Philip Otter          ||
//  ||                                      ||
//  || Handles the main page interactions   ||
//  ||======================================||

console.log("LOADED main.js");

// Import port and host values
const port = document.getElementById("port").innerHTML;
console.log("Port value loaded as:  "+port);
const host = document.getElementById("host").innerHTML;
console.log("Host value loaded as:  "+host);
// Generate application address
const baseURL = "http://"+host+":"+port+"/";
console.log("Base URL set as:  "+baseURL);


// Clicking the load button
const  loadButton = document.getElementById("loadButton");
loadButton.addEventListener("click", load_button);

function load_button() {
    console.log('"Load" button clicked');
    let xhrPost = new XMLHttpRequest();
    xhrPost.open("POST", baseURL, true);
    xhrPost.setRequestHeader("Content-type", "application/json");
    let data = {
        "Action":"load"
    };
    xhrPost.onload = () => console.log(xhrPost.status);
    xhrPost.send(JSON.stringify(data));
};
