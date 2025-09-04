// Initialize ScrollReveal for animations
const scrollReveal = ScrollReveal({
    distance: '50px',
    duration: 1000,
    delay: 200,
    reset: true // ✅ Ensures animations replay on scroll
});

document.addEventListener('DOMContentLoaded', function () {
    // Get all necessary elements
    const btnLogin = document.querySelector('.btnLogin-popup');
    const blurBgOverlay = document.querySelector('.blur-bg-overlay');
    const authWrapper = document.querySelector('.auth-wrapper');
    const iconClose = document.querySelector('.icon-close');
    const registerLink = document.querySelector('.register-link'); // Switch to register
    const loginLink = document.querySelector('.login-link'); // Switch to login

    // Check URL parameters to show appropriate form on page load
    const urlParams = new URLSearchParams(window.location.search);
    const show = urlParams.get('show');

    if (show === 'register') {
        authWrapper.classList.add('active');
        blurBgOverlay.classList.add('active');
        authWrapper.classList.add('active-popup');
    } else if (show === 'login') {
        authWrapper.classList.remove('active');
        blurBgOverlay.classList.add('active');
        authWrapper.classList.add('active-popup');
    }

    // Show login form when login button clicked
    btnLogin?.addEventListener('click', () => {
        blurBgOverlay.classList.add('active');
        authWrapper.classList.add('active-popup');
        // Default to login form
        authWrapper.classList.remove('active');
    });

    // Close popup
    iconClose?.addEventListener('click', () => {
        blurBgOverlay.classList.remove('active');
        authWrapper.classList.remove('active-popup');
        // Reset to login form when closing
        authWrapper.classList.remove('active');
    });

    // Switch to register form
    registerLink?.addEventListener('click', (e) => {
        e.preventDefault();
        authWrapper.classList.add('active');
    });

    // Switch to login form
    loginLink?.addEventListener('click', (e) => {
        e.preventDefault();
        authWrapper.classList.remove('active');
    });

    // Password toggle functionality
    document.querySelectorAll('.toggle-password').forEach(button => {
        button.addEventListener('click', function () {
            const passwordInput = this.closest('.input-box').querySelector('.password-input');
            const eyeIcon = this.querySelector('.eye-icon');

            if (passwordInput && eyeIcon) {
                if (passwordInput.type === 'password') {
                    passwordInput.type = 'text';
                    eyeIcon.setAttribute('name', 'eye');
                } else {
                    passwordInput.type = 'password';
                    eyeIcon.setAttribute('name', 'eye-off');
                }
            }
        });
    });

    // Close popup when clicking outside
    blurBgOverlay?.addEventListener('click', (e) => {
        if (e.target === blurBgOverlay) {
            blurBgOverlay.classList.remove('active');
            authWrapper.classList.remove('active-popup');
            authWrapper.classList.remove('active');
        }
    });
});// Check URL parameters to show appropriate form
document.addEventListener('DOMContentLoaded', function () {
    const urlParams = new URLSearchParams(window.location.search);
    const show = urlParams.get('show');

    const wrapper = document.querySelector('.auth-wrapper');
    const blurBg = document.querySelector('.blur-bg-overlay');

    if (show === 'register') {
        wrapper.classList.add('active');
        blurBg.classList.add('active');
    } else if (show === 'login') {
        wrapper.classList.remove('active');
        blurBg.classList.add('active');
    }
});

// Existing form switching logic
const wrapper = document.querySelector('.auth-wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.btnLogin-popup');
const iconClose = document.querySelector('.icon-close');
const blurBgOverlay = document.querySelector('.blur-bg-overlay');

registerLink.addEventListener('click', (e) => {
    e.preventDefault();
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', (e) => {
    e.preventDefault();
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', () => {
    blurBgOverlay.classList.add('active');
});

iconClose.addEventListener('click', () => {
    blurBgOverlay.classList.remove('active');
});

