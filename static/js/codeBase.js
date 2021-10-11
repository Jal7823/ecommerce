let buscador = document.getElementById('entrada');
let icono = document.getElementById('iconsito');

buscador.style.visibility='hidden'

icono.addEventListener('click',ocultar);


function ocultar(){
    buscador.style.visibility='visible'
    buscador.style.transition='2s'
}




