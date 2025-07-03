---
title: "Chương 2: Cài đặt và Thiết lập Môi trường"
description: "Hướng dẫn chi tiết cách cài đặt Python, VS Code và thiết lập môi trường lập trình chuyên nghiệp."
layout: chapter
chapter_number: 2
difficulty: beginner
reading_time: 25
objectives:
  - "Cài đặt thành công Python 3 trên Windows, macOS và Linux."
  - "Kiểm tra và xác nhận phiên bản Python đã cài đặt."
  - "Hiểu và sử dụng được Python IDLE."
  - "Cài đặt và cấu hình VS Code cho lập trình Python."
  - "Biết cách tạo và quản lý môi trường ảo (venv)."
  - "Chạy được chương trình Python đầu tiên."
prerequisites:
  - "Hoàn thành Chương 1: Giới thiệu về Python."
  - "Máy tính có kết nối internet."
  - "Quyền admin để cài đặt phần mềm."
next_chapter:
  title: "Chương 3: Cú pháp cơ bản và Biến"
  url: "/chapters/chapter03.html"
key_terms:
  - name: "Python Installer"
    definition: "Trình cài đặt Python."
  - name: "PATH"
    definition: "Biến môi trường hệ thống giúp tìm kiếm file thực thi."
  - name: "IDLE"
    definition: "Môi trường phát triển tích hợp đơn giản đi kèm Python."
  - name: "VS Code"
    definition: "Trình soạn thảo mã nguồn phổ biến và mạnh mẽ."
  - name: "venv"
    definition: "Công cụ tạo môi trường ảo, cô lập các thư viện của dự án."
  - name: "pip"
    definition: "Hệ thống quản lý gói của Python."
---

## 🚀 Giới thiệu

Chào mừng bạn đến với phần thực hành đầu tiên! Trong chương này, chúng ta sẽ cùng nhau "xây dựng xưởng làm việc" của mình. Việc cài đặt môi trường đúng cách ngay từ đầu sẽ giúp bạn học tập và làm việc hiệu quả hơn rất nhiều sau này.

Chúng ta sẽ đi qua 3 bước chính:
1.  **Cài đặt Python**: "Trái tim" của mọi thứ.
2.  **Cài đặt Editor**: Công cụ để "viết" code. Chúng ta sẽ tập trung vào **Visual Studio Code (VS Code)**, một lựa chọn cực kỳ phổ biến và mạnh mẽ.
3.  **Tạo Môi trường ảo**: "Ngôi nhà" riêng cho mỗi dự án, giúp quản lý thư viện một cách gọn gàng.

Hãy cùng bắt đầu!

## 1. Cài đặt Python

