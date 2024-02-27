document.addEventListener('DOMContentLoaded', function() {
    toggleMobileMenu();
});

const toggleMobileMenu = () => {
    const hamburgerButton = document.querySelector('#hamburger-btn');
    const mobileMenu = document.querySelector('#mobile-menu');
    hamburgerButton.addEventListener('click', () =>{
        mobileMenu.classList.toggle('hidden');
    });
}