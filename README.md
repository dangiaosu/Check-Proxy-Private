# Proxy Private Checker - Đan Giáo Sư

Proxy Checker là công cụ mạnh mẽ được viết bằng Python, giúp kiểm tra trạng thái proxy, lấy thông tin IP public, và xuất kết quả ra file Excel. Công cụ này được tối ưu hóa để hoạt động nhanh chóng và dễ dàng cho cả người mới bắt đầu.

---

## **Tính năng nổi bật**
- Kiểm tra trạng thái của proxy (`active`, `die`, `duplicate`).
- Lấy thông tin chi tiết về IP public thông qua API của [ipinfo.io](https://ipinfo.io/).
- Xuất kết quả ra file Excel (`proxy_check_results.xlsx`).
- Giao diện thân thiện, dễ sử dụng.
- Được tối ưu cho người dùng Windows.

---

## **Cách sử dụng**

### **1. Yêu cầu hệ thống**
- **Python**: Phiên bản 3.9 trở lên.
- **Kết nối mạng**: Đảm bảo máy tính của bạn có kết nối Internet.

---

### **2. Đăng ký tài khoản và lấy token tại ipinfo.io**
1. Truy cập vào [ipinfo.io](https://ipinfo.io/).
2. Nhấn vào nút **Sign Up** và điền đầy đủ thông tin.
3. Sau khi đăng ký thành công, truy cập vào [Dashboard](https://ipinfo.io/account/token).
4. Sao chép **Access Token** (ví dụ: `99215av6f6142`) và thay thế token này vào file `check.py` trong biến `IPINFO_TOKEN`:
   ```python
   IPINFO_TOKEN = "YOUR_ACCESS_TOKEN"

### **3. Cài đặt**


1. Clone repository hoặc tải mã nguồn:
```bash
git clone https://github.com/yourusername/proxy-checker.git
cd proxy-checker
```

2. Đảm bảo bạn đã cài Python và pip:

3. Sử dụng tệp start.bat:
- Chạy start.bat để tự động kiểm tra môi trường và cài đặt đầy đủ các thư viện.

4. Chuẩn bị danh sách proxy
Tạo file proxy.txt trong thư mục chính.

Định dạng file proxy.txt:
```ruby
IP:PORT:USERNAME:PASSWORD
```

Ví dụ:
```ruby
192.168.1.1:8080:user1:pass1
192.168.1.2:9090:user2:pass2
```

5. Chạy chương trình
Sau khi đã chuẩn bị xong, chạy file start.bat để bắt đầu kiểm tra proxy.

### **Kết quả**
- Kết quả kiểm tra sẽ được lưu vào file proxy_check_results.xlsx.
- File kết quả bao gồm:
  - Proxy: Proxy đã kiểm tra.
  - IP Public: Địa chỉ IP công khai.
  - Trạng thái: (active, die, duplicate).
  - Thông tin chi tiết: Dữ liệu từ API ipinfo.io (nếu proxy hoạt động).

### **Cấu trúc thư mục**

```css
proxy-checker/
│
├── check.py                   # Mã nguồn chính
├── proxy.txt                  # Danh sách proxy (do người dùng thêm)
├── proxy_check_results.xlsx   # File kết quả kiểm tra
├── start.bat                  # Tệp chạy chính, kiểm tra và khởi động chương trình
└── README.md                  # Tài liệu hướng dẫn
```

### **Hỗ trợ**
Nếu bạn gặp vấn đề hoặc có câu hỏi, vui lòng liên hệ qua:

- Telegram: [@dangiaosu](https://t.me/dangiaosu/)
- Facebook: [Đan Tạ ( Giáo Sư )](https://fb.com/prof.danta/)
- Zalo: 0828092390

### **Credits**
Credits
- Đan Giáo Sư: Idea và gõ prompt.
- ChatGPT: Code toàn bộ và tối ưu.
