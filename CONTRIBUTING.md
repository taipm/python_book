# Hướng dẫn đóng góp - Python Book

Cảm ơn bạn quan tâm đến việc đóng góp cho dự án "Lập trình Python cơ bản"! 

## 🎯 Các cách đóng góp

### 📝 Viết nội dung
- Viết/chỉnh sửa các chương
- Tạo bài tập và ví dụ
- Kiểm tra và sửa lỗi chính tả
- Cải thiện cách giải thích

### 🐛 Báo cáo lỗi
- Lỗi trong code examples
- Lỗi chính tả/ngữ pháp
- Links không hoạt động
- Vấn đề về formatting

### 💡 Đề xuất cải tiến
- Ý tưởng cho nội dung mới
- Cải thiện cấu trúc
- Tools và resources hữu ích
- Feedback về trải nghiệm đọc

## 🔧 Quy trình đóng góp

### 1. Fork Repository
```bash
# Click Fork trên GitHub hoặc:
gh repo fork taipm/python_book
```

### 2. Clone về máy
```bash
git clone https://github.com/YOUR-USERNAME/python_book.git
cd python_book
```

### 3. Tạo branch mới
```bash
git checkout -b feature/your-feature-name
# hoặc
git checkout -b fix/bug-description
```

### 4. Thực hiện thay đổi
- Viết/sửa nội dung
- Test code examples
- Commit thường xuyên

### 5. Commit changes
```bash
git add .
git commit -m "feat: thêm ví dụ cho chương 5"
# hoặc
git commit -m "fix: sửa lỗi code trong chương 3"
```

### 6. Push và tạo PR
```bash
git push origin feature/your-feature-name
```
Sau đó tạo Pull Request trên GitHub.

## 📋 Coding Standards

### Markdown Style
- Sử dụng heading levels đúng thứ tự (h1 → h2 → h3)
- Dòng trống giữa sections
- Lists có indentation nhất quán
- Code blocks có syntax highlighting

### Python Code Style
- Follow PEP 8
- Comments bằng tiếng Việt
- Variable names tiếng Anh nhưng descriptive
- Include docstrings cho functions

### Content Guidelines
- Ngôn ngữ đơn giản, dễ hiểu
- Ví dụ thực tế, gần gũi
- Giải thích step-by-step
- Include output cho code examples

## 🗂️ Cấu trúc file

### Chapters
```markdown
# Chương X: Tên chương

## Mục tiêu học tập
- Mục tiêu 1
- Mục tiêu 2

## Nội dung chính
### Phần 1
### Phần 2

## Ví dụ thực hành
## Bài tập
## Tóm tắt
## Đọc thêm
```

### Code Examples
```python
# Filename: descriptive_name.py
# Chapter: X
# Description: Mô tả ngắn gọn

def main():
    """Hàm chính của chương trình."""
    # Code implementation
    pass

if __name__ == "__main__":
    main()
```

## ✅ Checklist trước khi submit

### Content
- [ ] Spelling và grammar check
- [ ] Code examples đã test
- [ ] Links hoạt động
- [ ] Formatting đúng markdown style
- [ ] Cross-references cập nhật

### Technical
- [ ] Branch up-to-date với main
- [ ] No merge conflicts
- [ ] Descriptive commit messages
- [ ] PR description rõ ràng

## 🎨 Style Guide

### Terminology
| Tiếng Anh | Tiếng Việt |
|-----------|------------|
| Function | Hàm |
| Variable | Biến |
| String | Chuỗi |
| List | Danh sách |
| Loop | Vòng lặp |
| Condition | Điều kiện |

### Code Comments
```python
# Tốt ✅
def tinh_tong(a, b):
    """Tính tổng của hai số."""
    return a + b

# Không tốt ❌
def calculate_sum(x, y):
    # calculate sum
    return x + y
```

## 🚀 Development Setup

### Requirements
- Python 3.8+
- Git
- Text editor (VS Code recommended)
- GitHub account

### Local Testing
```bash
# Test Python examples
python code-examples/chapter01/example01.py

# Check markdown
markdownlint chapters/*.md

# Preview GitHub Pages locally (optional)
bundle exec jekyll serve
```

## 📞 Liên hệ

- **Issues**: [GitHub Issues](https://github.com/taipm/python_book/issues)
- **Discussions**: [GitHub Discussions](https://github.com/taipm/python_book/discussions)
- **Email**: tai.pm@example.com

## 🙏 Cảm ơn

Mọi đóng góp đều được ghi nhận trong:
- Contributors section
- Commit history
- Release notes

**Happy coding! 🐍**
