const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
const body = document.querySelector('body');

hamburger.addEventListener('click', () => {
    navLinks.classList.toggle('show');
    body.classList.toggle('lock-scroll'); // Prevents scrolling when the menu is open
});

// Optional: Close the navbar and restore scrolling when a link is clicked
document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('show');
        body.classList.remove('lock-scroll');
    });
});