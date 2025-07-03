---
layout: chapter
title: "Bài tập: Giải phương trình bậc hai"
---

# Bài tập: Giải phương trình bậc hai

### Đề bài

Viết một chương trình Python để giải và biện luận nghiệm của phương trình bậc hai có dạng tổng quát:

$$ax^2 + bx + c = 0$$

**Yêu cầu:**

1.  Chương trình cho phép người dùng nhập vào 3 hệ số `a`, `b`, và `c` từ bàn phím.
2.  Chương trình phải xử lý trường hợp `a = 0` (phương trình trở thành bậc nhất).
3.  Dựa vào giá trị của biệt thức (delta), hãy biện luận các trường hợp nghiệm của phương trình:
    -   **Delta (\(\Delta\))** được tính theo công thức: \(\Delta = b^2 - 4ac\)
    -   Nếu \(\Delta > 0\): Phương trình có 2 nghiệm thực phân biệt.
    -   Nếu \(\Delta = 0\): Phương trình có nghiệm kép.
    -   Nếu \(\Delta < 0\): Phương trình có 2 nghiệm phức.

### Lời giải tham khảo

Dưới đây là một đoạn code Python hoàn chỉnh để giải quyết bài toán trên.

```python
import cmath

def solve_quadratic_equation(a, b, c):
    """
    Hàm giải phương trình bậc hai ax^2 + bx + c = 0 và biện luận nghiệm.
    """
    # Trường hợp a = 0, phương trình trở thành bậc nhất: bx + c = 0
    if a == 0:
        if b == 0:
            if c == 0:
                print("Kết luận: Phương trình có vô số nghiệm.")
            else:
                print("Kết luận: Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình bậc nhất có một nghiệm duy nhất: x = {x}")
        return

    # Tính delta
    delta = (b**2) - (4*a*c)

    print(f"Biệt thức delta = {delta}")

    # Biện luận nghiệm dựa trên delta
    if delta > 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print("Kết luận: Phương trình có 2 nghiệm thực phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Kết luận: Phương trình có nghiệm kép: x1 = x2 = {x}")
    else:
        # Sử dụng thư viện cmath để tính căn bậc hai của số âm (nghiệm phức)
        x1 = (-b - cmath.sqrt(delta)) / (2*a)
        x2 = (-b + cmath.sqrt(delta)) / (2*a)
        print("Kết luận: Phương trình có 2 nghiệm phức:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

if __name__ == '__main__':
    try:
        print("--- CHƯƠNG TRÌNH GIẢI PHƯƠNG TRÌNH BẬC 2 ---")
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
        
        print(f"\nGiải phương trình: {a}x^2 + {b}x + {c} = 0")
        solve_quadratic_equation(a, b, c)

    except ValueError:
        print("Lỗi: Vui lòng chỉ nhập số!")

```

**Giải thích code:**

- **`import cmath`**: Chúng ta import thư viện `cmath` (complex math) để có thể tính toán căn bậc hai của số âm, vốn là trường hợp cho ra nghiệm phức.
- **Hàm `solve_quadratic_equation`**: Đóng gói logic chính vào một hàm để dễ dàng tái sử dụng và quản lý.
- **Xử lý `a = 0`**: Đây là bước quan trọng để đảm bảo chương trình chạy đúng trong mọi trường hợp.
- **`if __name__ == '__main__'`**: Khối lệnh này đảm bảo rằng phần code yêu cầu người dùng nhập chỉ chạy khi file được thực thi trực tiếp, không phải khi được import như một module.
- **`try...except`**: Bẫy lỗi `ValueError` phòng trường hợp người dùng nhập vào không phải là số.
