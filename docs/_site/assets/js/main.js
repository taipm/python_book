// ===== MAIN JAVASCRIPT FILE =====

(function() {
    'use strict';

    // ===== UTILITY FUNCTIONS =====
    
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

    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }

    function getScrollPercentage() {
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        return scrollHeight > 0 ? (scrollTop / scrollHeight) * 100 : 0;
    }

    function smoothScrollTo(element, offset = 0) {
        const elementPosition = element.offsetTop - offset;
        window.scrollTo({
            top: elementPosition,
            behavior: 'smooth'
        });
    }

    // ===== THEME MANAGEMENT =====
    
    class ThemeManager {
        constructor() {
            this.themeToggle = document.querySelector('.theme-toggle');
            this.currentTheme = localStorage.getItem('theme') || 'light';
            this.init();
        }

        init() {
            this.setTheme(this.currentTheme);
            if (this.themeToggle) {
                this.themeToggle.addEventListener('click', () => this.toggleTheme());
            }
        }

        setTheme(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            this.currentTheme = theme;
        }

        toggleTheme() {
            const newTheme = this.currentTheme === 'light' ? 'dark' : 'light';
            this.setTheme(newTheme);
        }
    }

    // ===== SEARCH FUNCTIONALITY =====
    
    class SearchManager {
        constructor() {
            this.searchToggle = document.querySelector('.search-toggle');
            this.searchOverlay = document.querySelector('.search-overlay');
            this.searchInput = document.querySelector('.search-input');
            this.searchClose = document.querySelector('.search-close');
            this.searchResults = document.querySelector('.search-results');
            this.searchData = [];
            this.init();
        }

        init() {
            if (!this.searchToggle) return;

            this.searchToggle.addEventListener('click', () => this.openSearch());
            this.searchClose.addEventListener('click', () => this.closeSearch());
            this.searchOverlay.addEventListener('click', (e) => {
                if (e.target === this.searchOverlay) this.closeSearch();
            });

            this.searchInput.addEventListener('input', debounce((e) => {
                this.performSearch(e.target.value);
            }, 300));

            // Keyboard shortcuts
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') this.closeSearch();
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    this.openSearch();
                }
            });

            this.loadSearchData();
        }

        openSearch() {
            this.searchOverlay.classList.add('active');
            this.searchInput.focus();
        }

        closeSearch() {
            this.searchOverlay.classList.remove('active');
            this.searchInput.value = '';
            this.searchResults.innerHTML = '';
            this.searchResults.classList.remove('has-results');
        }

        async loadSearchData() {
            try {
                // In a real implementation, this would load from a search index
                // For now, we'll create a simple mock
                this.searchData = [
                    {
                        title: 'Chương 1: Giới thiệu về Python',
                        url: '/chapters/chapter01.html',
                        content: 'Python là ngôn ngữ lập trình bậc cao...'
                    },
                    {
                        title: 'Chương 2: Cài đặt môi trường',
                        url: '/chapters/chapter02.html',
                        content: 'Hướng dẫn cài đặt Python và các công cụ...'
                    }
                ];
            } catch (error) {
                console.error('Failed to load search data:', error);
            }
        }

        performSearch(query) {
            if (!query.trim()) {
                this.searchResults.classList.remove('has-results');
                return;
            }

            const results = this.searchData.filter(item => 
                item.title.toLowerCase().includes(query.toLowerCase()) ||
                item.content.toLowerCase().includes(query.toLowerCase())
            );

            this.displayResults(results, query);
        }

        displayResults(results, query) {
            if (results.length === 0) {
                this.searchResults.innerHTML = `
                    <div class="search-no-results">
                        <p>Không tìm thấy kết quả cho "${query}"</p>
                    </div>
                `;
            } else {
                this.searchResults.innerHTML = results.map(result => `
                    <div class="search-result-item">
                        <h4><a href="${result.url}">${result.title}</a></h4>
                        <p>${result.content.substring(0, 150)}...</p>
                    </div>
                `).join('');
            }
            
            this.searchResults.classList.add('has-results');
        }
    }

    // ===== NAVIGATION MANAGEMENT =====
    
    class NavigationManager {
        constructor() {
            this.mobileToggle = document.querySelector('.mobile-menu-toggle');
            this.mainNav = document.querySelector('.main-nav');
            this.init();
        }

        init() {
            if (this.mobileToggle) {
                this.mobileToggle.addEventListener('click', () => this.toggleMobileMenu());
            }

            // Close mobile menu when clicking outside
            document.addEventListener('click', (e) => {
                if (!e.target.closest('.site-header')) {
                    this.closeMobileMenu();
                }
            });
        }

        toggleMobileMenu() {
            this.mainNav.classList.toggle('mobile-active');
            this.mobileToggle.classList.toggle('active');
        }

        closeMobileMenu() {
            this.mainNav.classList.remove('mobile-active');
            this.mobileToggle.classList.remove('active');
        }
    }

    // ===== READING PROGRESS =====
    
    class ReadingProgressManager {
        constructor() {
            this.progressBar = document.querySelector('.reading-progress-indicator .progress-fill');
            this.sidebarProgress = document.querySelector('.reading-progress .progress-fill');
            this.progressPercentage = document.querySelector('.progress-percentage');
            this.init();
        }

        init() {
            if (!this.progressBar) return;

            const updateProgress = throttle(() => {
                const percentage = getScrollPercentage();
                
                if (this.progressBar) {
                    this.progressBar.style.width = `${percentage}%`;
                }
                
                if (this.sidebarProgress) {
                    this.sidebarProgress.style.width = `${percentage}%`;
                }
                
                if (this.progressPercentage) {
                    this.progressPercentage.textContent = `${Math.round(percentage)}%`;
                }
            }, 16);

            window.addEventListener('scroll', updateProgress);
            window.addEventListener('resize', updateProgress);
        }
    }

    // ===== TABLE OF CONTENTS =====
    
    class TableOfContentsManager {
        constructor() {
            this.tocContainer = document.querySelector('.toc-content');
            this.headings = [];
            this.activeHeading = null;
            this.init();
        }

        init() {
            if (!this.tocContainer) return;

            this.generateTOC();
            this.setupScrollSpy();
        }

        generateTOC() {
            const content = document.querySelector('.chapter-body') || document.querySelector('.main-content');
            if (!content) return;

            this.headings = Array.from(content.querySelectorAll('h2, h3, h4'));
            
            if (this.headings.length === 0) return;

            const tocHTML = this.headings.map((heading, index) => {
                const id = heading.id || `heading-${index}`;
                if (!heading.id) heading.id = id;

                const level = parseInt(heading.tagName.charAt(1));
                const indent = level > 2 ? 'style="margin-left: ' + ((level - 2) * 20) + 'px"' : '';

                return `<li ${indent}><a href="#${id}" class="toc-link" data-heading="${id}">${heading.textContent}</a></li>`;
            }).join('');

            this.tocContainer.innerHTML = `<ul>${tocHTML}</ul>`;

            // Add click handlers
            this.tocContainer.querySelectorAll('.toc-link').forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const target = document.getElementById(link.dataset.heading);
                    if (target) {
                        smoothScrollTo(target, 100);
                    }
                });
            });
        }

        setupScrollSpy() {
            const updateActiveHeading = throttle(() => {
                let current = null;
                const scrollTop = window.pageYOffset + 150;

                for (const heading of this.headings) {
                    if (heading.offsetTop <= scrollTop) {
                        current = heading;
                    } else {
                        break;
                    }
                }

                if (current && current !== this.activeHeading) {
                    // Remove active class from all links
                    this.tocContainer.querySelectorAll('.toc-link').forEach(link => {
                        link.classList.remove('active');
                    });

                    // Add active class to current link
                    const activeLink = this.tocContainer.querySelector(`[data-heading="${current.id}"]`);
                    if (activeLink) {
                        activeLink.classList.add('active');
                    }

                    this.activeHeading = current;
                }
            }, 16);

            window.addEventListener('scroll', updateActiveHeading);
        }
    }

    // ===== BACK TO TOP =====
    
    class BackToTopManager {
        constructor() {
            this.backToTopBtn = document.querySelector('.back-to-top');
            this.init();
        }

        init() {
            if (!this.backToTopBtn) return;

            const toggleVisibility = throttle(() => {
                if (window.pageYOffset > 300) {
                    this.backToTopBtn.classList.add('visible');
                } else {
                    this.backToTopBtn.classList.remove('visible');
                }
            }, 16);

            window.addEventListener('scroll', toggleVisibility);

            this.backToTopBtn.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }
    }

    // ===== CODE FUNCTIONALITY =====
    
    class CodeManager {
        constructor() {
            this.init();
        }

        init() {
            this.addCopyButtons();
            this.addLanguageLabels();
            this.setupInteractiveCode();
        }

        addCopyButtons() {
            document.querySelectorAll('.highlight').forEach(block => {
                const button = document.createElement('button');
                button.className = 'copy-btn';
                button.textContent = 'Copy';
                button.addEventListener('click', () => this.copyCode(block, button));
                block.appendChild(button);
            });
        }

        addLanguageLabels() {
            document.querySelectorAll('.highlight').forEach(block => {
                const code = block.querySelector('code');
                if (code && code.className) {
                    const language = code.className.match(/language-(\w+)/);
                    if (language) {
                        block.setAttribute('data-lang', language[1]);
                    }
                }
            });
        }

        async copyCode(block, button) {
            const code = block.querySelector('pre').textContent;
            
            try {
                await navigator.clipboard.writeText(code);
                button.textContent = 'Copied!';
                button.style.backgroundColor = 'var(--color-success)';
                
                setTimeout(() => {
                    button.textContent = 'Copy';
                    button.style.backgroundColor = '';
                }, 2000);
            } catch (err) {
                console.error('Failed to copy code:', err);
                button.textContent = 'Failed';
                setTimeout(() => {
                    button.textContent = 'Copy';
                }, 2000);
            }
        }

        setupInteractiveCode() {
            document.querySelectorAll('.interactive-code .run-btn').forEach(button => {
                button.addEventListener('click', () => {
                    // This would integrate with a code execution service
                    console.log('Running code...');
                    button.textContent = 'Running...';
                    
                    setTimeout(() => {
                        button.textContent = 'Run Code';
                    }, 2000);
                });
            });
        }
    }

    // ===== FLOATING ACTIONS =====
    
    class FloatingActionsManager {
        constructor() {
            this.bookmarkBtn = document.querySelector('.bookmark-btn');
            this.notesBtn = document.querySelector('.notes-btn');
            this.shareBtn = document.querySelector('.share-btn');
            this.notesModal = document.querySelector('.notes-modal');
            this.shareModal = document.querySelector('.share-modal');
            this.init();
        }

        init() {
            if (this.bookmarkBtn) {
                this.bookmarkBtn.addEventListener('click', () => this.toggleBookmark());
            }

            if (this.notesBtn) {
                this.notesBtn.addEventListener('click', () => this.openNotesModal());
            }

            if (this.shareBtn) {
                this.shareBtn.addEventListener('click', () => this.openShareModal());
            }

            this.setupModals();
            this.loadBookmarkState();
        }

        toggleBookmark() {
            const chapterUrl = this.bookmarkBtn.dataset.chapter;
            const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
            
            if (bookmarks.includes(chapterUrl)) {
                const index = bookmarks.indexOf(chapterUrl);
                bookmarks.splice(index, 1);
                this.bookmarkBtn.classList.remove('active');
            } else {
                bookmarks.push(chapterUrl);
                this.bookmarkBtn.classList.add('active');
            }
            
            localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
        }

        loadBookmarkState() {
            if (!this.bookmarkBtn) return;
            
            const chapterUrl = this.bookmarkBtn.dataset.chapter;
            const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
            
            if (bookmarks.includes(chapterUrl)) {
                this.bookmarkBtn.classList.add('active');
            }
        }

        openNotesModal() {
            if (this.notesModal) {
                this.notesModal.classList.add('active');
                this.loadNotes();
            }
        }

        openShareModal() {
            if (this.shareModal) {
                this.shareModal.classList.add('active');
            }
        }

        setupModals() {
            // Close modals when clicking outside or on close button
            document.querySelectorAll('.modal').forEach(modal => {
                modal.addEventListener('click', (e) => {
                    if (e.target === modal || e.target.classList.contains('modal-close')) {
                        modal.classList.remove('active');
                    }
                });
            });

            // Notes modal functionality
            const saveNotesBtn = document.querySelector('.notes-save');
            const cancelNotesBtn = document.querySelector('.notes-cancel');
            
            if (saveNotesBtn) {
                saveNotesBtn.addEventListener('click', () => this.saveNotes());
            }
            
            if (cancelNotesBtn) {
                cancelNotesBtn.addEventListener('click', () => {
                    this.notesModal.classList.remove('active');
                });
            }

            // Share modal functionality
            document.querySelectorAll('.share-option').forEach(option => {
                option.addEventListener('click', (e) => this.handleShare(e));
            });
        }

        loadNotes() {
            const chapterUrl = this.notesBtn.dataset.chapter;
            const notes = localStorage.getItem(`notes-${chapterUrl}`) || '';
            const textarea = document.querySelector('.notes-textarea');
            if (textarea) {
                textarea.value = notes;
            }
        }

        saveNotes() {
            const chapterUrl = this.notesBtn.dataset.chapter;
            const textarea = document.querySelector('.notes-textarea');
            const notes = textarea.value;
            
            localStorage.setItem(`notes-${chapterUrl}`, notes);
            this.notesModal.classList.remove('active');
            
            // Update notes button state
            if (notes.trim()) {
                this.notesBtn.classList.add('active');
            } else {
                this.notesBtn.classList.remove('active');
            }
        }

        handleShare(e) {
            const platform = e.currentTarget.dataset.platform;
            const url = window.location.href;
            const title = document.title;
            
            if (platform === 'facebook') {
                window.open(`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`, '_blank');
            } else if (platform === 'twitter') {
                window.open(`https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`, '_blank');
            } else if (platform === 'linkedin') {
                window.open(`https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`, '_blank');
            } else if (e.currentTarget.classList.contains('copy-link')) {
                navigator.clipboard.writeText(url).then(() => {
                    e.currentTarget.innerHTML = '<i class="fas fa-check"></i> Đã sao chép';
                    setTimeout(() => {
                        e.currentTarget.innerHTML = '<i class="fas fa-link"></i> Sao chép link';
                    }, 2000);
                });
            }
            
            this.shareModal.classList.remove('active');
        }
    }

    // ===== FEEDBACK SYSTEM =====
    
    class FeedbackManager {
        constructor() {
            this.feedbackButtons = document.querySelectorAll('.feedback-btn');
            this.init();
        }

        init() {
            this.feedbackButtons.forEach(button => {
                button.addEventListener('click', (e) => this.handleFeedback(e));
            });
        }

        handleFeedback(e) {
            const feedback = e.currentTarget.dataset.feedback;
            const chapterUrl = window.location.pathname;
            
            // Store feedback locally
            const feedbackData = JSON.parse(localStorage.getItem('feedback') || '{}');
            feedbackData[chapterUrl] = feedback;
            localStorage.setItem('feedback', JSON.stringify(feedbackData));
            
            // Update UI
            this.feedbackButtons.forEach(btn => btn.classList.remove('active'));
            e.currentTarget.classList.add('active');
            
            // Show thank you message
            const thankYouMsg = document.createElement('div');
            thankYouMsg.className = 'feedback-thanks';
            thankYouMsg.textContent = 'Cảm ơn phản hồi của bạn!';
            thankYouMsg.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: var(--color-success);
                color: white;
                padding: 12px 20px;
                border-radius: 6px;
                z-index: 1000;
                animation: slideIn 0.3s ease;
            `;
            
            document.body.appendChild(thankYouMsg);
            
            setTimeout(() => {
                thankYouMsg.remove();
            }, 3000);
        }
    }

    // ===== LEARNING OBJECTIVES =====
    
    class LearningObjectivesManager {
        constructor() {
            this.checkboxes = document.querySelectorAll('.objective-checkbox');
            this.init();
        }

        init() {
            this.loadProgress();
            this.checkboxes.forEach(checkbox => {
                checkbox.addEventListener('change', () => this.saveProgress());
            });
        }

        loadProgress() {
            const chapterUrl = window.location.pathname;
            const progress = JSON.parse(localStorage.getItem(`objectives-${chapterUrl}`) || '{}');
            
            this.checkboxes.forEach((checkbox, index) => {
                if (progress[index]) {
                    checkbox.checked = true;
                }
            });
        }

        saveProgress() {
            const chapterUrl = window.location.pathname;
            const progress = {};
            
            this.checkboxes.forEach((checkbox, index) => {
                progress[index] = checkbox.checked;
            });
            
            localStorage.setItem(`objectives-${chapterUrl}`, JSON.stringify(progress));
        }
    }

    // ===== INITIALIZATION =====
    
    function initializeApp() {
        // Initialize all managers
        new ThemeManager();
        new SearchManager();
        new NavigationManager();
        new ReadingProgressManager();
        new TableOfContentsManager();
        new BackToTopManager();
        new CodeManager();
        new FloatingActionsManager();
        new FeedbackManager();
        new LearningObjectivesManager();

        // Add loading animation styles
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
        `;
        document.head.appendChild(style);

        console.log('Python Book app initialized successfully! 🐍');
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeApp);
    } else {
        initializeApp();
    }

})();