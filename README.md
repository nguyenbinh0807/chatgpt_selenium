<div align="center">
  <h1>Tự động hóa ChatGPT (Selenium)</h1>
  <div style="display: inline-block">
    <a href="https://mail.google.com/mail/u/?authuser=ntbinh.c6ntmkhai@gmail.com">
      <img alt="Abhishek Naidu | Twitter" width="20px" src="https://edent.github.io/SuperTinyIcons/images/svg/gmail.svg" />
      <code>ntbinh.c6ntmkhai@gmail.com</code>
    </a>
    <span> ┃ </span>
<a href="https://www.facebook.com/binh.nguyenthe.5815255/">
      <img alt="Your Facebook" width="20px" src="https://edent.github.io/SuperTinyIcons/images/svg/facebook.svg" />
      <code>@Nguyễn Thế Bình</code>
    </a>
  </div>
  
  <br />
  <strong>Để thảo luận, truy vấn và làm việc tự do. Hãy liên lạc với tôi. .👆👆👆</strong>
</div>


 
# Giới thiệu

Đây là tập lệnh Python sử dụng Selenium để tự động hóa quá trình trò chuyện với ChatGPT ( https://chatgpt.openai.com/ ). Nó gửi một câu hỏi tới ChatGPT và đưa ra câu trả lời.

# Lợi ích

- Thay vì mình phải nạp mua để có một tài khoản api, để sử dụng mô hình của openai. thì mọi người hãy sử dụng code này để lấy câu hỏi của chatgpt để áp dụng cho những ứng dụng của bạn khỏi phải tốn thêm phí.

# Lưu ý

- code này mình chỉ viết áp dụng trên trình duyệt chorme thôi.

# Cách sử dụng
1. Mọi người cứ việc clone code về
``` 
git clone https://github.com/nguyenbinh0807/chatgpt_selenium
```
2. Cài các thư viện để setup
```
pip install -r requirements.txt
```
3. đây là file demogpt.py:
```
from gpt_selenium import GPT_Selenium

#ta cần phải nhập email và password vào nếu mà bạn không có trên mạng có cả chục tài khoản free lên đó chúng ta lấy hehe
chat_bot = GPT_Selenium(
    email='ntbinh.c6ntmkhai@gmail.com',
    password='*********'
)
"""-Tiếp theo phải chạy connect để kết nối(bởi vì có trường hợp ngăn chặn đưa thông báo bạn phải đăng nhập sau)

-Nên hàm connect của tôi đã giúp tránh trườn hợp đó

-Nên trong lúc kết nối nó sẽ chậm bởi nhưng sau khi kết nối được nó sẽ gửi thông báo là kết nối được(từ đó chatgpt sẽ trả lời cực nhanh)
"""
print(chat_bot.connect())
"""
sau khi xong hết mn hãy chạy hàm run nó nhận câu hỏi đầu vào và trả ra kết quả trả lời của chatgpt
"""
while True:
    question=input('Human: ')
    if question=='':
        print('bye human')
        break
    else:
        answer=chat_bot.run(question=question)
        print(answer)
```
4. Kết quả của file trên máy tính:

<img src="png\Screenshot 2023-04-26 135448.png" />

5. Kết quả trên web chatgpt:

 <img src="png\webchatgpt1.png" />

 <img src="png\webchatgpt2.png" />


# Đóng góp
- Hiện tại mình còn đang bận đi học nên chỉ viết thành code và để lên mọi người tham khảo.

- Nếu mọi người có câu hỏi gì cứ liên hệ tôi hoặc hãy tạo một vấn đề.

- Cảm ơn mọi người rất nhiều.

