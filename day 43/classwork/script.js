document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    console.log("name:", name);
    console.log("email:", email);
    console.log("password:", password);
});

document.getElementById("userForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let formData = new FormData(event.target);

    console.log("name:", formData.get("name"));
    console.log("email:", formData.get("email"));
    console.log("password:", formData.get("password"));
});
