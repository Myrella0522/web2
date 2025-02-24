        var form = document.getElementById("form");
        var nome = document.getElementById("nome");
        var idade = document.getElementById("idade");
        var tipo_sanguineo = document.getElementById("tipo_sanguineo");
        var email = document.getElementById("email");
        var senha = document.getElementById("senha");
        var senha2 = document.getElementById("senha2");

        var erroNome = document.getElementById("erroNome");
        var erroIdade = document.getElementById("erroIdade");
        var erroTipoSanguineo = document.getElementById("erroTipoSanguineo");
        var erroEmail = document.getElementById("erroEmail");
        var erroSenha = document.getElementById("erroSenha");
        var erroSenha2 = document.getElementById("erroSenha2");


        form.onsubmit = function(event) {

            erroNome.innerHTML = "";
            erroIdade.innerHTML = "";
            erroTipoSanguineo.innerHTML = "";
            erroEmail.innerHTML = "";
            erroSenha.innerHTML = "";
            erroSenha2.innerHTML = "";

            var valido = true;


            if (nome.value === "") {
                erroNome.innerHTML = "Por favor, preencha o seu nome completo.";
                valido = false;
            }else if (idade.value === "" || isNaN(idade.value) || idade.value < 16 || idade.value > 69) {
                erroIdade.innerHTML = "Você deve ter entre 16 e 69 anos para realizar a doação.";
                valido = false;
            }else if (tipo_sanguineo.value === "") {
                erroTipoSanguineo.innerHTML = "Por favor, selecione o tipo sanguíneo.";
                valido = false;
            }else if (email.value === "") {
                erroEmail.innerHTML = "Por favor, preencha o e-mail.";
                valido = false;
            }else if (senha.value === "") {
                erroSenha.innerHTML = "Por favor, preencha a senha.";
                valido = false;
            }else if (senha2.value === "") {
                erroSenha2.innerHTML = "Por favor, confirme a senha.";
                valido = false;
            }else if (senha.value !== senha2.value) {
                erroSenha2.innerHTML = "As senhas estão diferentes.";
                valido = false;
            }

            if (!valido) {
                event.preventDefault();
            }
        };







