# 👤 Face Dataset Creator & Trainer with Database Integration

## 📖 Giới thiệu
Dự án này được xây dựng để **tạo dataset khuôn mặt** từ webcam và **huấn luyện mô hình nhận diện** bằng thuật toán **LBPH (Local Binary Patterns Histogram)**.  
Ngoài ra, hệ thống tích hợp **MySQL (SQL Workbench)** để lưu trữ thông tin người dùng (ID, Tên, Tuổi), cho phép quản lý và cập nhật dữ liệu dễ dàng.  

## 🚀 Tính năng chính
- **Thu thập dữ liệu khuôn mặt** trực tiếp từ webcam.  
- **Lưu thông tin người dùng** (ID, Name, Age) vào MySQL database.  
- **Phát hiện khuôn mặt** bằng Haar Cascade (`haarcascade_frontalface_default.xml`), khi nhận diện được khuôn mặt sẽ có name + age của từng người.
- **Sinh dataset tự động**: lưu ảnh với định dạng `User.ID.SampleNum.jpg`.  
- **Huấn luyện mô hình LBPH** với dữ liệu thu thập được.  
- **Xuất file model (`trainer.yml`)** để dùng lại trong các ứng dụng nhận diện.  
- **Tích hợp database**: cập nhật và truy vấn thông tin từ MySQL Workbench.
  
## 📌 Ghi chú

Dự án được thực hiện trong quá trình học tập, vì vậy khó tránh khỏi những sai sót và nhầm lẫn.  
Mình rất mong nhận được sự góp ý, phản hồi từ các bạn để hoàn thiện hơn.  

📧 Liên hệ: ...........

