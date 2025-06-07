# Xử lý đầu vào của người dùng
user_input = input("Câu hỏi của bạn: ").lower().strip()

# Chào người dùng
if user_input == "hi":
    print(
        "Xin chào quý khách! Tôi có thể giúp gì cho quý khách?\n"
        "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
    )

elif user_input == "hello":
    print(
        "Xin chào, bạn cần tôi giúp gì không?\n"
        "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
    )

# Tư vấn mua hàng
elif user_input == "tư vấn mua hàng":
    print(["điện thoại", "laptop", "máy tính bảng"])

elif user_input == "điện thoại":
    print("Quý khách muốn mua điện thoại nào ạ?")

elif user_input == "laptop":
    print("Quý khách muốn mua laptop nào ạ?")

elif user_input == "máy tính bảng":
    print("Quý khách muốn mua tablet nào ạ?")

# Tra cứu bảo hành
elif user_input == "tra cứu bảo hành":
    print(["tra cứu bằng số điện thoại", "tra cứu bằng IMEI"])

elif user_input == "tra cứu bằng số điện thoại":
    print("Quý khách vui lòng nhập số điện thoại để tra cứu bảo hành")

elif user_input == "tra cứu bằng imei":
    print("Quý khách vui lòng nhập IMEI để tra cứu bảo hành")

# Hỗ trợ kỹ thuật
elif user_input == "hỗ trợ kỹ thuật":
    print(["lỗi phần cứng", "lỗi phần mềm"])

elif user_input == "lỗi phần cứng":
    print("Quý khách vui lòng mô tả lỗi phần cứng để được hỗ trợ")

elif user_input == "lỗi phần mềm":
    print("Quý khách vui lòng mô tả lỗi phần mềm để được hỗ trợ")

# Không hiểu yêu cầu
else:
    print("Xin lỗi! Tôi không hiểu yêu cầu của bạn. Bạn có thể nói rõ hơn không?")