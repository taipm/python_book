# Kế hoạch viết sách "Lập trình Python cơ bản"

## 🎯 Mục tiêu tổng quan
Viết một cuốn sách hướng dẫn lập trình Python cơ bản dành cho người mới bắt đầu, sử dụng GitHub Docs để xuất bản và chia sẻ. Sách cần có nội dung dễ hiểu, ví dụ thực tế và bài tập ứng dụng.

## 📚 Đối tượng độc giả
- Người mới bắt đầu học lập trình, chưa có kinh nghiệm.
- Sinh viên, học sinh cần tài liệu học tập môn Python.
- Người chuyển từ ngôn ngữ lập trình khác sang Python.
- Những ai muốn tự học Python một cách có hệ thống và bài bản.

## 🏗️ Cấu trúc sách

### Phần 1: Giới thiệu và Cài đặt (Chương 1-2)
**Chương 1: Giới thiệu về Python**
- Python là gì và tại sao nên học Python?
- Lịch sử và triết lý của Python (The Zen of Python).
- Ứng dụng của Python trong các lĩnh vực: Web, Data Science, AI, Automation...
- So sánh Python với các ngôn ngữ phổ biến khác (JavaScript, Java, C++).

**Chương 2: Cài đặt và Thiết lập môi trường**
- Hướng dẫn cài đặt Python trên Windows, macOS, và Linux.
- Giới thiệu về các công cụ:
  - Python IDLE: Trình thông dịch mặc định.
  - Text Editors: VS Code (khuyến khích), Sublime Text.
  - IDEs: PyCharm.
- Hướng dẫn sử dụng `pip` để quản lý thư viện.
- Giới thiệu và cách tạo môi trường ảo (`venv`).

### Phần 2: Nền tảng cơ bản (Chương 3-8)
**Chương 3: Cú pháp cơ bản và Biến**
- Cú pháp và cấu trúc một chương trình Python.
- Ghi chú (comments) trong code.
- Biến và quy tắc đặt tên biến.
- Các kiểu dữ liệu cơ bản: `int`, `float`, `str`, `bool`.
- Hàm `input()` và `print()` để tương tác với người dùng.

**Chương 4: Chuỗi (Strings)**
- Tạo và làm việc với chuỗi.
- Các phương thức chuỗi phổ biến (`upper`, `lower`, `strip`, `split`...).
- Truy cập ký tự (indexing) và cắt chuỗi (slicing).
- Định dạng chuỗi: f-strings (khuyến khích), phương thức `format()`.

**Chương 5: Cấu trúc dữ liệu (Lists, Tuples, Sets)**
- **Lists**: Tạo, truy cập, thay đổi, và các phương thức (`append`, `pop`, `sort`...).
- **Tuples**: Đặc điểm và khi nào nên sử dụng.
- **Sets**: Các thao tác cơ bản và ứng dụng (tìm phần tử duy nhất).
- List Comprehension: Cú pháp viết code ngắn gọn và hiệu quả.

**Chương 6: Dictionaries**
- Cấu trúc key-value.
- Tạo, truy cập, và thay đổi dictionary.
- Các phương thức phổ biến (`keys`, `values`, `items`).
- Lặp qua dictionary.

**Chương 7: Câu lệnh điều kiện**
- Câu lệnh `if`, `elif`, `else`.
- Toán tử so sánh (`==`, `!=`, `>`, `<`...) và toán tử logic (`and`, `or`, `not`).
- Câu lệnh điều kiện lồng nhau (nested conditions).
- Toán tử ba ngôi (Ternary operator).

**Chương 8: Vòng lặp**
- Vòng lặp `for` và vòng lặp `while`.
- Hàm `range()`.
- Các từ khóa `break` và `continue`.
- Vòng lặp lồng nhau (nested loops).
- Kết hợp vòng lặp với `else`.

### Phần 3: Kỹ thuật nâng cao (Chương 9-14)
**Chương 9: Hàm (Functions)**
- Định nghĩa và gọi hàm.
- Tham số (parameters) và đối số (arguments).
- Giá trị trả về (`return`).
- Phạm vi của biến: local vs global.
- Tham số mặc định, `*args`, và `**kwargs`.
- Docstrings và Type Hints.
- Hàm Lambda.

**Chương 10: Xử lý ngoại lệ (Exception Handling)**
- Giới thiệu về lỗi (errors) và ngoại lệ (exceptions).
- Cấu trúc `try...except...else...finally`.
- Bắt các loại exception cụ thể.
- Từ khóa `raise` để tạo ra exception.

**Chương 11: Làm việc với File**
- Đọc và ghi file text (`.txt`).
- Các chế độ mở file (`r`, `w`, `a`).
- Sử dụng `with` statement để quản lý file an toàn.
- Làm việc với file CSV và JSON.
- Giới thiệu thư viện `pathlib` để làm việc với đường dẫn.

**Chương 12: Module và Package**
- `import` module có sẵn trong thư viện chuẩn.
- Cách tạo và sử dụng module của riêng bạn.
- Cấu trúc một package với `__init__.py`.
- Giới thiệu một vài thư viện chuẩn hữu ích: `os`, `sys`, `datetime`, `random`.

**Chương 13: Lập trình hướng đối tượng (OOP)**
- Khái niệm về Class và Object.
- Thuộc tính (attributes) và phương thức (methods).
- Hàm khởi tạo `__init__`.
- Kế thừa (Inheritance).
- Đóng gói (Encapsulation): public, protected, private.
- Đa hình (Polymorphism) và các phương thức đặc biệt (dunder methods).

**Chương 14: Giới thiệu các thư viện phổ biến**
- `requests`: Gửi HTTP requests để tương tác với web API.
- `BeautifulSoup`: Phân tích HTML để trích xuất dữ liệu (web scraping).
- `Pillow`: Xử lý ảnh cơ bản.
- `Matplotlib`: Vẽ biểu đồ và trực quan hóa dữ liệu.

### Phần 4: Dự án thực hành (Chương 15-17)
**Chương 15: Dự án 1 - To-Do List App (Command-line)**
- Áp dụng kiến thức về file, list, và vòng lặp.
- Xây dựng ứng dụng quản lý công việc trên giao diện dòng lệnh.

**Chương 16: Dự án 2 - Web Scraper đơn giản**
- Sử dụng `requests` và `BeautifulSoup`.
- Trích xuất thông tin từ một trang web (ví dụ: tin tức, giá sản phẩm).

**Chương 17: Dự án 3 - Ứng dụng Web với Flask**
- Giới thiệu về web framework Flask.
- Xây dựng một trang web đơn giản hiển thị "Hello, World!" và một vài thông tin cơ bản.

### Phần 5: Bài tập và Lời giải
**Chương 18: Bài tập thực hành - Giải phương trình bậc hai**
- Vận dụng kiến thức về biến, hàm, câu lệnh điều kiện và xử lý lỗi.
- Lời giải chi tiết và giải thích code.

## 📅 Kế hoạch xuất bản
- **Viết và review**: Tháng 7 - Tháng 9, 2025.
- **Hoàn thiện và xuất bản**: Tháng 10, 2025.
- **Kênh xuất bản**: GitHub Pages (sử dụng Jekyll).

### Về tác giả

Thông tin chi tiết về tác giả có thể được tìm thấy trong file `author.md`.
