/**
 * Website Optimization & Performance Enhancement Script
 * Handles smooth transitions, lazy loading, and performance improvements
 */

(function() {
    'use strict';

    // Configuration
    const config = {
        enableLazyLoad: true,
        enableScrollAnimations: true,
        enableSmoothScroll: true,
        enablePageTransitions: true,
        observerOptions: {
            root: null,
            rootMargin: '50px',
            threshold: 0.1
        },
        debounceDelay: 150,
        transitionDelay: 300
    };

    // ============================================
    // 1. INTERSECTION OBSERVER FOR SCROLL ANIMATIONS
    // ============================================

    function initScrollAnimations() {
        if (!config.enableScrollAnimations) return;

        // Create intersection observer for scroll animations
        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -100px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    // Optionally stop observing after animation
                    // observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observe all scroll-animate elements
        const scrollElements = document.querySelectorAll('.scroll-animate, [data-scroll-animate]');
        scrollElements.forEach(el => observer.observe(el));
    }

    // ============================================
    // 2. LAZY LOADING IMAGES
    // ============================================

    function initLazyLoading() {
        if (!config.enableLazyLoad) return;

        // Use native lazy loading if available
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src || img.src;
                        img.srcset = img.dataset.srcset || img.srcset;
                        img.classList.remove('lazy-load');
                        img.classList.add('lazy-loaded');
                        
                        // Stop observing this image
                        imageObserver.unobserve(img);
                    }
                });
            }, {
                rootMargin: '100px 0px'
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }

        // Fallback for older browsers
        const lazyImages = document.querySelectorAll('img[data-src]');
        if ('loading' in HTMLImageElement.prototype) {
            lazyImages.forEach(img => {
                img.loading = 'lazy';
            });
        }
    }

    // ============================================
    // 3. SMOOTH PAGE TRANSITIONS
    // ============================================

    function initPageTransitions() {
        if (!config.enablePageTransitions) return;

        // Add fade-in animation to page load
        document.addEventListener('DOMContentLoaded', function() {
            document.body.classList.add('page-transition-enter');
        });

        // Handle link clicks for smooth transitions
        document.addEventListener('click', function(e) {
            const link = e.target.closest('a[href]:not([href^="#"]):not([target]):not([href*="javascript"])');
            
            if (link && link.hostname === window.location.hostname) {
                e.preventDefault();
                
                // Add fade-out animation
                document.body.classList.add('page-transition-exit');
                
                // Navigate after animation
                setTimeout(() => {
                    window.location.href = link.href;
                }, config.transitionDelay);
            }
        });
    }

    // ============================================
    // 4. SMOOTH SCROLL BEHAVIOR
    // ============================================

    function initSmoothScroll() {
        if (!config.enableSmoothScroll) return;

        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href !== '#' && href !== '#!') {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            });
        });
    }

    // ============================================
    // 5. DEBOUNCE UTILITY
    // ============================================

    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // ============================================
    // 6. HEADER SCROLL EFFECT
    // ============================================

    function initHeaderEffect() {
        const header = document.querySelector('.header, [role="banner"], header');
        if (!header) return;

        const scrollThreshold = 50;
        let lastScrollTop = 0;

        window.addEventListener('scroll', debounce(function() {
            const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

            if (scrollTop > scrollThreshold) {
                header.classList.add('sticky');
            } else {
                header.classList.remove('sticky');
            }

            lastScrollTop = scrollTop <= 0 ? 0 : scrollTop;
        }, config.debounceDelay));
    }

    // ============================================
    // 7. FILTER & SEARCH ANIMATIONS
    // ============================================

    function initFilterAnimations() {
        const filterButtons = document.querySelectorAll('.filter-button, [data-filter]');
        
        filterButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                
                // Remove active class from all buttons
                filterButtons.forEach(btn => btn.classList.remove('active'));
                
                // Add active class to clicked button
                this.classList.add('active');
                
                // Add animation to content
                const container = document.querySelector('[data-filter-target]');
                if (container) {
                    container.style.opacity = '0';
                    container.style.transform = 'translateY(10px)';
                    
                    setTimeout(() => {
                        container.style.transition = 'all 0.3s ease';
                        container.style.opacity = '1';
                        container.style.transform = 'translateY(0)';
                    }, 50);
                }
            });
        });
    }

    // ============================================
    // 8. FORM INPUT ANIMATIONS
    // ============================================

    function initFormAnimations() {
        const inputs = document.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            // Add filled class if input has value
            if (input.value) {
                input.classList.add('filled');
            }

            input.addEventListener('focus', function() {
                this.closest('.form-group, .field-wrapper')?.classList.add('focused');
            });

            input.addEventListener('blur', function() {
                this.closest('.form-group, .field-wrapper')?.classList.remove('focused');
                if (this.value) {
                    this.classList.add('filled');
                } else {
                    this.classList.remove('filled');
                }
            });

            input.addEventListener('input', function() {
                if (this.value) {
                    this.classList.add('filled');
                } else {
                    this.classList.remove('filled');
                }
            });
        });
    }

    // ============================================
    // 9. MODAL & DIALOG ANIMATIONS
    // ============================================

    function initModalAnimations() {
        // Close modal on background click
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('modal-overlay')) {
                const modal = e.target.closest('.modal, [role="dialog"]');
                if (modal) {
                    modal.classList.add('closing');
                    setTimeout(() => {
                        modal.remove();
                    }, 300);
                }
            }
        });

        // Close modal on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const modal = document.querySelector('.modal.active, [role="dialog"][aria-modal="true"]');
                if (modal) {
                    modal.classList.add('closing');
                    setTimeout(() => {
                        modal.classList.remove('active');
                    }, 300);
                }
            }
        });
    }

    // ============================================
    // 10. BUTTON RIPPLE EFFECT
    // ============================================

    function initRippleEffect() {
        document.addEventListener('click', function(e) {
            const button = e.target.closest('button, .btn, [role="button"]');
            if (!button) return;

            // Create ripple element
            const ripple = document.createElement('span');
            ripple.classList.add('ripple');
            
            const rect = button.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';

            button.appendChild(ripple);

            // Remove ripple after animation
            setTimeout(() => ripple.remove(), 600);
        });
    }

    // ============================================
    // 11. PERFORMANCE MONITORING
    // ============================================

    function initPerformanceMonitoring() {
        // Report Core Web Vitals if available
        if ('web-vital' in window) {
            window.addEventListener('web-vital', (event) => {
                console.log('Web Vital:', event.detail.name, event.detail.value);
            });
        }

        // Log performance timing
        window.addEventListener('load', function() {
            if (window.performance && window.performance.timing) {
                const timing = window.performance.timing;
                const loadTime = timing.loadEventEnd - timing.navigationStart;
                console.log('Page Load Time:', loadTime + 'ms');
            }
        });
    }

    // ============================================
    // 12. ANIMATION FRAME THROTTLING
    // ============================================

    function throttleScroll(callback) {
        let ticking = false;
        
        window.addEventListener('scroll', function() {
            if (!ticking) {
                window.requestAnimationFrame(function() {
                    callback();
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // ============================================
    // 13. REDUCE MOTION SUPPORT
    // ============================================

    function initAccessibilitySupport() {
        // Check if user prefers reduced motion
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        
        if (prefersReducedMotion) {
            document.body.classList.add('reduce-motion');
            document.documentElement.style.scrollBehavior = 'auto';
        }

        // Listen for changes in preference
        window.matchMedia('(prefers-reduced-motion: reduce)').addEventListener('change', (e) => {
            if (e.matches) {
                document.body.classList.add('reduce-motion');
            } else {
                document.body.classList.remove('reduce-motion');
            }
        });
    }

    // ============================================
    // 14. UTILITY FUNCTIONS
    // ============================================

    function addAnimationClass(element, animationClass, duration = 500) {
        if (!element) return;
        element.classList.add(animationClass);
        setTimeout(() => {
            element.classList.remove(animationClass);
        }, duration);
    }

    function animateCounter(element, target, duration = 1000) {
        if (!element) return;
        const start = 0;
        const increment = target / (duration / 16);
        let current = start;

        const counter = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.textContent = target;
                clearInterval(counter);
            } else {
                element.textContent = Math.floor(current);
            }
        }, 16);
    }

    // ============================================
    // 15. INITIALIZATION
    // ============================================

    function init() {
        // Wait for DOM to be fully loaded
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initAll);
        } else {
            initAll();
        }
    }

    function initAll() {
        console.log('Initializing website optimizations...');
        
        initScrollAnimations();
        initLazyLoading();
        initPageTransitions();
        initSmoothScroll();
        initHeaderEffect();
        initFilterAnimations();
        initFormAnimations();
        initModalAnimations();
        initRippleEffect();
        initAccessibilitySupport();
        initPerformanceMonitoring();

        console.log('Website optimizations initialized successfully!');
    }

    // Expose public API
    window.WebsiteOptimizations = {
        init: init,
        addAnimationClass: addAnimationClass,
        animateCounter: animateCounter,
        config: config,
        debounce: debounce
    };

    // Auto-initialize
    init();

})();
