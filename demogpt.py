from gpt_selenium import GPT_Selenium

#ta cần phải nhập email và password vào nếu mà bạn không có trên mạng có cả chục tài khoản free lên đó chúng ta lấy hehe
chat_bot = GPT_Selenium(
    email='ntbinh.c6ntmkhai@gmail.com',
    password='*********'
)
"""tiếp theo phải chạy connect để kết nối(bởi vì có trường hợp ngăn chặn đưa thông báo bạn phải đăng nhập sau)
nên hàm connect của tôi đã giúp tránh trườn hợp đó
nếu kết nối được nó sẽ đưa ra thông báo kết nối được
"""
print(chat_bot.connect())
"""
sau khi xong hết mn hãy chạy hàm run nó nhận câu hỏi đầu vào và trả ra kết quả trả lời của chatgpt
"""
while True:
    question=input('Human: ')
    if question=='':
        print('bye human :(( ')
        break
    else:
        answer=chat_bot.run(question=question)
        print('Chatgpt: '+ answer)
