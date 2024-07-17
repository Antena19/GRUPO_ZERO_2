function CambiarTema(){
    console.log("Entró a cambiar tema");

            if (document.body.classList.contains('tema-oscuro')) {
                localStorage.setItem('tema', 'claro');
                console.log("Cambia Tema Claro");
            } else {
                localStorage.setItem('tema', 'oscuro');
                console.log("Cambia Tema Oscuro");
            }
    
    

    const temaGuardado = localStorage.getItem('tema');
    if (temaGuardado === 'oscuro') {
        document.body.classList.add('tema-oscuro');
        document.body.classList.remove('tema-claro');
    }
    if (temaGuardado === 'claro') {
        document.body.classList.add('tema-claro');
        document.body.classList.remove('tema-oscuro');
    }
}

document.addEventListener('DOMContentLoaded', function() {


//CARRITO DE COMPRA    
document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('.quantity-input');
    const totalElement = document.getElementById('total');
    const updateSubtotal = (itemRow, newQuantity, price) => {
        const subtotalElement = itemRow.querySelector('.subtotal');
        const newSubtotal = (newQuantity * price).toFixed(2);
        subtotalElement.textContent = `$${newSubtotal}`;
    };
    const updateTotal = () => {
        let total = 0;
        document.querySelectorAll('.quantity-input').forEach(input => {
            const itemRow = input.closest('tr');
            const price = parseFloat(itemRow.querySelector('td:nth-child(2)').textContent.slice(1));
            const quantity = parseInt(input.value);
            total += price * quantity;
        });
        totalElement.textContent = total.toFixed(2);
    };
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const itemRow = this.closest('tr');
            const newQuantity = parseInt(this.value);
            const price = parseFloat(itemRow.querySelector('td:nth-child(2)').textContent.slice(1));
            updateSubtotal(itemRow, newQuantity, price);
            updateTotal();
        });
    });
});

  
    // FORMULARIO DE BÚSQUEDA
    const searchForm = document.querySelector('form[role="search"]');
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            let searchTerm = this.querySelector('input[type="search"]').value.trim().toLowerCase();

            const datosInternos = [
                { seccion: 'artistas', nombre: 'Artistas', descripcion: 'Lista de artistas' },
                { seccion: 'tecnicas', nombre: 'Técnicas', descripcion: 'Lista de técnicas' },
                { seccion: 'productos', nombre: 'Productos', descripcion: 'Lista de productos' },
            ];

            const resultadosInternos = datosInternos.filter(dato =>
                dato.nombre.toLowerCase().includes(searchTerm) || dato.descripcion.toLowerCase().includes(searchTerm)
            );

            const resultadosDiv = document.getElementById('resultados-busqueda');
            if (resultadosInternos.length > 0) {
                if (resultadosDiv) {
                    resultadosDiv.innerHTML = '';
                    resultadosInternos.forEach(result => {
                        resultadosDiv.innerHTML += `
                            <div>
                                <h3>${result.nombre}</h3>
                                <p>${result.descripcion}</p>
                                <a href="/${result.seccion}/">Ir a ${result.nombre}</a>
                            </div>
                        `;
                    });
                }
            } else {
                window.location.href = `https://www.google.com/search?q=${searchTerm}`;
            }
        });
    }

    // EFECTO DE APARICIÓN DE LETRAS EN LOS TÍTULOS DE LAS TARJETAS
    const cardTitles = document.querySelectorAll('.card-title');
    cardTitles.forEach(title => {
        const text = title.textContent;
        title.innerHTML = '';
        const span = document.createElement('span');
        span.classList.add('typing-animation');
        title.appendChild(span);

        let index = 0;
        const typingEffect = () => {
            if (index < text.length) {
                const letter = document.createElement('span');
                letter.textContent = text.charAt(index) === ' ' ? '\u00A0' : text.charAt(index);
                letter.style.animationDelay = `${index * 0.1}s`;
                span.appendChild(letter);
                index++;
                setTimeout(typingEffect, 100); // Ajusta la velocidad de la animación 
            }
        };

        typingEffect();
    });
});