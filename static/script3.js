document.querySelector("form").onsubmit = function(event) {
    var email = document.getElementById("email");
    var senha = document.getElementById("senha");
    var valido = true;

    if (email.value === "") {
        alert("Por favor, preencha o e-mail.");
        valido = false;
    }

    if (senha.value === "") {
        alert("Por favor, preencha a senha.");
        valido = false;
    }

    if (!valido) {
        event.preventDefault();
    }
};
