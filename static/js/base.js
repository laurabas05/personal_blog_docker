// Cogemos el botón del HTML
const boton = document.getElementById('darkModeButton');

// Si el usuario ya eligió un tema antes, lo aplicamos al cargar
if (localStorage.getItem('tema') === 'oscuro') {
  document.documentElement.classList.add('dark');
  boton.textContent = '🌞';
}

// Cada vez que se hace clic en el botón:
boton.addEventListener('click', () => {
  // Si ahora mismo está en modo oscuro:
  if (document.documentElement.classList.contains('dark')) {
    // Quitamos la clase "dark" → vuelve al modo claro
    document.documentElement.classList.remove('dark');
    // Cambiamos el icono
    boton.textContent = '🌙';
    // Guardamos la elección en el navegador
    localStorage.setItem('tema', 'claro');
  } else {
    // Si está en claro → activamos modo oscuro
    document.documentElement.classList.add('dark');
    boton.textContent = '🌞';
    localStorage.setItem('tema', 'oscuro');
  }
});
