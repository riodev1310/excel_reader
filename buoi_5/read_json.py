import json

# Đường dẫn đến file JSON
file_path = "alphabet.json"

try:
    # Mở và đọc file JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        alphabet_positions = json.load(file)
    
    # In ra dictionary để kiểm tra
    print("Dữ liệu từ file JSON:")
    print(alphabet_positions)
    
    # Ví dụ: truy cập vị trí của một chữ cái
    letter = 'A'
    if letter in alphabet_positions:
        print(f"Vị trí của chữ cái {letter}: {alphabet_positions[letter]}")
    else:
        print(f"Chữ cái {letter} không có trong dictionary.")

except FileNotFoundError:
    print(f"Không tìm thấy file: {file_path}")
except json.JSONDecodeError:
    print("Lỗi: File JSON không hợp lệ.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")