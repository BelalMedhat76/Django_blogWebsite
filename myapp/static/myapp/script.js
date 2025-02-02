// Add any custom JavaScript here
document.addEventListener('DOMContentLoaded', function () {
    // Example: Add animations to elements
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
    });
});