Phiên bản Python mới nhất luôn có sẵn trên trang chủ [python.org](https://python.org). Chúng tôi khuyến khích bạn sử dụng phiên bản Python 3.8 trở lên.

### Hướng dẫn cho Windows

Đây là hệ điều hành phổ biến nhất, và việc cài đặt cũng rất đơn giản.

1.  **Tải về bộ cài đặt**:
    - Truy cập [https://www.python.org/downloads/](https://www.python.org/downloads/).
    - Trang web sẽ tự động nhận diện bạn đang dùng Windows và đề xuất phiên bản phù hợp. Nhấn nút "Download Python 3.x.x".

2.  **Chạy file Installer**:
    - Mở file `.exe` bạn vừa tải về.
    - Một cửa sổ cài đặt sẽ hiện ra. Đây là bước **quan trọng nhất**:

    ![Mô tả ảnh: Cửa sổ cài đặt Python trên Windows](assets/images/ch02/windows_installer.png "Nhớ chọn Add Python to PATH")

    - **✅ Tích vào ô "Add Python 3.x to PATH"**. Việc này giúp bạn có thể gõ lệnh `python` từ bất kỳ đâu trong Command Prompt.
    - Sau đó, nhấn vào **"Install Now"**.

3.  **Hoàn tất**:
    - Chờ vài phút để quá trình cài đặt hoàn tất.
    - Sau khi xong, bạn sẽ thấy thông báo "Setup was successful".

### Hướng dẫn cho macOS

macOS đã có sẵn một phiên bản Python cũ. Tuy nhiên, chúng ta nên cài đặt phiên bản mới nhất để sử dụng. Cách tốt nhất là dùng **Homebrew**.

1.  **Cài đặt Homebrew** (nếu bạn chưa có):
    - Mở ứng dụng **Terminal**.
    - Dán lệnh sau và nhấn Enter:
      ```bash
      /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
      ```

2.  **Cài đặt Python qua Homebrew**:
    - Sau khi cài Homebrew xong, chạy lệnh sau trong Terminal:
      ```bash
      brew install python3
      ```
    - Homebrew sẽ tự động tải và cài đặt phiên bản Python 3 mới nhất.

### Hướng dẫn cho Linux (Ubuntu/Debian)

Hầu hết các bản phân phối Linux đã có sẵn Python 3. Bạn chỉ cần đảm bảo nó là phiên bản mới và cài thêm `pip` (trình quản lý gói) và `venv` (môi trường ảo).

1.  **Mở Terminal**.
2.  **Cập nhật danh sách gói**:
    ```bash
    sudo apt update
    ```
3.  **Cài đặt Python và các công cụ cần thiết**:
    ```bash
    sudo apt install python3 python3-pip python3-venv
    ```

## 2. Kiểm tra Cài đặt

Sau khi cài đặt, hãy kiểm tra xem mọi thứ đã sẵn sàng chưa.

1.  Mở **Command Prompt** (trên Windows) hoặc **Terminal** (trên macOS/Linux).
2.  Gõ lệnh sau và nhấn Enter:
    ```bash
    python3 --version
    ```
    *Lưu ý: Trên Windows, bạn có thể chỉ cần gõ `python --version`.*

3.  Nếu bạn thấy kết quả tương tự như `Python 3.12.4`, xin chúc mừng, bạn đã cài đặt thành công!

4.  Tiếp theo, kiểm tra `pip`:
    ```bash
    pip3 --version
    # Hoặc pip --version trên Windows
    ```

## 3. Chạy chương trình Python đầu tiên

Bây giờ là lúc để xem thành quả!

### Sử dụng Python IDLE

IDLE là một trình soạn thảo đơn giản đi kèm với Python, rất tiện để chạy thử các đoạn code ngắn.

1.  **Mở IDLE**:
    - **Windows**: Tìm "IDLE" trong Start Menu.
    - **macOS/Linux**: Gõ `idle3` trong Terminal.
2.  Cửa sổ **Python Shell** sẽ hiện ra, với dấu nhắc `>>>`.
3.  Gõ lệnh sau và nhấn Enter:
    ```python
    print("Xin chào từ IDLE!")
    ```
4.  Kết quả sẽ được in ra ngay bên dưới.

![Mô tả ảnh: Cửa sổ Python IDLE Shell](assets/images/ch02/idle_shell.png "Python IDLE Shell")

### Sử dụng file `.py`

Đây là cách chúng ta sẽ làm việc trong suốt cuốn sách.

1.  **Tạo một thư mục** cho dự án sách, ví dụ `python-book-project`.
2.  **Tạo một file** bên trong thư mục đó tên là `hello.py`.
3.  **Mở file `hello.py`** bằng một trình soạn thảo bất kỳ (như Notepad, hoặc tốt hơn là VS Code mà chúng ta sẽ cài ở bước tiếp theo).
4.  **Viết code** vào file:
    ```python
    # file: hello.py
    message = "Xin chào thế giới Python!"
    print(message)
    print("Tôi đã sẵn sàng cho hành trình phía trước.")
    ```
5.  **Lưu file** lại.
6.  **Chạy file** từ Terminal/Command Prompt:
    - Dùng lệnh `cd` để di chuyển vào thư mục dự án của bạn.
    - Gõ lệnh sau:
      ```bash
      python3 hello.py
      # Hoặc python hello.py trên Windows
      ```
7.  Bạn sẽ thấy kết quả được in ra màn hình.

## 4. Thiết lập Visual Studio Code (VS Code)

VS Code là một trình soạn thảo code miễn phí, mạnh mẽ và được yêu thích nhất hiện nay.

1.  **Tải và cài đặt VS Code**:
    - Truy cập [https://code.visualstudio.com/](https://code.visualstudio.com/).
    - Tải về phiên bản cho hệ điều hành của bạn và tiến hành cài đặt.

2.  **Cài đặt Extension cho Python**:
    - Mở VS Code.
    - Nhấn vào biểu tượng **Extensions** ở thanh công cụ bên trái (trông giống 4 ô vuông).
    - Trong ô tìm kiếm, gõ `Python`.
    - Chọn extension **Python** của Microsoft và nhấn **Install**. Extension này cung cấp các tính năng như gợi ý code (IntelliSense), kiểm tra lỗi, và hỗ trợ gỡ lỗi (debugging).

    ![Mô tả ảnh: Cài đặt extension Python trong VS Code](assets/images/ch02/vscode_python_extension.png "Extension Python của Microsoft")

3.  **Mở thư mục dự án**:
    - Trong VS Code, vào `File > Open Folder...` và chọn thư mục `python-book-project` bạn đã tạo.

4.  **Chạy code trong VS Code**:
    - Mở file `hello.py`.
    - Bạn sẽ thấy một nút **Play (▶)** ở góc trên bên phải. Nhấn vào đó.
    - Một cửa sổ Terminal sẽ tự động mở ra bên dưới và chạy code của bạn. Thật tiện lợi!

## 5. Môi trường ảo (Virtual Environment)

Đây là một khái niệm cực kỳ quan trọng trong lập trình Python chuyên nghiệp.

### Tại sao cần môi trường ảo?

Hãy tưởng tượng bạn có 2 dự án:
- **Dự án A**: Cần thư viện `requests` phiên bản 2.25.
- **Dự án B**: Cần thư viện `requests` phiên bản 2.28 mới nhất.

Nếu bạn cài đặt `requests` chung cho toàn bộ máy tính, bạn sẽ không thể đáp ứng yêu cầu của cả hai dự án cùng lúc.

**Môi trường ảo (venv)** giải quyết vấn đề này bằng cách tạo ra một "thư mục" riêng, chứa các thư viện chỉ dành cho một dự án cụ thể.

### Cách tạo và sử dụng `venv`

Hãy thực hành ngay với dự án của chúng ta.

1.  **Mở Terminal/Command Prompt** và di chuyển vào thư mục `python-book-project`.

2.  **Tạo môi trường ảo**:
    - Chạy lệnh sau. `venv` ở cuối là tên của thư mục môi trường ảo, đây là tên gọi theo quy ước.
      ```bash
      python3 -m venv venv
      # Hoặc python -m venv venv trên Windows
      ```
    - Bạn sẽ thấy một thư mục mới tên là `venv` được tạo ra.

3.  **Kích hoạt môi trường ảo**:
    - **Windows**:
      ```bash
      .\venv\Scripts\activate
      ```
    - **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```
    - Sau khi kích hoạt, bạn sẽ thấy `(venv)` xuất hiện ở đầu dòng lệnh, cho biết bạn đang ở trong môi trường ảo.

4.  **Làm việc trong môi trường ảo**:
    - Bây giờ, bất kỳ thư viện nào bạn cài bằng `pip` sẽ chỉ được cài vào thư mục `venv` này.
    - Ví dụ, hãy thử cài một thư viện: `pip install requests`.

5.  **Thoát khỏi môi trường ảo**:
    - Khi làm việc xong, gõ lệnh:
      ```bash
      deactivate
      ```

> **Quy tắc vàng**: Luôn tạo và kích hoạt môi trường ảo cho **mỗi** dự án Python mới.

## 📋 Tóm tắt chương

- Bạn đã cài đặt thành công **Python 3** và biết cách kiểm tra phiên bản.
- Bạn đã chạy được chương trình Python đầu tiên bằng cả **IDLE** và **file `.py`**.
- Bạn đã thiết lập **VS Code** với extension Python, sẵn sàng cho việc code chuyên nghiệp.
- Bạn đã học được cách tạo và quản lý **môi trường ảo (`venv`)**, một kỹ năng cực kỳ quan trọng.

## 🧠 Bài tập củng cố

Hãy chắc chắn rằng bạn đã tự tay hoàn thành các bước cài đặt và thiết lập trong chương này.

- **[Bài tập Chương 2 &raquo;](../exercises/chapter02.html)**

## ➡️ Chương tiếp theo

Bạn đã có đầy đủ công cụ. Trong [Chương 3: Cú pháp cơ bản và Biến](/chapters/chapter03.html), chúng ta sẽ bắt đầu viết những dòng code Python thực sự đầu tiên để giải quyết các bài toán.
