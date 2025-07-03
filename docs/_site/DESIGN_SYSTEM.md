# 🎨 Design System - Python Book

## Tổng quan

Website Python Book đã được nâng cấp hoàn toàn với một design system hiện đại, chuyên nghiệp và tối ưu trải nghiệm người dùng.

## 🌟 Tính năng chính

### 1. Giao diện hiện đại
- **Dark/Light Mode**: Tự động chuyển đổi theo preference của user
- **Typography**: Sử dụng Inter font cho text và JetBrains Mono cho code
- **Color System**: Palette màu nhất quán với Python branding
- **Responsive Design**: Tối ưu cho mọi thiết bị

### 2. Trải nghiệm đọc nâng cao
- **Reading Progress**: Thanh tiến độ đọc realtime
- **Table of Contents**: Tự động generate và scroll spy
- **Bookmark System**: Lưu trang yêu thích
- **Notes Feature**: Ghi chú cá nhân cho từng chương

### 3. Code Experience
- **Syntax Highlighting**: GitHub-style với theme sáng/tối
- **Copy Code**: 1-click copy với feedback
- **Interactive Blocks**: Chạy code trực tiếp (planned)
- **Language Labels**: Hiển thị ngôn ngữ programming

### 4. Navigation & Search
- **Smart Search**: Tìm kiếm nội dung với keyboard shortcut (Ctrl+K)
- **Chapter Navigation**: Previous/Next với preview
- **Breadcrumbs**: Định hướng vị trí hiện tại
- **Mobile Menu**: Hamburger menu responsive

## 🎨 Design Tokens

### Colors
```css
/* Primary Colors */
--color-primary: #3776ab;        /* Python Blue */
--color-secondary: #ffd43b;      /* Python Yellow */

/* Semantic Colors */
--color-success: #28a745;
--color-warning: #ffc107;
--color-error: #dc3545;
--color-info: #17a2b8;

/* Text Colors */
--color-text: #2c3e50;           /* Dark theme: #e2e8f0 */
--color-text-light: #6c757d;     /* Dark theme: #a0aec0 */
--color-text-muted: #95a5a6;     /* Dark theme: #718096 */

/* Background Colors */
--color-bg: #ffffff;             /* Dark theme: #1a202c */
--color-bg-secondary: #f8f9fa;   /* Dark theme: #2d3748 */
--color-bg-tertiary: #e9ecef;    /* Dark theme: #4a5568 */
```

### Typography
```css
/* Font Families */
--font-family-base: 'Inter', sans-serif;
--font-family-mono: 'JetBrains Mono', monospace;

/* Font Sizes */
--font-size-xs: 0.75rem;    /* 12px */
--font-size-sm: 0.875rem;   /* 14px */
--font-size-base: 1rem;     /* 16px */
--font-size-lg: 1.125rem;   /* 18px */
--font-size-xl: 1.25rem;    /* 20px */
--font-size-2xl: 1.5rem;    /* 24px */
--font-size-3xl: 1.875rem;  /* 30px */
--font-size-4xl: 2.25rem;   /* 36px */

/* Font Weights */
--font-weight-light: 300;
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Spacing
```css
--spacing-xs: 0.25rem;   /* 4px */
--spacing-sm: 0.5rem;    /* 8px */
--spacing-md: 1rem;      /* 16px */
--spacing-lg: 1.5rem;    /* 24px */
--spacing-xl: 2rem;      /* 32px */
--spacing-2xl: 3rem;     /* 48px */
--spacing-3xl: 4rem;     /* 64px */
```

### Border Radius
```css
--radius-sm: 0.25rem;    /* 4px */
--radius-md: 0.5rem;     /* 8px */
--radius-lg: 0.75rem;    /* 12px */
--radius-xl: 1rem;       /* 16px */
--radius-full: 9999px;   /* Full rounded */
```

## 📱 Responsive Breakpoints

```css
/* Mobile First Approach */
@media (max-width: 480px)  { /* Mobile */ }
@media (max-width: 768px)  { /* Tablet */ }
@media (max-width: 1024px) { /* Desktop */ }
@media (max-width: 1200px) { /* Large Desktop */ }
```

## 🧩 Components

### 1. Buttons
```html
<!-- Primary Button -->
<a href="#" class="btn btn-primary">
    <i class="fas fa-play"></i> Bắt đầu học
</a>

<!-- Secondary Button -->
<a href="#" class="btn btn-secondary">Tìm hiểu thêm</a>

<!-- Outline Button -->
<a href="#" class="btn btn-outline">Xem chi tiết</a>

<!-- Large Button -->
<a href="#" class="btn btn-primary btn-large">Call to Action</a>
```

### 2. Cards
```html
<!-- Feature Card -->
<div class="feature-card">
    <div class="feature-icon">🚀</div>
    <h3>Tiêu đề</h3>
    <p>Mô tả tính năng...</p>
</div>