// Password toggle functionality
document.querySelectorAll('.toggle-password').forEach(toggle => {
    toggle.addEventListener('click', function () {
        const passwordInput = this.previousElementSibling;
        const eyeIcon = this.querySelector('.eye-icon');

        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            eyeIcon.name = 'eye';
        } else {
            passwordInput.type = 'password';
            eyeIcon.name = 'eye-off';
        }
    });
});



// Enhanced message handling
document.addEventListener('DOMContentLoaded', function () {
    // Add close buttons to all messages
    const messages = document.querySelectorAll('.messages .alert');

    messages.forEach(function (message, index) {
        // Add close button
        const closeBtn = document.createElement('button');
        closeBtn.className = 'alert-close';
        closeBtn.innerHTML = '×';
        closeBtn.setAttribute('aria-label', 'Close message');

        // Close message when clicked
        closeBtn.addEventListener('click', function () {
            message.style.animation = 'none';
            message.style.opacity = '0';
            message.style.transform = 'translateY(-20px) scale(0.95)';
            setTimeout(() => {
                message.remove();
            }, 200);
        });

        message.appendChild(closeBtn);

        // Auto remove after animation completes
        setTimeout(() => {
            if (message.parentNode) {
                message.style.opacity = '0';
                message.style.transform = 'translateY(-20px) scale(0.95)';
                setTimeout(() => {
                    message.remove();
                }, 300);
            }
        }, 4800); // Remove slightly before animation ends
    });
});



// Function to create new messages dynamically (if needed)
function showMessage(text, type = 'info') {
    const messagesContainer = document.querySelector('.messages') || createMessagesContainer();

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = text;

    // Add close button
    const closeBtn = document.createElement('button');
    closeBtn.className = 'alert-close';
    closeBtn.innerHTML = '×';
    closeBtn.addEventListener('click', function () {
        alert.remove();
    });

    alert.appendChild(closeBtn);
    messagesContainer.appendChild(alert);



    // Auto remove
    setTimeout(() => {
        if (alert.parentNode) {
            alert.remove();
        }
    }, 5000);
}

function createMessagesContainer() {
    const container = document.createElement('div');
    container.className = 'messages';
    document.body.appendChild(container);
    return container;
}


// Automatic Video Slideshow
let currentVideoIndex = 0;
const videoButtons = document.querySelectorAll('.vid-btn');
const videoSlider = document.getElementById('video-slider');

function changeVideo(index) {
    videoButtons.forEach(btn => btn.classList.remove('active'));
    videoButtons[index].classList.add('active');
    const newSrc = videoButtons[index].getAttribute('data-src');
    videoSlider.src = newSrc;
    videoSlider.play();
}

function autoPlayVideos() {
    setInterval(() => {
        currentVideoIndex = (currentVideoIndex + 1) % videoButtons.length;
        changeVideo(currentVideoIndex);
    }, 5000);
}

autoPlayVideos();

videoButtons.forEach((btn, index) => {
    btn.addEventListener('click', () => {
        currentVideoIndex = index;
        changeVideo(currentVideoIndex);
    });
});



const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

if (localStorage.getItem('dark-mode')) {
    body.classList.add('dark-mode');
    themeToggle.checked = true;
}

themeToggle.addEventListener('change', function () {
    if (this.checked) {
        body.classList.add('dark-mode');
        localStorage.setItem('dark-mode', 'enabled');
    } else {
        body.classList.remove('dark-mode');
        localStorage.removeItem('dark-mode');
    }
});


// Banner Top Destinations
const banner = document.querySelector(".banner_wrapper");
Array.from(banner.children).forEach((item) => {
    const duplicateNode = item.cloneNode(true);
    duplicateNode.setAttribute("aria-hidden", true);
    banner.appendChild(duplicateNode);
});

// Packages Swiper
document.addEventListener('DOMContentLoaded', function () {
    // Card Packages Swiper
    const cardSwiper = new Swiper('.container.swiper', {
        loop: true,
        spaceBetween: 30,
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
            dynamicBullets: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            0: { slidesPerView: 1 },
            768: { slidesPerView: 2 },
            1024: { slidesPerView: 3 }
        },
    });

});