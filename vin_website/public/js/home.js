document.addEventListener('DOMContentLoaded', function () {

    // =========================================================
    // 1. NAVBAR – Reveal links + scrolled state
    // =========================================================
    const navbar = document.getElementById('navbar');
    const navItems = document.querySelectorAll('.nav-item');
    const hamburger = document.getElementById('hamburger');
    const navLinksContainer = document.getElementById('navLinks');
    const sections = document.querySelectorAll('section[id]');

    // Instantly make nav items visible (staggered)
    navItems.forEach((item, i) => {
        setTimeout(() => {
            item.classList.add('visible');
        }, i * 80);
    });

    // =========================================================
    // 0. BACKGROUND PARTICLES
    // =========================================================
    const particlesContainer = document.getElementById('particles');
    if (particlesContainer) {
        const particleCount = 20;
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';

            // Random properties
            const size = Math.random() * 5 + 2;
            const left = Math.random() * 100;
            const duration = Math.random() * 10 + 10;
            const delay = Math.random() * 10;
            const opacity = Math.random() * 0.3 + 0.1;

            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.left = `${left}%`;
            particle.style.animationDuration = `${duration}s`;
            particle.style.animationDelay = `${delay}s`;
            particle.style.opacity = opacity;
            particle.style.background = i % 2 === 0 ? 'var(--brand-primary)' : 'var(--brand-secondary)';

            particlesContainer.appendChild(particle);
        }
    }

    // Smooth scroll on nav link click
    navItems.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection && navbar) {
                window.scrollTo({
                    top: targetSection.offsetTop - navbar.offsetHeight,
                    behavior: 'smooth'
                });
            }
            // Close mobile menu
            if (navLinksContainer) navLinksContainer.classList.remove('active');
            if (hamburger) hamburger.classList.remove('active');
        });
    });

    // Mobile hamburger toggle
    if (hamburger && navLinksContainer) {
        hamburger.addEventListener('click', () => {
            navLinksContainer.classList.toggle('active');
            hamburger.classList.toggle('active');
        });
    }

    // Scroll: navbar shadow + active link + progress bar + bg shift
    window.addEventListener('scroll', () => {
        if (navbar) {
            const isScrolled = window.scrollY > 50;
            navbar.classList.toggle('scrolled', isScrolled);
            navbar.style.transform = isScrolled ? 'scale(0.98)' : 'scale(1)';
        }

        // Background Tone Shift
        const scrollPercent = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight);
        const hue = 220 + (scrollPercent * 30); // Shift from 220 to 250
        document.body.style.backgroundColor = `hsl(${hue}, 40%, 98%)`;

        // Scroll Progress Bar
        const scrollProgress = document.getElementById('scrollProgress');
        if (scrollProgress) {
            const totalScroll = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (window.scrollY / totalScroll) * 100;
            scrollProgress.style.width = progress + '%';
        }

        // Hero Parallax (Subtle)
        const shapes = document.querySelectorAll('.shape');
        shapes.forEach((shape, i) => {
            const speed = 0.05 + (i * 0.02);
            shape.style.transform = `translateY(${window.scrollY * speed}px)`;
        });

        // Active link highlighting
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop - (navbar ? navbar.offsetHeight : 72) - 150;
            if (window.scrollY >= sectionTop) {
                current = section.getAttribute('id');
            }
        });
        navItems.forEach(link => {
            link.classList.remove('active');
            if (current && link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });

        // Scroll-to-top button
        const scrollTopBtn = document.getElementById('scrollTop');
        if (scrollTopBtn) {
            scrollTopBtn.classList.toggle('visible', window.scrollY > 500);
        }
    });

    // Scroll to top
    const scrollTopBtn = document.getElementById('scrollTop');
    if (scrollTopBtn) {
        scrollTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // =========================================================
    // 2. SCROLL REVEAL – IntersectionObserver
    // =========================================================
    const revealEls = document.querySelectorAll('.reveal-left, .reveal-right, .reveal-up, .reveal-card');
    if ('IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                } else {
                    // Optional: remove if you want them to hide again when scrolling away
                    entry.target.classList.remove('revealed');
                }
            });
        }, { threshold: 0.12 });

        revealEls.forEach(el => revealObserver.observe(el));
    } else {
        // Fallback for older browsers
        revealEls.forEach(el => el.classList.add('revealed'));
    }

    // =========================================================
    // 3. STAT COUNTER ANIMATION
    // =========================================================
    const statNums = document.querySelectorAll('.stat-num[data-target]');
    if (statNums.length > 0) {
        const animateCounter = (el) => {
            if (el.dataset.animating === 'true') return;
            el.dataset.animating = 'true';

            const target = parseInt(el.getAttribute('data-target'), 10);
            let current = 0;
            const duration = 2000; // 2 seconds
            const steps = 60;
            const increment = target / steps;
            const stepTime = duration / steps;

            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                    el.dataset.animating = 'false';
                }
                el.textContent = Math.floor(current);
            }, stepTime);
        };

        if ('IntersectionObserver' in window) {
            const counterObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateCounter(entry.target);
                    } else {
                        // Reset when out of view if you want it to re-run
                        entry.target.textContent = '0';
                        entry.target.dataset.animating = 'false';
                    }
                });
            }, { threshold: 0.5 });

            statNums.forEach(el => counterObserver.observe(el));
        } else {
            statNums.forEach(el => el.textContent = el.getAttribute('data-target'));
        }
    }

    // =========================================================
    function showPopup(title, msg, icon) {
        const popup = document.getElementById('popup');
        const popupTitle = document.getElementById('popupTitle');
        const popupMsg = document.getElementById('popupMsg');
        const popupIcon = document.getElementById('popupIcon');

        if (popup && popupTitle && popupMsg && popupIcon) {
            popupTitle.innerText = title;
            popupMsg.innerText = msg;
            popupIcon.innerText = icon || '🔔';
            popup.classList.add('show');
            setTimeout(() => popup.classList.remove('show'), 5000);
        } else {
            alert(title + ': ' + msg);
        }
    }

    const popupClose = document.getElementById('popupClose');
    if (popupClose) {
        popupClose.addEventListener('click', () => {
            const popup = document.getElementById('popup');
            if (popup) popup.classList.remove('show');
        });
    }

    // =========================================================
    // 4. CONTACT FORM – Lead creation via frappe.call
    // =========================================================
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            e.preventDefault();

            const submitBtn = document.getElementById('submitBtn');
            if (!submitBtn) return;

            const getVal = id => {
                const el = document.getElementById(id);
                return el ? el.value.trim() : '';
            };

            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = 'Sending... ⏳';

            // Direct creation via API
            frappe.call({
                method: 'vin_website.api.create_lead',
                args: {
                    first_name: getVal('first_name'),
                    last_name: getVal('last_name'),
                    email_id: getVal('email_id'),
                    mobile_no: getVal('mobile_no'),
                    company_name: getVal('company_name'),
                    gender: getVal('gender'),
                    request_type: getVal('request_type')
                },
                callback: function (r) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;

                    if (r && r.message && r.message.status === 'Success') {
                        showPopup('Thank you! 🎉', 'Our experts will contact you soon.', '🎉');
                        contactForm.reset();
                    } else {
                        showPopup('Error ❌', 'Something went wrong. Please try again.', '❌');
                    }
                },
                error: function (r) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                    console.error('Lead creation error:', r);
                    showPopup('Error ❌', 'Something went wrong. Please try again.', '❌');
                }
            });
        });
    }

    // =========================================================
    // 5. MAGNETIC BUTTONS (Premium Feel)
    // =========================================================
    const magneticBtns = document.querySelectorAll('.btn-primary, .btn-outline, .nav-cta, .service-btn');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', function (e) {
            const position = btn.getBoundingClientRect();
            const x = e.pageX - position.left - position.width / 2;
            const y = e.pageY - position.top - position.height / 2;

            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.5}px) scale(1.05)`;
        });

        btn.addEventListener('mouseout', function () {
            btn.style.transform = 'translate(0px, 0px) scale(1)';
        });
    });

});