<!-- Chapter Card -->
<div class="start-card">
    <div class="card-header">
        <span class="chapter-number">01</span>
        <div class="card-meta">
            <span class="difficulty beginner">Cơ bản</span>
            <span class="reading-time">15 phút</span>
        </div>
    </div>
    <h3>Tiêu đề chương</h3>
    <p>Mô tả nội dung...</p>
    <div class="card-footer">
        <a href="#" class="btn btn-primary">Đọc chương</a>
    </div>
</div>
```

### 3. Code Blocks
```html
<!-- Basic Code Block -->
<div class="highlight">
    <pre><code class="language-python">
print("Hello, World!")
    </code></pre>
</div>

<!-- Code with Title -->
<div class="code-example">
    <div class="code-title">hello.py</div>
    <div class="highlight">
        <pre><code class="language-python">
print("Hello, World!")
        </code></pre>
    </div>
</div>

<!-- Interactive Code -->
<div class="interactive-code">
    <div class="code-header">
        <span class="code-title">Thử ngay</span>
        <button class="run-btn">Chạy code</button>
    </div>
    <div class="highlight">
        <pre><code class="language-python">
# Code có thể chạy
print("Interactive Python!")
        </code></pre>
    </div>
</div>
```

### 4. Badges & Status
```html
<!-- Difficulty Badges -->
<span class="difficulty beginner">Cơ bản</span>
<span class="difficulty intermediate">Trung bình</span>
<span class="difficulty advanced">Nâng cao</span>

<!-- Status Badges -->
<span class="chapter-status status-available">Sẵn sàng</span>
<span class="chapter-status status-coming-soon">Sắp có</span>
```

## 🎯 Layout System

### 1. Home Layout
- Hero section với gradient background
- Features grid với hover effects
- Quick start cards với featured highlighting
- Curriculum overview với status indicators
- Learning paths với recommendations
- Call-to-action section

### 2. Chapter Layout
- Chapter header với metadata
- Learning objectives checklist
- Prerequisites information
- Sidebar với TOC và progress
- Reading progress indicator
- Floating action buttons
- Chapter navigation
- Feedback system

### 3. Default Layout
- Sticky header với navigation
- Search overlay
- Theme toggle
- Mobile-responsive menu
- Footer với links
- Back-to-top button

## 🚀 Performance Features

### 1. Loading Optimization
- CSS variables cho theme switching
- Font preloading
- Lazy loading cho images
- Minified assets

### 2. User Experience
- Smooth scrolling
- Transition animations
- Loading states
- Error handling
- Accessibility support

### 3. Progressive Enhancement
- Works without JavaScript
- Graceful degradation
- Print-friendly styles
- SEO optimized

## 📚 Usage Guidelines

### 1. Theme Implementation
```javascript
// Theme switching
const theme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', theme);
```

### 2. Component Usage
- Sử dụng CSS classes có sẵn
- Tuân thủ naming convention
- Responsive-first approach
- Accessibility considerations

### 3. Content Guidelines
- Sử dụng emoji phù hợp
- Consistent tone of voice
- Clear hierarchy
- Actionable content

## 🔧 Development

### File Structure
```
docs/
├── _layouts/
│   ├── default.html      # Base layout
│   ├── home.html         # Homepage layout
│   └── chapter.html      # Chapter layout
├── assets/
│   ├── css/
│   │   ├── main.css      # Main styles
│   │   └── syntax.css    # Code highlighting
│   ├── js/
│   │   └── main.js       # JavaScript functionality
│   └── images/
│       └── favicon.svg   # Site icon
└── _config.yml           # Jekyll configuration
```

### Build Process
1. Jekyll processes Markdown files
2. Liquid templates render layouts
3. CSS/JS assets are served
4. GitHub Pages deployment

## 🎨 Customization

### Adding New Colors
```css
:root {
    --color-custom: #your-color;
}

[data-theme="dark"] {
    --color-custom: #your-dark-color;
}
```

### Creating New Components
1. Follow BEM methodology
2. Use CSS variables
3. Ensure responsive design
4. Add dark theme support
5. Test accessibility

### Extending Layouts
1. Create new layout in `_layouts/`
2. Extend from `default.html`
3. Add specific styles
4. Update navigation if needed

## 📖 Best Practices

### 1. CSS
- Mobile-first responsive design
- Use CSS custom properties
- Consistent naming convention
- Modular architecture

### 2. JavaScript
- Progressive enhancement
- Event delegation
- Performance optimization
- Error handling

### 3. Content
- Semantic HTML structure
- Proper heading hierarchy
- Alt text for images
- Keyboard navigation support

## 🚀 Future Enhancements

### Planned Features
- [ ] Advanced search with filters
- [ ] Code playground integration
- [ ] Progress tracking across sessions
- [ ] Social sharing improvements
- [ ] Offline reading support
- [ ] Multi-language support
- [ ] Interactive exercises
- [ ] Video integration
- [ ] Community features
- [ ] Analytics dashboard

### Technical Improvements
- [ ] Service Worker for caching
- [ ] WebP image optimization
- [ ] Critical CSS inlining
- [ ] Bundle optimization
- [ ] Performance monitoring
- [ ] A11y testing automation

---

**Design System Version**: 1.0.0  
**Last Updated**: January 2025  
**Maintainer**: Tai PM