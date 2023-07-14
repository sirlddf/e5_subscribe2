import time

def countdown(mins):
    # 将分钟数转换为秒数
    seconds = mins * 60
    # 倒计时循环
    while seconds > 0:
        # 显示剩余时间
        print(f"{seconds // 60}:{seconds % 60:02d}")
        # 等待1秒
        time.sleep(1)
        # 减少剩余时间
        seconds -= 1

# 提示用户输入要计时的分钟数
mins = int(input("请输入要计时的分钟数："))
# 开始倒计时
countdown(mins)
