---
title: "Lời giải Bài tập Chương 1"
layout: chapter
---

### Câu hỏi Trắc nghiệm

**Câu 1: C. Guido van Rossum**
- Guido van Rossum là người đã tạo ra Python vào cuối những năm 1980.

**Câu 2: B. Một chương trình hài kịch trên TV**
- Tên "Python" được lấy từ chương trình "Monty Python's Flying Circus" của đài BBC.

**Câu 3: B. Cần biên dịch trước khi chạy**
- Python là ngôn ngữ thông dịch (interpreted), tức là code được thực thi trực tiếp mà không cần qua bước biên dịch như C++ hay Java.

**Câu 4: C. Python 3.x**
- Python 2 đã chính thức ngừng hỗ trợ vào năm 2020. Mọi dự án mới đều nên bắt đầu với Python 3.

**Câu 5: B. `import this`**
- Chạy lệnh này trong Python sẽ hiển thị 19 nguyên tắc của "The Zen of Python".

### Câu hỏi Tự luận

**Câu 6:** Ba lý do người mới nên học Python:
1.  **Dễ học, dễ đọc:** Cú pháp của Python rất gần với ngôn ngữ tự nhiên, giúp người mới tập trung vào tư duy giải quyết vấn đề thay vì phải v���t lộn với các cú pháp phức tạp.
2.  **Cộng đồng lớn và hỗ trợ mạnh mẽ:** Khi gặp vấn đề, bạn có thể dễ dàng tìm thấy câu trả lời trên các diễn đàn như Stack Overflow, Reddit, hoặc các nhóm cộng đồng. Có vô số thư viện sẵn có giúp bạn không phải "phát minh lại bánh xe".
3.  **Ứng dụng đa dạng:** Học một ngôn ngữ nhưng có thể làm được rất nhiều việc (web, AI, data science, game, automation...). Điều này tạo ra nhiều cơ hội nghề nghiệp và giúp người học không bị giới hạn trong một lĩnh vực hẹp.

**Câu 7:** Ba lĩnh vực ứng dụng mạnh mẽ của Python:
1.  **Phát triển Web (Web Development):**
    - *Framework phổ biến:* Django, Flask, FastAPI.
2.  **Khoa học Dữ liệu (Data Science):**
    - *Thư viện phổ biến:* Pandas (xử lý dữ liệu), NumPy (tính toán số), Matplotlib/Seaborn (vẽ biểu đồ).
3.  **Trí tuệ Nhân tạo & Học máy (AI & Machine Learning):**
    - *Thư viện phổ biến:* TensorFlow, PyTorch, Scikit-learn.

### Bài tập thực hành

**Câu 8:**
- Để tìm phiên bản mới nhất, bạn truy cập [https://www.python.org/downloads/](https://www.python.org/downloads/). Tại thời điểm viết bài, phiên bản ổn định mới nhất thường được hiển thị nổi bật ngay trên đầu trang.

### Lời giải Bài tập Lập trình

**Bài 1:**
```python
ten = input("Nhập tên của bạn: ")
print("Xin chào", ten)
```

**Bài 2:**
```python
ten = input("Nhập tên của bạn: ")
ho = input("Nhập họ của bạn: ")
print("Xin chào", ten, ho)
```

**Bài 3:**
```python
print("Bạn gọi một con gấu không có răng là gì?\nMột con gấu gummy!")
```

**Bài 4:**
```python
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
tong = so1 + so2
print("Tổng là", tong)
```

**Bài 5:**
```python
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
so3 = int(input("Nhập số thứ ba: "))
ket_qua = (so1 + so2) * so3
print("Kết quả là", ket_qua)
```

**Bài 6:**
```python
so_lat_ban_dau = int(input("Bạn có bao nhiêu lát pizza? "))
so_lat_da_an = int(input("Bạn đã ăn bao nhiêu lát? "))
so_lat_con_lai = so_lat_ban_dau - so_lat_da_an
print("Bạn còn lại", so_lat_con_lai, "lát pizza.")
```

**Bài 7:**
```python
ten = input("Tên bạn là gì? ")
tuoi = int(input("Bạn bao nhiêu tuổi? "))
tuoi_moi = tuoi + 1
print(ten, "vào sinh nhật tới bạn sẽ", tuoi_moi, "tuổi.")
```

**Bài 8:**
```python
tong_hoa_don = float(input("Tổng hóa đơn là bao nhiêu? "))
so_nguoi_an = int(input("Có bao nhiêu người ăn? "))
moi_nguoi_tra = tong_hoa_don / so_nguoi_an
print("Mỗi người phải trả", moi_nguoi_tra)
```

**Bài 9:**
```python
so_ngay = int(input("Nhập số ngày: "))
gio = so_ngay * 24
phut = gio * 60
giay = phut * 60
print("Trong", so_ngay, "ngày có:")
print("- ", gio, "giờ")
print("- ", phut, "phút")
print("- ", giay, "giây")
```

**Bài 10:**
```python
kg = float(input("Nhập cân nặng (kg): "))
pounds = kg * 2.204
print("Trọng lượng tương ứng là", pounds, "pounds.")
```

**Bài 11:**
```python
so_lon = int(input("Nhập một số lớn hơn 100: "))
so_nho = int(input("Nhập một số nhỏ hơn 10: "))
so_lan = so_lon // so_nho
print("Số", so_nho, "chứa trong số", so_lon, "được", so_lan, "lần.")
```
