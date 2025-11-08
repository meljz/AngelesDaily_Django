// ========== CAROUSEL (only on home page) ==========
const track = document.querySelector('.carousel-track');
const nextBtn = document.querySelector('.next');
const prevBtn = document.querySelector('.prev');

// Check: Do these elements exist?
if (track && nextBtn && prevBtn) {
    let index = 0;

    nextBtn.onclick = () => {
        index = (index + 1) % document.querySelectorAll('.carousel-slide').length;
        track.style.transform = `translateX(-${index * 100}%)`;
    };

    prevBtn.onclick = () => {
        const slides = document.querySelectorAll('.carousel-slide');
        index = (index - 1 + slides.length) % slides.length;
        track.style.transform = `translateX(-${index * 100}%)`;
    };
}

// ========== BURGER MENU (on all pages) ==========
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    navLinks.classList.remove('active');
  });
});

const burger = document.querySelector('.burger_menu');
const navLinks = document.querySelector('.nav-links');

// Check: Do these elements exist?
if (burger && navLinks) {
    burger.onclick = () => {
        navLinks.classList.toggle('active');
    };
}