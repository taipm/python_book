#!/usr/bin/env python3
"""
Python Book Website Optimization Script
Tối ưu hóa performance và SEO cho website
"""

import os
import sys
import json
import gzip
import shutil
from pathlib import Path
from typing import Dict, List, Optional
import subprocess
import time

class WebsiteOptimizer:
    """Tối ưu hóa website Python Book"""
    
    def __init__(self, docs_dir: str = "docs"):
        self.docs_dir = Path(docs_dir)
        self.build_dir = self.docs_dir / "_site"
        self.assets_dir = self.docs_dir / "assets"
        
        # Statistics
        self.stats = {
            "files_processed": 0,
            "bytes_saved": 0,
            "errors": []
        }
    
    def run_optimization(self):
        """Chạy tất cả optimizations"""
        print("🚀 Bắt đầu tối ưu hóa Python Book website...")
        start_time = time.time()
        
        try:
            # 1. Kiểm tra môi trường
            self.check_environment()
            
            # 2. Build Jekyll site
            self.build_jekyll_site()
            
            # 3. Tối ưu CSS
            self.optimize_css()
            
            # 4. Tối ưu JavaScript
            self.optimize_javascript()
            
            # 5. Tối ưu hình ảnh
            self.optimize_images()
            
            # 6. Tạo gzip files
            self.create_gzip_files()
            
            # 7. Generate sitemap
            self.generate_sitemap()
            
            # 8. Validate HTML
            self.validate_html()
            
            # 9. Performance audit
            self.performance_audit()
            
            # 10. Báo cáo kết quả
            self.print_report(time.time() - start_time)
            
        except Exception as e:
            print(f"❌ Lỗi trong quá trình tối ưu: {e}")
            sys.exit(1)
    
    def check_environment(self):
        """Kiểm tra môi trường và dependencies"""
        print("🔍 Kiểm tra môi trường...")
        
        # Kiểm tra Jekyll
        try:
            subprocess.run(["jekyll", "--version"], 
                         capture_output=True, check=True)
            print("✅ Jekyll đã cài đặt")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Jekyll chưa được cài đặt")
            print("Cài đặt: gem install jekyll bundler")
            sys.exit(1)
        
        # Kiểm tra thư mục docs
        if not self.docs_dir.exists():
            print(f"❌ Không tìm thấy thư mục {self.docs_dir}")
            sys.exit(1)
        
        print("✅ Môi trường OK")
    
    def build_jekyll_site(self):
        """Build Jekyll site"""
        print("🏗️ Building Jekyll site...")
        
        try:
            result = subprocess.run(
                ["jekyll", "build", "--source", str(self.docs_dir)],
                capture_output=True,
                text=True,
                check=True
            )
            print("✅ Jekyll build thành công")
        except subprocess.CalledProcessError as e:
            print(f"❌ Jekyll build thất bại: {e.stderr}")
            sys.exit(1)
    
    def optimize_css(self):
        """Tối ưu CSS files"""
        print("🎨 Tối ưu CSS...")
        
        css_files = list(self.build_dir.rglob("*.css"))
        
        for css_file in css_files:
            try:
                # Đọc file CSS
                content = css_file.read_text(encoding='utf-8')
                original_size = len(content)
                
                # Minify CSS (basic)
                minified = self.minify_css(content)
                
                # Ghi lại file
                css_file.write_text(minified, encoding='utf-8')
                
                # Cập nhật stats
                saved = original_size - len(minified)
                self.stats["bytes_saved"] += saved
                self.stats["files_processed"] += 1
                
                print(f"  ✅ {css_file.name}: -{saved} bytes")
                
            except Exception as e:
                error_msg = f"Lỗi tối ưu CSS {css_file}: {e}"
                self.stats["errors"].append(error_msg)
                print(f"  ❌ {error_msg}")
    
    def minify_css(self, css_content: str) -> str:
        """Minify CSS content (basic implementation)"""
        import re
        
        # Remove comments
        css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
        
        # Remove extra whitespace
        css_content = re.sub(r'\s+', ' ', css_content)
        
        # Remove whitespace around specific characters
        css_content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', css_content)
        
        # Remove trailing semicolons
        css_content = re.sub(r';}', '}', css_content)
        
        return css_content.strip()
    
    def optimize_javascript(self):
        """Tối ưu JavaScript files"""
        print("⚡ Tối ưu JavaScript...")
        
        js_files = list(self.build_dir.rglob("*.js"))
        
        for js_file in js_files:
            try:
                # Đọc file JS
                content = js_file.read_text(encoding='utf-8')
                original_size = len(content)
                
                # Basic minification
                minified = self.minify_js(content)
                
                # Ghi lại file
                js_file.write_text(minified, encoding='utf-8')
                
                # Cập nhật stats
                saved = original_size - len(minified)
                self.stats["bytes_saved"] += saved
                self.stats["files_processed"] += 1
                
                print(f"  ✅ {js_file.name}: -{saved} bytes")
                
            except Exception as e:
                error_msg = f"Lỗi tối ưu JS {js_file}: {e}"
                self.stats["errors"].append(error_msg)
                print(f"  ❌ {error_msg}")
    
    def minify_js(self, js_content: str) -> str:
        """Minify JavaScript content (basic implementation)"""
        import re
        
        # Remove single-line comments (but preserve URLs)
        js_content = re.sub(r'(?<!:)//.*$', '', js_content, flags=re.MULTILINE)
        
        # Remove multi-line comments
        js_content = re.sub(r'/\*.*?\*/', '', js_content, flags=re.DOTALL)
        
        # Remove extra whitespace
        js_content = re.sub(r'\s+', ' ', js_content)
        
        # Remove whitespace around operators
        js_content = re.sub(r'\s*([{}();,=+\-*/<>!&|])\s*', r'\1', js_content)
        
        return js_content.strip()
    
    def optimize_images(self):
        """Tối ưu hình ảnh"""
        print("🖼️ Tối ưu hình ảnh...")
        
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.svg']
        image_files = []
        
        for ext in image_extensions:
            image_files.extend(self.build_dir.rglob(f"*{ext}"))
        
        for image_file in image_files:
            try:
                original_size = image_file.stat().st_size
                
                # Tối ưu dựa trên loại file
                if image_file.suffix.lower() == '.svg':
                    self.optimize_svg(image_file)
                
                # Cập nhật stats
                new_size = image_file.stat().st_size
                saved = original_size - new_size
                
                if saved > 0:
                    self.stats["bytes_saved"] += saved
                    self.stats["files_processed"] += 1
                    print(f"  ✅ {image_file.name}: -{saved} bytes")
                
            except Exception as e:
                error_msg = f"Lỗi tối ưu image {image_file}: {e}"
                self.stats["errors"].append(error_msg)
                print(f"  ❌ {error_msg}")
    
    def optimize_svg(self, svg_file: Path):
        """Tối ưu SVG file"""
        import re
        
        content = svg_file.read_text(encoding='utf-8')
        
        # Remove comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        
        # Remove extra whitespace
        content = re.sub(r'\s+', ' ', content)
        content = re.sub(r'>\s+<', '><', content)
        
        svg_file.write_text(content.strip(), encoding='utf-8')
    
    def create_gzip_files(self):
        """Tạo gzip files cho static assets"""
        print("🗜️ Tạo gzip files...")
        
        # File types to gzip
        gzip_extensions = ['.html', '.css', '.js', '.json', '.xml', '.txt']
        
        for ext in gzip_extensions:
            files = list(self.build_dir.rglob(f"*{ext}"))
            
            for file_path in files:
                try:
                    # Tạo gzip version
                    gzip_path = file_path.with_suffix(file_path.suffix + '.gz')
                    
                    with open(file_path, 'rb') as f_in:
                        with gzip.open(gzip_path, 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    
                    # Kiểm tra compression ratio
                    original_size = file_path.stat().st_size
                    compressed_size = gzip_path.stat().st_size
                    ratio = (1 - compressed_size / original_size) * 100
                    
                    if ratio > 10:  # Chỉ giữ nếu tiết kiệm > 10%
                        self.stats["files_processed"] += 1
                        print(f"  ✅ {file_path.name}.gz: {ratio:.1f}% smaller")
                    else:
                        gzip_path.unlink()  # Xóa nếu không hiệu quả
                        
                except Exception as e:
                    error_msg = f"Lỗi tạo gzip {file_path}: {e}"
                    self.stats["errors"].append(error_msg)
                    print(f"  ❌ {error_msg}")
    
    def generate_sitemap(self):
        """Generate sitemap.xml"""
        print("🗺️ Tạo sitemap...")
        
        try:
            # Tìm tất cả HTML files
            html_files = list(self.build_dir.rglob("*.html"))
            
            # Tạo sitemap XML
            sitemap_content = self.create_sitemap_xml(html_files)
            
            # Ghi sitemap
            sitemap_path = self.build_dir / "sitemap.xml"
            sitemap_path.write_text(sitemap_content, encoding='utf-8')
            
            print(f"  ✅ Sitemap tạo với {len(html_files)} URLs")
            
        except Exception as e:
            error_msg = f"Lỗi tạo sitemap: {e}"
            self.stats["errors"].append(error_msg)
            print(f"  ❌ {error_msg}")
    
    def create_sitemap_xml(self, html_files: List[Path]) -> str:
        """Tạo nội dung sitemap XML"""
        from datetime import datetime
        
        base_url = "https://taipm.github.io/python_book"
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        urls = []
        for html_file in html_files:
            # Tạo relative URL
            rel_path = html_file.relative_to(self.build_dir)
            url = f"{base_url}/{rel_path}".replace("\\", "/")
            
            # Xác định priority dựa trên file
            if rel_path.name == "index.html":
                priority = "1.0"
            elif "chapter" in str(rel_path):
                priority = "0.8"
            else:
                priority = "0.6"
            
            urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{current_date}</lastmod>
    <priority>{priority}</priority>
  </url>""")
        
        return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""
    
    def validate_html(self):
        """Validate HTML files"""
        print("✅ Validate HTML...")
        
        html_files = list(self.build_dir.rglob("*.html"))
        issues = []
        
        for html_file in html_files[:5]:  # Chỉ check 5 files đầu
            try:
                content = html_file.read_text(encoding='utf-8')
                
                # Basic HTML validation
                html_issues = self.basic_html_validation(content, html_file.name)
                issues.extend(html_issues)
                
            except Exception as e:
                issues.append(f"Lỗi đọc {html_file}: {e}")
        
        if issues:
            print(f"  ⚠️ Tìm thấy {len(issues)} vấn đề HTML")
            for issue in issues[:10]:  # Chỉ hiển thị 10 đầu
                print(f"    - {issue}")
        else:
            print("  ✅ HTML validation OK")
    
    def basic_html_validation(self, content: str, filename: str) -> List[str]:
        """Basic HTML validation"""
        import re
        issues = []
        
        # Check for missing alt attributes
        img_tags = re.findall(r'<img[^>]*>', content)
        for img in img_tags:
            if 'alt=' not in img:
                issues.append(f"{filename}: <img> thiếu alt attribute")
        
        # Check for missing title
        if '<title>' not in content:
            issues.append(f"{filename}: Thiếu <title> tag")
        
        # Check for missing meta description
        if 'name="description"' not in content:
            issues.append(f"{filename}: Thiếu meta description")
        
        return issues
    
    def performance_audit(self):
        """Kiểm tra performance cơ bản"""
        print("⚡ Performance audit...")
        
        try:
            # Tính tổng kích thước files
            total_size = 0
            file_count = 0
            
            for file_path in self.build_dir.rglob("*"):
                if file_path.is_file():
                    total_size += file_path.stat().st_size
                    file_count += 1
            
            # Tính kích thước theo loại file
            css_size = sum(f.stat().st_size for f in self.build_dir.rglob("*.css"))
            js_size = sum(f.stat().st_size for f in self.build_dir.rglob("*.js"))
            html_size = sum(f.stat().st_size for f in self.build_dir.rglob("*.html"))
            
            print(f"  📊 Tổng kích thước: {total_size / 1024:.1f} KB ({file_count} files)")
            print(f"  📄 HTML: {html_size / 1024:.1f} KB")
            print(f"  🎨 CSS: {css_size / 1024:.1f} KB")
            print(f"  ⚡ JS: {js_size / 1024:.1f} KB")
            
            # Recommendations
            if css_size > 100 * 1024:  # > 100KB
                print("  ⚠️ CSS files khá lớn, cân nhắc code splitting")
            
            if js_size > 200 * 1024:  # > 200KB
                print("  ⚠️ JS files khá lớn, cân nhắc lazy loading")
                
        except Exception as e:
            print(f"  ❌ Lỗi performance audit: {e}")
    
    def print_report(self, duration: float):
        """In báo cáo kết quả"""
        print("\n" + "="*50)
        print("📊 BÁO CÁO TỐI ƯU HÓA")
        print("="*50)
        
        print(f"⏱️ Thời gian: {duration:.2f}s")
        print(f"📁 Files xử lý: {self.stats['files_processed']}")
        print(f"💾 Tiết kiệm: {self.stats['bytes_saved'] / 1024:.1f} KB")
        
        if self.stats['errors']:
            print(f"❌ Lỗi: {len(self.stats['errors'])}")
            for error in self.stats['errors'][:5]:
                print(f"   - {error}")
        
        print("\n🎉 Tối ưu hóa hoàn tất!")
        print("🚀 Website sẵn sàng deploy!")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Tối ưu Python Book website")
    parser.add_argument("--docs-dir", default="docs", 
                       help="Thư mục docs (default: docs)")
    parser.add_argument("--skip-build", action="store_true",
                       help="Bỏ qua Jekyll build")
    
    args = parser.parse_args()
    
    optimizer = WebsiteOptimizer(args.docs_dir)
    
    if args.skip_build:
        print("⏭️ Bỏ qua Jekyll build")
        optimizer.build_jekyll_site = lambda: None
    
    optimizer.run_optimization()


if __name__ == "__main__":
    main()