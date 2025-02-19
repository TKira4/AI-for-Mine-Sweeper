# AI-for-Mine-Sweeper
### Giới Thiệu
Dự án Minesweeper AI này nhằm xây dựng một hệ thống tự động giải bài toán Minesweeper bằng cách kết hợp giải thuật DFS (Depth First Search) để cascade mở các ô an toàn cùng với các logic đơn giản để cắm cờ (Flagging) vào các ô nghi ngờ chứa mìn. Hệ thống được xây dựng bằng Python và sử dụng thư viện Pygame để visualize cho người xem thấy được từng nước đi trực quan của giải thuật.
##
### Ý Tưởng Chính
- **Mở rộng vùng an toàn (Safe - có giá trị 0) bằng DFS**: Khi một ô có giá trị 0 (không có mìn xung quanh) được mở, chúng ta sử dụng thuật toán DFS để cascade mở tất cả các ô liền kề an toàn. Sử dụng iterative DFS để tránh lỗi đệ quy khi vùng an toàn lớn.
- **Logic**: Sử dụng các quy tắc đơn giản dựa trên số hiển thị trên các ô đã mở để:
    - **Cắm cờ (Flagging)**: Nếu số ô ẩn liền kề cộng với số ô đã cắm cờ bằng với số hiển thị, các ô ẩn còn lại được xác định là chứa mìn và được cắm cờ.
    - **Mở ô an toàn (Revealing a safe cell)**: Nếu số ô đã cắm cờ bằng số hiển thị trên ô, các ô ẩn liền kề khác được xác định là an toàn và sẽ được mở.
- **Nước đoán (Guess move)**: Trong trường hợp không có bước suy luận an toàn nào, AI sẽ thực hiện "nước đoán" bằng cách chọn ngẫu nhiên một ô chưa được mở (not revealed) và chưa được cắm cờ (not flagging). Điều này là tối quan trọng vì Minesweeper có tính chất NP-complete nên không phải lúc nào cũng đủ thông tin để suy luận an toàn.
##
### Kiến Trúc Dự Án
- *main.py*: đây là file chính để khởi tạo Pygame, tạo bảng để visualize và gọi các hành động của AI. Quản lí vòng lặp chính, xử lí sự kiên và cập nhật giao diện.
- *board.py*:
    - Khởi tạo bảng, đặt mìn và tính số trên mỗi ô.
    - Phương thức `draw_board()` để vẽ giao diện bảng bằng Pygame.
    - Phương thức `reveal()` sử dụng *iterative DFS* để mở các ô an toàn mà không gặp lỗi đệ quy.
- *ai_solver.py*:
    - Các phương thức suy luận như `flag_sure_mines()` và `reveal_safe_cell()` để cắm cờ và mở các ô dựa trên các quy tắc logic.
    - Phương thức `solve()` kết hợp quy tắc logic và "nước đoán" khi không còn bước suy luận an toàn.
##
### Những Trường Hợp DFS Giải Quyết Tốt
- **Bảng có mật độ mìn ít**: Khi có nhiều ô an toàn liền kề (ô có giá trị 0), DFS sẽ cascade mở ra phần lớn bảng.
- **Khu vực an toàn liên thông**: Nếu một vùng rộng của bảng không có mìn xung quanh, DFS sẽ tự động mở tất cả các ô trong vùng đó.
##
### Hạn Chế và Hướng Phát Triển
- **Hạn chế của DFS và quy tắc logic đơn giản**: Ở những bảng có mật độ mìn cao hoặc cấu trúc phức tạp, thông tin từ các ô mở không đủ để suy luận an toàn hoàn toàn, dẫn đến việc AI buộc phải "đoán". Trong trường hợp này, có thể xảy ra mở ô chứa mìn hoặc không giải được hết bảng.
- **Cải tiến**:
    - Nâng cao logic suy luận: Sử dụng các chiến lược logic phức tạp hơn hoặc phương pháp tính xác suất để đưa ra quyết định "đoán" chính xác hơn.
    - Tối ưu hóa quá trình "cascade": Đảm bảo các ô đã cắm cờ không được mở lại.
##
### Thư Viện Cần Thiết Và Lệnh Để Chạy Chương Trình
**1. Yêu cầu hệ thống**
- Python 3.9 hoặc cao hơn (Tôi đang sử dụng Python 3.11.9).
- Thư viện pygame (2.6.0).
- Visual Studio Code (hoặc các IDE tương tự).

**2. Clone dự án từ Github**
```basg
git clone https://github.com/TKira4/AI-for-Mine-Sweeper.git
cd AI-for-Mine-Sweeper
```

**3. Tạo và kích hoạt môi trường ảo**
*Đối với Windows:*
```basg
python -m venv venv
.\venv\Scripts\activate
```
*Đối với macOS/Linux:*
```basg
python3 -m venv venv
source venv/bin/activate
```
**4. Cài đặt thư viện cần thiết**
```basg
pip install -r requirement.txt     
```

# Hướng dẫn chạy
```basg
.\venv\Scripts\activate
python -B .\src\main.py