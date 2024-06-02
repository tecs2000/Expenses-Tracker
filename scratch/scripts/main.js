/**
 * The following code alters the image from ouroboros to anya's face when clicked on it
 */

const myImage = document.querySelector("img");

myImage.onclick = function () {
    const mySrc = myImage.getAttribute("src");

    if (mySrc === "images/ouroboros.png") {
        myImage.setAttribute("src", "images/anya.png");
    }
    else {
        myImage.setAttribute("src", "images/ouroboros.png");
    }
}


/**
 * Retriever the user's name to create a personalized
 * welcome message. Save the data in the local storage.
 */
let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");

function setUserName() {
    const username = prompt("Please enter your name");

    if (!username) {
        setUserName();
    }

    else {
        localStorage.setItem("name", username);
        myHeading.textContent = `Welcome to my page, ${username}!`;
    }
}

if (!localStorage.getItem("name")) {
    myHeading.textContent = `Welcome to my page, stranger!`;
}
else {
    const storedUsername = localStorage.getItem("name");
    myHeading.textContent = `Welcome to my page, ${storedUsername}!`;
}

myButton.onclick = function () {
    setUserName();
}