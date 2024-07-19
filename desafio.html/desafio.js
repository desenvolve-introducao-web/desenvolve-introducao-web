// script.js
document.addEventListener('DOMContentLoaded', () => {
    // Obtém o botão de alternância do modo escuro
    const toggleButton = document.getElementById('darkModeToggle');
    
    // Adiciona um ouvinte de evento para o clique no botão
    toggleButton.addEventListener('click', () => {
        // Alterna a classe 'dark-mode' no corpo e outros elementos da página
        document.body.classList.toggle('dark-mode');
        document.querySelector('header').classList.toggle('dark-mode');
        document.querySelector('nav').classList.toggle('dark-mode');
        document.querySelector('footer').classList.toggle('dark-mode');
        document.querySelectorAll('article').forEach(el => el.classList.toggle('dark-mode'));
        document.querySelectorAll('form').forEach(el => el.classList.toggle('dark-mode'));
        
        // Alterna a classe do botão e links para modo escuro
        toggleButton.classList.toggle('dark-mode');
        document.querySelectorAll('a').forEach(el => el.classList.toggle('dark-mode'));
        document.querySelectorAll('button').forEach(el => el.classList.toggle('dark-mode'));
    });
});
