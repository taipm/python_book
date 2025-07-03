# Chương 2: Cài đặt môi trường

## 🎯 Mục tiêu học tập

Sau khi hoàn thành chương này, bạn sẽ có thể:

- [ ] Cài đặt Python trên máy tính của bạn
- [ ] Thiết lập môi trường phát triển
- [ ] Chạy chương trình Python đầu tiên
- [ ] Làm quen với Python IDLE và các editor

## 📖 Kiến thức cần có

- Hoàn thành [Chương 1: Giới thiệu về Python](chapter01.md)
- Máy tính có kết nối internet
- Quyền admin để cài đặt phần mềm

## 🔧 Cài đặt Python

### Windows

1. Truy cập [python.org](https://python.org)
2. Click "Download Python 3.x.x"
3. Chạy file installer
4. **Quan trọng**: Check "Add Python to PATH"
5. Click "Install Now"

### macOS

```bash
# Sử dụng Homebrew (recommended)
brew install python

# Hoặc download từ python.org
```

### Linux

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip
```

## ✅ Kiểm tra cài đặt

Mở Terminal/Command Prompt và chạy:

```bash
python --version
# hoặc
python3 --version
```

Nếu thấy "Python 3.x.x" là thành công!

## 🚀 Chương trình đầu tiên

Tạo file `hello.py`:

```python
print("Xin chào, Python!")
print("Tôi đã cài đặt thành công!")
```

Chạy:
```bash
python hello.py
```

## ➡️ Chương tiếp theo

Trong [Chương 3: Cú pháp cơ bản](chapter03.md), chúng ta sẽ học:
- Variables và data types
- Input/Output operations
- Comments và documentation

---

*Chương đang được phát triển...*
