document.addEventListener('DOMContentLoaded', () => {
    // 1. Resaltar visualmente la página activa de forma segura
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');

    navLinks.forEach(link => {
        // link.pathname obtiene de forma nativa la ruta absoluta (ej: '/' o '/about')
        const linkPath = link.pathname;
        
        // Evitamos que coincida todo con la raíz '/' usando validaciones exactas
        if (linkPath === currentPath) {
            link.classList.add('active');
        } else if (linkPath !== '/' && currentPath.startsWith(linkPath)) {
            // Esto mantiene encendido el menú si estamos dentro de un post específico
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    // 2. Animación fluida de entrada para la página (Optimizada sin bloquear hilos)
    const mainContent = document.querySelector('main');
    if (mainContent) {
        mainContent.style.opacity = '0';
        mainContent.style.transform = 'translateY(5px)';
        mainContent.style.transition = 'opacity 0.25s ease-out, transform 0.25s ease-out';
        
        requestAnimationFrame(() => {
            setTimeout(() => {
                mainContent.style.opacity = '1';
                mainContent.style.transform = 'translateY(0)';
            }, 10);
        });
    }
});
