
// se deja ocultos los errores de formulario
document.getElementById("error_rut").style.display = "none";
document.getElementById("error_nombre_min").style.display = "none";
document.getElementById("error_nombre_max").style.display = "none";
document.getElementById("error_apellido_min").style.display = "none";
document.getElementById("error_apellido_max").style.display = "none";
document.getElementById("error_nacimiento").style.display = "none";
document.getElementById("error_email").style.display = "none";
document.getElementById("error_password").style.display = "none";
document.getElementById("error_direccion").style.display = "none";
document.getElementById("error_comuna").style.display = "none";
document.getElementById("error_carrera").style.display = "none";
document.getElementById('mostrar_pass').style.display = 'inline';
document.getElementById('ocultar_pass').style.display = 'none';

// Aquí funciones de control de formulario
$("#txtRut").on("blur", function(){
    let rut = document.getElementById("txtRut").value;
    validarRut(rut);
})
$("#nombre").on("blur", function(){
    let nombre = document.getElementById("nombre").value;
    validarNombre(nombre);
})
$("#apellido").on("blur", function(){
    let apellido = document.getElementById("apellido").value;
    validarApellido(apellido);
})
$("#fecha_nac").on("blur", function(){
    let fechaNacimiento = document.getElementById("fecha_nac").value;
    validarFechaNacimiento(fechaNacimiento);
})
$("#email").on("blur", function(){
    let email = document.getElementById("email").value;
    validarEmail(email);
})
$("#password").on("blur", function(){
    let password = document.getElementById("password").value;
    validarPassword(password);
})

$("#direccion").on("blur", function(){
    let direccion = document.getElementById("direccion").value;
    validarDireccion(direccion);
})
$("#comuna").on("blur", function(){
    let comuna = document.getElementById("comuna").value;
    validarComuna(comuna);
})
$("#carrera").on("blur", function(){
    let carrera = document.getElementById("carrera").value;
    validarCarrera(carrera);
})

$("#btn-password").on("click", function(event){
    event.preventDefault();
    verPassword();
})


function validacionFormulario(){
    $("small").css('color', 'red');
    

    let rt = validarRut(rut);
    let nom = validarNombre(nombre);
    let apll = validarApellido(apellido);
    let fecnac = validarFechaNacimiento(fechaNacimiento);
    let em = validarEmail(email);
    let pass = validarPassword(password);
    let dir = validarDireccion(direccion);
    let com = validarComuna(comuna);
    let carr = validarCarrera(carrera);

    if (rt & nom & apll & fecnac & em & pass & dir & com & carr){
        return true;
    }
    return false;
}
// Aquí funciones de control de formulario


//FUNCIONES
function validarRut(rut){
    var Fn = {
        // Valida el rut con su cadena completa "XXXXXXXX-X"
        validaRut : function (rutCompleto) {
            rutCompleto = rutCompleto.replace("‐","-");
            if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
                    return false;
            var tmp 	= rutCompleto.split('-');
            var digv	= tmp[1]; 
            var rut 	= tmp[0];
            if ( digv == 'K' ) digv = 'k' ;
            
            return (Fn.dv(rut) == digv );
        },
        dv : function(T){
            var M=0,S=1;
            for(;T;T=Math.floor(T/10))
                    S=(S+T%10*(9-M++%6))%11;
            return S?S-1:'k';
        }
    } 
    
    if (Fn.validaRut(rut) == false) {
        document.getElementById("error_rut").style.display = "inline";
        document.getElementById("txtRut").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_rut").style.display = "none";
        document.getElementById("txtRut").classList.remove("is-invalid");
        document.getElementById("txtRut").classList.add("is-valid");
        return true;
    }
}

function validarNombre(nombre){
    if(nombre.trim().length <= 3){
        document.getElementById("error_nombre_min").style.display = "inline";
        document.getElementById("nombre").classList.add("is-invalid");
        return false;
    }else if(nombre.trim().length > 20){
        document.getElementById("error_nombre_min").style.display = "none";
        document.getElementById("error_nombre_max").style.display = "inline";
        document.getElementById("nombre").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_nombre_min").style.display = "none";
        document.getElementById("error_nombre_max").style.display = "none";
        document.getElementById("nombre").classList.remove("is-invalid");
        document.getElementById("nombre").classList.add("is-valid");
        return true;
    }   
}

