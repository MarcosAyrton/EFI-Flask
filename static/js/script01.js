// Función visibilityCards:

// Declaramos todas las cards:
var cards = [
    document.getElementById("card01"),
    document.getElementById("card02"),
    document.getElementById("card03"),
    document.getElementById("card04"),
    document.getElementById("card05"),
    document.getElementById("card06")
  ];
  // indice para buscar la card que está visible
  var currentCardIndex = 0;

// Boton siguiente para mostrar y esconder formularios
function visibilityCards() {

    // Ocultar la card actual
    if (currentCardIndex < cards.length) {
        cards[currentCardIndex].style.display = "none";
        currentCardIndex++;
}
}

