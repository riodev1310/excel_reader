import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from cover_letter import CoverLetterProcessor

# Main Streamlit app
st.title("Google Sheets Editor with Streamlit")

# Sidebar for Google Sheets configuration
SHEET_ID = st.sidebar.text_input("Enter sheet's ID: ")
SHEET_NAME = st.sidebar.text_input("Enter sheet's name: ")

if SHEET_ID and SHEET_NAME:
    # Cấu hình Google Sheet API
    try:
        # Load credentials từ file JSON
        creds = Credentials.from_service_account_file("google_service.json", scopes=["https://www.googleapis.com/auth/spreadsheets"])
        # Kết nối tới Google Sheets
        client = gspread.authorize(creds)
        # Mở file Google Sheet và lấy dữ liệu
        sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        # data = sheet.get_all_records()
        all_values = sheet.get_all_values()
        # Lấy ra những hàng đầu là tên cột
        headers = all_values[0]
        # Lấy dữ liệu từ hàng thứ hai trở đi
        data = all_values[1:] if len(all_values) > 1 else []
        # Lưu dưới dạng Dataframe
        df = pd.DataFrame(data, columns=headers)
        st.success("Kết nối thành công")
    except FileNotFoundError:
        st.error("Lỗi Credentials")
    except gspread.SpreadsheetNotFound:
        st.error("Không tìm thấy file")
    except gspread.exceptions.APIError as e:
        st.error("Google API error")

    # Form nhập liệu thủ công
    with st.form(key='user_form'):
        ho_ten = st.text_input("Họ và tên (Viết in hoa)")
        gioi_tinh = st.selectbox("Giới tính", ["Nam", "Nữ"])
        ngay_sinh = st.text_input("Ngày sinh (ví dụ: 07 tháng 05 năm 2025)")
        noi_sinh = st.text_input("Nơi sinh")
        nguyen_quan = st.text_input("Nguyên quán")
        ho_khau = st.text_input("Hộ khẩu")
        cho_o_hien_nay = st.text_input("Chỗ ở hiện nay")
        dien_thoai = st.text_input("Điện thoại")
        dan_toc = st.text_input("Dân tộc", value="Kinh")
        cccd_cmnd = st.text_input("CCCD/CMND")
        ngay_cap = st.text_input("Ngày cấp (Ví dụ: 07/05/2025)")
        noi_cap = st.text_input("Nơi cấp", value="Cục Cảnh sát")
        trinh_do_van_hoa = st.selectbox("Trình độ văn hóa", ["Học sinh tiểu học", "Trung học cơ sở", "Trung học phổ thông", "Đại học", "Sinh viên"])
        so_truong = st.text_input("Sở trường")

        # Nút submit cho form thủ công
        submit_button = st.form_submit_button(label='Gửi thông tin')
        if submit_button:
            user_data = {
                "Họ và tên": ho_ten, "Giới tính": gioi_tinh, "Ngày sinh": ngay_sinh,
                "Nơi sinh": noi_sinh, "Nguyên quán": nguyen_quan, "Hộ khẩu": ho_khau,
                "Chỗ ở hiện nay": cho_o_hien_nay, "Điện thoại": dien_thoai,
                "Dân tộc": dan_toc, "CCCD/CMND": cccd_cmnd, "Ngày cấp": ngay_cap,
                "Nơi cấp": noi_cap, "Trình độ văn hóa": trinh_do_van_hoa, "Sở trường": so_truong
            }
            new_row = pd.DataFrame([user_data])
            df = pd.concat([df, new_row], ignore_index=True)
            df["Điện thoại"] = df["Điện thoại"].astype("string")
            df["CCCD/CMND"] = df["CCCD/CMND"].astype("string") 
            # df["Ngày cấp"] = pd.to_datetime(df["Ngày cấp"])
            sheet.clear()
            sheet.update([df.columns.values.tolist()] + df.values.tolist())
            st.success("Thêm dữ liệu thành công")

    # Upload file .docx
    uploaded_files = st.file_uploader("Tải lên các file sơ yếu lý lịch (.docx)", type="docx", accept_multiple_files=True)
    processor = CoverLetterProcessor()

    if uploaded_files:
        if st.button("Trích xuất và Lưu từ file"):
            extracted_data = processor.process_documents(uploaded_files)
            if extracted_data:
                new_df = pd.DataFrame(extracted_data, columns=processor.headers)
                df = pd.concat([df, new_df], ignore_index=True)
                df["Điện thoại"] = df["Điện thoại"].astype("string")
                df["CCCD/CMND"] = df["CCCD/CMND"].astype("string") 
    
                sheet.clear() 
                sheet.update([df.columns.values.tolist()] + df.values.tolist())
                st.success("Dữ liệu từ file đã được trích xuất và lưu thành công!")
                uploaded_files.clear()

    # Hiển thị dữ liệu
    st.dataframe(df)