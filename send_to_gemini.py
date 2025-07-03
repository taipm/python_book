import subprocess
import sys

def run_gemini_with_tools(prompt: str) -> str:
    """
    Gửi một câu lệnh đến Gemini CLI, cho phép nó sử dụng các công cụ
    bằng cách sử dụng cờ --all_files.

    Args:
        prompt: Chuỗi câu lệnh yêu cầu Gemini thực hiện hành động.

    Returns:
        Kết quả đầu ra từ Gemini CLI.
    """
    if not prompt:
        return "Lỗi: Câu lệnh không được để trống."

    try:
        # ✅ SỬA LỖI QUAN TRỌNG:
        # Thay thế đối số "." bằng cờ "--all_files".
        # Đây là cách đúng để cấp quyền cho tool dựa trên menu help của CLI.
        command = [
            "gemini",
            "--prompt", prompt,
            "--sandbox=true",
            "--all_files"  # Cấp quyền truy cập vào các tệp trong thư mục hiện tại
        ]

        # Thực thi lệnh và chờ nó hoàn thành
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=120
        )

        return result.stdout

    except FileNotFoundError:
        return "Lỗi: Không tìm thấy 'gemini' CLI."
    except subprocess.CalledProcessError as e:
        return f"Lỗi khi thực thi lệnh Gemini CLI:\n{e.stderr}"
    except Exception as e:
        return f"Đã xảy ra một lỗi không mong muốn: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
        print(f"🤖 Đang gửi yêu cầu '{user_prompt}' tới Gemini với quyền truy cập tool...")
        response = run_gemini_with_tools(user_prompt)
        print("\n--- Phản hồi từ Gemini ---")
        print(response)
        print("\n✅ Hãy kiểm tra thư mục của bạn để xem tệp đã được tạo chưa.")
    else:
        print("Vui lòng cung cấp câu lệnh làm đối số.")
        print('Ví dụ: python3 send_to_gemini.py "Viết hàm tính giai thừa vào file factorial.py"')
# import subprocess
# import sys

# def send_command_to_gemini(prompt: str) -> str:
#     """
#     Gửi một câu lệnh (prompt) đến Gemini CLI và trả về kết quả.

#     Args:
#         prompt: Chuỗi câu lệnh bạn muốn gửi đến Gemini.

#     Returns:
#         Kết quả đầu ra từ Gemini CLI.
#     """
#     if not prompt:
#         return "Lỗi: Câu lệnh không được để trống."

#     try:
#         # ✅ SỬA LỖI QUAN TRỌNG:
#         # Thêm cờ '--sandbox=false' để ngăn Gemini cố gắng sử dụng công cụ
#         # và buộc nó phải trả về văn bản thuần túy.
#         command = ["gemini", "--prompt", prompt, "--sandbox=false"]

#         # Thực thi lệnh và chờ nó hoàn thành
#         result = subprocess.run(
#             command,
#             capture_output=True,
#             text=True,
#             check=True,
#             timeout=120  # Đặt thời gian chờ để tránh treo
#         )

#         # Trả về kết quả từ stdout (kết quả thành công)
#         return result.stdout

#     except FileNotFoundError:
#         return "Lỗi: Không tìm thấy 'gemini' CLI. Hãy chắc chắn rằng nó đã được cài đặt và nằm trong PATH của hệ thống."
#     except subprocess.CalledProcessError as e:
#         # Trả về lỗi từ stderr để gỡ lỗi
#         error_message = f"Lỗi khi thực thi lệnh Gemini CLI:\n{e.stderr}"
#         return error_message
#     except subprocess.TimeoutExpired:
#         return "Lỗi: Yêu cầu tới Gemini đã hết thời gian chờ."
#     except Exception as e:
#         return f"Đã xảy ra một lỗi không mong muốn: {e}"

# if __name__ == "__main__":
#     if len(sys.argv) > 1:
#         user_prompt = " ".join(sys.argv[1:])
#         print("🤖 Đang gửi yêu cầu tới Gemini...")
#         response = send_command_to_gemini(user_prompt)
#         print("\n--- Phản hồi từ Gemini ---")
#         print(response)
#     else:
#         print("Vui lòng cung cấp câu lệnh làm đối số.")
#         print('Ví dụ: python3 send_to_gemini.py "Kể một câu chuyện cười"')
# # import subprocess
# # import sys

# # def send_command_to_gemini(prompt: str) -> str:
# #     """
# #     Gửi một câu lệnh (prompt) đến Gemini CLI và trả về kết quả.

# #     Args:
# #         prompt: Chuỗi câu lệnh bạn muốn gửi đến Gemini.

# #     Returns:
# #         Kết quả đầu ra từ Gemini CLI.
# #     """
# #     if not prompt:
# #         return "Lỗi: Câu lệnh không được để trống."

# #     try:
# #         # SỬA LỖI TẠI ĐÂY:
# #         # Thay thế 'generate' bằng cờ '--prompt'
# #         # Cấu trúc đúng là: gemini --prompt "câu lệnh của bạn"
# #         command = ["gemini", "--prompt", prompt]

# #         # Thực thi lệnh và chờ nó hoàn thành
# #         result = subprocess.run(
# #             command,
# #             capture_output=True,
# #             text=True,
# #             check=True,
# #             # Thêm timeout để tránh treo nếu lệnh chạy quá lâu
# #             timeout=120 
# #         )

# #         # Trả về kết quả từ stdout
# #         return result.stdout

# #     except FileNotFoundError:
# #         return "Lỗi: Không tìm thấy 'gemini' CLI. Hãy chắc chắn rằng nó đã được cài đặt và nằm trong PATH của hệ thống."
# #     except subprocess.CalledProcessError as e:
# #         # Nếu có lỗi từ CLI, nó sẽ được in ra stderr
# #         error_message = f"Lỗi khi thực thi lệnh Gemini CLI:\n{e.stderr}"
# #         return error_message
# #     except subprocess.TimeoutExpired:
# #         return "Lỗi: Yêu cầu tới Gemini đã hết thời gian chờ."
# #     except Exception as e:
# #         return f"Đã xảy ra một lỗi không mong muốn: {e}"

# # if __name__ == "__main__":
# #     # Lấy câu lệnh từ đối số dòng lệnh khi chạy file python
# #     if len(sys.argv) > 1:
# #         user_prompt = " ".join(sys.argv[1:])
# #         print("🤖 Đang gửi yêu cầu tới Gemini...")
# #         response = send_command_to_gemini(user_prompt)
# #         print("\n--- Phản hồi từ Gemini ---")
# #         print(response)
# #     else:
# #         print("Vui lòng cung cấp câu lệnh làm đối số.")
# #         print('Ví dụ: python3 send_to_gemini.py "Kể một câu chuyện cười"')