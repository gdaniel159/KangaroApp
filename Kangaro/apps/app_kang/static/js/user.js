// Llamamos al objeto del DOM y le agregamos el evento clic
document.getElementById("menu-icon").addEventListener("click", function() {
    
    // Luego usamos el toggle show para mostrar el elemento
    document.getElementById("menu-dropdown").classList.toggle("show");

});

// Hacemos lo mismo aqui pero aplicacion el remove

document.getElementById("close-menu").addEventListener("click", function() {
    
    document.getElementById("menu-dropdown").classList.remove("show");

});