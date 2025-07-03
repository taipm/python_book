---
title: "Lời giải Bài tập Chương 2"
layout: chapter
---

Các bài tập trong chương 2 là các nhiệm vụ thực hành trên máy tính cá nhân của bạn. Không có "đáp án" duy nhất, nhưng dưới đây là các kết quả mong đợi bạn nên đạt được:

**Nhiệm vụ 1: Kiểm tra phiên bản**
- Bạn có thể chạy lệnh `python3 --version` hoặc `python --version`.
- Kết quả mong đợi là một dòng chữ hiện ra, ví dụ: `Python 3.11.5`.

**Nhiệm vụ 2: Chạy chương trình đầu tiên**
- Sau khi chạy lệnh `python3 greeting.py`, terminal sẽ in ra đúng tên và quê quán bạn đã viết trong file.

**Nhiệm vụ 3: Làm quen với VS Code**
- Bạn có thể mở thư mục dự án và chạy file Python thành công từ giao diện của VS Code. Cửa sổ "TERMINAL" trong VS Code sẽ hiện ra kết quả tương tự như khi bạn chạy ở Nhiệm vụ 2.

**Nhiệm vụ 4: Thực hành với môi trường ảo**
- Bạn tạo thành công thư mục `my_env`.
- Dòng lệnh của bạn có `(my_env)` ở phía trước sau khi kích hoạt.
- Lệnh `pip list` cho thấy thư viện `numpy` (và một vài thư viện ph��� thuộc khác) đã được cài đặt.
- Sau khi `deactivate`, `(my_env)` biến mất và `pip list` (nếu chạy lại) sẽ không còn thấy `numpy` nữa (nếu trước đó bạn chưa cài `numpy` ở môi trường global).