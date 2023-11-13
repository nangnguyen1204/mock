
import streamlit as st


st.title("bai tap streamlit")

"""
Bài tập 1: Tạo nút nhấn và hiển thị
        Tạo một ứng dụng Streamlit đơn giản với một nút nhấn.
        Khi người dùng nhấn nút, hiển thị một dòng chữ "Hello"
"""

if st.button("hay an vao day"):
    st.write('hello')

"""
Bài tập 2: Sự kiện và cập nhật dữ liệu
        Tạo một ứng dụng với một ô văn bản và một nút nhấn.
        Khi người dùng nhập văn bản và nhấn nút, hiển thị thông điệp dựa trên văn bản họ đã nhập.
"""

user_input = st.text_input("Nhap vao van ban:", "")

if st.button("Hien thi van ban"):
    st.write(f"Ban da nhap: {user_input}")

"""
Bài tập 3: Chia cột và hiển thị danh sách
        Tạo một ứng dụng với hai cột.
        Trong cột bên trái, hiện thị 1 đoạn văn bất kì
        Trong cột bên phải, hiện thị 1 đoạn văn bất kì
"""

# tao 2 cot
left_col, right_col = st.columns(2)

with left_col:
    st.write("Doan van ban bat ki")
    st.write("Nam o cot ben trai")

with right_col:
    st.write("Doan van ban bat ki")
    st.write("Nam o cot ben phai")

"""
Bài tập 4: Tải lên tệp và hiển thị hình ảnh
        Tạo một ứng dụng cho phép người dùng tải lên một tệp hình ảnh.
        Khi họ tải lên, hiển thị hình ảnh trong ứng dụng.
"""

from PIL import Image
import io

#su dung st.file_uploader de tai hinh anh len 
uploaded_img = st.file_uploader("Tai len hinh anh", type=["jpg","png","jpeg"])

# Kiem tra xem nguoi dung co tai hinh anh len chua 
if uploaded_img is not None:
    #Doc hinh anh tai len
    img = Image.open(uploaded_img)

    #hien thi hinh anh
    st.image(img, caption="Hinh anh vua tai", use_column_width=True)

"""
 Bài tập 5: Chọn hình ảnh từ danh sách và hiển thị
        Tạo một ứng dụng với một danh sách các hình ảnh và một nút nhấn.
        Khi người dùng nhấn nút, hiển thị hình ảnh được chọn từ danh sách lên giao diện.

"""

# tao danh sach hinh anh
img_list = {
    "Hinh1":"index.jpeg",
    "Hinh2":"output.png",
}

# Tao select box

selected_img = st.selectbox("Chon 1 hinh anh:", list(img_list.keys()))

#Hien thi hinh anh duoc chon

if st.button("Hien thi hinh anh"):
    img_path = img_list.get(selected_img)
    if img_path:
        st.image(img_path, caption=selected_img, use_column_width=True)
    else:
        st.warning("Hinh anh khong ton tai.")