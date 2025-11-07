// Simple JavaScript for interaction (e.g., alert on button click or section click)
document.addEventListener('DOMContentLoaded', () => {
    const contactSection = document.querySelector('#contact');
    contactSection.addEventListener('click', () => {
        alert("You can contact me via email at your.email@example.com");
    });
});
