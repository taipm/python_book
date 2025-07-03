import subprocess
import sys

def run_gemini_with_tools(prompt: str) -> str:
    """
    Gửi một câu lệnh đến Gemini CLI, cho phép nó sử dụng các công cụ
    và tự động chấp nhận các hành động.
    """
    if not prompt:
        return "Lỗi: Câu lệnh không được để trống."

    try:
        command = [
            "gemini",
            "--prompt", prompt,
            "--sandbox=true",
            "--all_files",
            "--yolo"
        ]
        
        # Thêm cờ --debug để xem log chi tiết
        # command.append("--debug")

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            timeout=180
        )
        
        # ✅ SỬA LỖI QUAN TRỌNG:
        # Trả về cả stdout và stderr để không bỏ sót thông tin gỡ lỗi.
        stdout_output = f"--- STDOUT ---\n{result.stdout}" if result.stdout else "--- STDOUT ---\n(Trống)"
        stderr_output = f"--- STDERR ---\n{result.stderr}" if result.stderr else "--- STDERR ---\n(Trống)"
        
        return f"{stdout_output}\n\n{stderr_output}"

    except FileNotFoundError:
        return "Lỗi: Không tìm thấy 'gemini' CLI."
    except subprocess.CalledProcessError as e:
        # Khi có lỗi, cũng in ra cả stdout và stderr
        return f"Lỗi khi thực thi lệnh Gemini CLI (Exit Code {e.returncode}):\n--- STDOUT ---\n{e.stdout}\n--- STDERR ---\n{e.stderr}"
    except Exception as e:
        return f"Đã xảy ra một lỗi không mong muốn: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_prompt = " ".join(sys.argv[1:])
        print(f"🚀 Đang gửi yêu cầu '{user_prompt}' tới Gemini với chế độ tự động xác nhận...")
        response = run_gemini_with_tools(user_prompt)
        print("\n--- Phản hồi từ Gemini ---")
        print(response)
        print("\n✅ Hoàn thành.")
        
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