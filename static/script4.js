var form = document.getElementById("formAgendamento");
var hemocentro = document.getElementById("hemocentro");
var data = document.getElementById("data");
var horario = document.getElementById("horario");
var observacao = document.getElementById("observacao");


var erroHemocentro = document.getElementById("erroHemocentro");
var erroData = document.getElementById("erroData");
var erroHorario = document.getElementById("erroHorario");

form.onsubmit = function (event) {

    erroHemocentro.innerHTML = "";
    erroData.innerHTML = "";
    erroHorario.innerHTML = "";

    var valido = true;


    if (hemocentro.value === "") {
        erroHemocentro.innerHTML = "Por favor, escolha um hemocentro.";
        valido = false;
    }

    else if (data.value === "") {
        erroData.innerHTML = "Por favor, escolha uma data.";
        valido = false;
    }
    else {
        var hoje = new Date();
        var dataEscolhida = new Date(data.value);


        if (dataEscolhida < hoje.setHours(0, 0, 0, 0)) {
            erroData.innerHTML = "A data não pode ser no passado.";
            valido = false;
        }
    }

    if (valido) {
        if (horario.value === "") {
            erroHorario.innerHTML = "Por favor, escolha um horário.";
            valido = false;
        }
    }

    if (valido) {
        if (observacao.value.length > 500) {
            alert("A observação não pode ter mais de 500 caracteres.");
            valido = false;
        }
    }


    if (!valido) {
        event.preventDefault();
    }
};