function validarApellido(apellido){
    if(apellido.trim().length <= 3){
        document.getElementById("error_apellido_min").style.display = "inline";
        document.getElementById("apellido").classList.add("is-invalid");
        return false;
    }else if(apellido.trim().length > 20){
        document.getElementById("error_apellido_min").style.display = "none";
        document.getElementById("error_apellido_max").style.display = "inline";
        document.getElementById("apellido").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_apellido_min").style.display = "none";
        document.getElementById("error_apellido_max").style.display = "none";
        document.getElementById("apellido").classList.remove("is-invalid");
        document.getElementById("apellido").classList.add("is-valid");
        return true;
    }   
}

function validarFechaNacimiento(fechaNacimiento){
    if (fechaNacimiento === "") {
        document.getElementById("error_nacimiento").style.display = "inline";
        document.getElementById("fecha_nac").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_nacimiento").style.display = "none";
        document.getElementById("fecha_nac").classList.remove("is-invalid");
        document.getElementById("fecha_nac").classList.add("is-valid");
        return true;
    }
}

function validarEmail(email){
    let rgEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    if (rgEmail.test(email) == false){
        document.getElementById("error_email").style.display = "inline";
        document.getElementById("email").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_email").style.display = "none"
        document.getElementById("email").classList.remove("is-invalid");
        document.getElementById("email").classList.add("is-valid");
        return true;
    }
}

function validarPassword(password){
    let rgPass = /^(?=\w*\d)(?=\w*[A-Z])(?=\w*[a-z])\S{6,10}$/;
    if (rgPass.test(password) == false){
        document.getElementById("error_password").style.display = "inline";
        document.getElementById("password").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_password").style.display = "none";
        document.getElementById("password").classList.remove("is-invalid");
        document.getElementById("password").classList.add("is-valid");
        return true;
    }
}

//Funcion para ver/no ver la password
function verPassword(){
    let input = document.getElementById("password");

    if(input.type == 'password'){
        input.type = 'text';
        document.getElementById('mostrar_pass').style.display = 'none';
        document.getElementById('ocultar_pass').style.display = 'inline';
    }else{
        input.type = 'password';
        document.getElementById('mostrar_pass').style.display = 'inline';
        document.getElementById('ocultar_pass').style.display = 'none';
    }
}

function validarDireccion(direccion){
    if(direccion.trim().length == 0){
        document.getElementById("error_direccion").style.display = "inline";
        document.getElementById("direccion").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_direccion").style.display = "none";
        document.getElementById("direccion").classList.remove("is-invalid");
        document.getElementById("direccion").classList.add("is-valid");
        return true;
    }
}

function validarComuna(comuna){
    if(comuna == "null"){
        document.getElementById("error_comuna").style.display = "inline";
        document.getElementById("comuna").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_comuna").style.display = "none";
        document.getElementById("comuna").classList.remove("is-invalid");
        document.getElementById("comuna").classList.add("is-valid");
        return true;
    }
}

function validarCarrera(carrera){
    if(carrera == "null"){
        document.getElementById("error_carrera").style.display = "inline";
        document.getElementById("carrera").classList.add("is-invalid");
        return false;
    }else{
        document.getElementById("error_carrera").style.display = "none";
        document.getElementById("carrera").classList.remove("is-invalid");
        document.getElementById("carrera").classList.add("is-valid");
        return true;
    }
}


    let max_caracteres = 50;
    $('#comentario').attr('maxlength', max_caracteres);  
  
    $('#comentario').keyup(function(){
      let num_caracteres = $('#comentario').val().length;
      let charRemain = (max_caracteres - num_caracteres);
        
  
      if(charRemain <= 0){
          document.getElementById("caracteres").innerHTML = '<span style="color: red;">Has excedido el límite de '+max_caracteres+' caracteres</span>';
      }else{
          document.getElementById("caracteres").innerHTML = charRemain+' caracteres restantes';   
      }
      
    });
  
