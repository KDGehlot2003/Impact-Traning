const heading = document.getElementById("heading");
const updateButton = document.getElementById("updateButton");

updateButton.addEventListener("click", () => {
    if (heading.innerText === heading.innerText.toLowerCase()){
        heading.innerText = heading.innerText.toUpperCase();
    } else {
        heading.innerText = heading.innerText.toLowerCase();
    }
})
