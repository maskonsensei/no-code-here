import turtle
import time
import pygame
from pygame import mixer
import threading
import math

# 初始化音频
pygame.init()
mixer.init()

# 加载音效（带错误处理）
try:
    heartbeat_sound = mixer.Sound("heartbeat.mp3")
    stop_sound = mixer.Sound("beep.mp3")
    mixer.music.load("lovemeordie.mp3")  # 背景音乐
except Exception as e:
    print(f"音频加载警告: {e}")
    heartbeat_sound = None
    stop_sound = None


def play_heartbeat():
    if heartbeat_sound:
        try:
            heartbeat_sound.play(loops=-1)  # 循环播放
        except:
            pass


def stop_all_sounds():
    mixer.stop()
    mixer.music.stop()


# 屏幕设置
screen = turtle.Screen()
screen.bgcolor('black')
screen.title('爱心表白')
screen.tracer(0)  # 关闭自动刷新

# 尝试全屏（可能在某些系统上不工作）
try:
    canvas = screen.getcanvas()
    canvas.master.attributes("-fullscreen", True)
except:
    pass

# 爱心绘制设置
heart = turtle.Turtle()
heart.speed(0)
heart.hideturtle()

# 爱心像素图
heart_pixel = [
    [0, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0]
]

pixel_size = 20  # 像素大小
spacing = 2  # 间距

# 计算爱心尺寸和中心位置
width = len(heart_pixel[0]) * (pixel_size + spacing)
height = len(heart_pixel) * (pixel_size + spacing)
heart_center_x = 0
heart_center_y = -height // 4  # 调整中心位置


def draw_heart(brightness=1.0):
    try:
        heart.clear()
        r = max(0, min(1.0, brightness))
        heart.color((r, 0, 0))  # 红色爱心

        for row in range(len(heart_pixel)):
            for col in range(len(heart_pixel[row])):
                if heart_pixel[row][col] == 1:
                    x = -width // 2 + col * (pixel_size + spacing)
                    y = height // 2 - row * (pixel_size + spacing)

                    heart.penup()
                    heart.goto(x, y)
                    heart.pendown()

                    heart.begin_fill()
                    for _ in range(4):
                        heart.forward(pixel_size)
                        heart.right(90)
                    heart.end_fill()
        screen.update()
    except:
        pass


def draw_arrow():
    arrow = turtle.Turtle()
    arrow.speed(0)
    arrow.hideturtle()

    # 箭杆
    arrow.penup()
    arrow.goto(-400, 0)
    arrow.pendown()
    arrow.pensize(3)
    arrow.color("white")
    arrow.forward(800)

    # 箭头
    arrow.penup()
    arrow.goto(0, 0)
    arrow.pendown()
    arrow.begin_fill()
    arrow.color("white")
    arrow.setheading(60)
    arrow.forward(20)
    arrow.right(120)
    arrow.forward(20)
    arrow.right(120)
    arrow.forward(20)
    arrow.end_fill()

    # 箭尾
    arrow.penup()
    arrow.goto(-400, 0)
    arrow.pendown()
    arrow.setheading(150)
    arrow.forward(15)
    arrow.penup()
    arrow.goto(-400, 0)
    arrow.pendown()
    arrow.setheading(210)
    arrow.forward(15)

    return arrow


def shoot_arrow():
    try:
        # 创建箭的移动效果
        arrow_turtle = turtle.Turtle()
        arrow_turtle.speed(0)
        arrow_turtle.hideturtle()

        # 绘制初始位置的箭
        for pos in range(-400, int(heart_center_x) + 1, 10):
            arrow_turtle.clear()

            # 箭杆
            arrow_turtle.penup()
            arrow_turtle.goto(pos, heart_center_y)
            arrow_turtle.pendown()
            arrow_turtle.pensize(3)
            arrow_turtle.color("white")
            arrow_turtle.setheading(0)
            arrow_turtle.forward(80)

            # 箭头
            arrow_turtle.penup()
            arrow_turtle.goto(pos + 80, heart_center_y)
            arrow_turtle.pendown()
            arrow_turtle.begin_fill()
            arrow_turtle.color("white")
            arrow_turtle.setheading(60)
            arrow_turtle.forward(20)
            arrow_turtle.right(120)
            arrow_turtle.forward(20)
            arrow_turtle.right(120)
            arrow_turtle.forward(20)
            arrow_turtle.end_fill()

            # 箭尾
            arrow_turtle.penup()
            arrow_turtle.goto(pos, heart_center_y)
            arrow_turtle.pendown()
            arrow_turtle.setheading(150)
            arrow_turtle.forward(15)
            arrow_turtle.penup()
            arrow_turtle.goto(pos, heart_center_y)
            arrow_turtle.pendown()
            arrow_turtle.setheading(210)
            arrow_turtle.forward(15)

            screen.update()
            time.sleep(0.01)

        # 最终停在心脏中心的箭
        arrow_turtle.clear()
        draw_arrow_at_center()

    except:
        pass


def draw_arrow_at_center():
    arrow = turtle.Turtle()
    arrow.speed(0)
    arrow.hideturtle()

    # 箭杆
    arrow.penup()
    arrow.goto(heart_center_x - 80, heart_center_y)
    arrow.pendown()
    arrow.pensize(3)
    arrow.color("white")
    arrow.setheading(0)
    arrow.forward(160)

    # 箭头
    arrow.penup()
    arrow.goto(heart_center_x + 80, heart_center_y)
    arrow.pendown()
    arrow.begin_fill()
    arrow.color("white")
    arrow.setheading(60)
    arrow.forward(20)
    arrow.right(120)
    arrow.forward(20)
    arrow.right(120)
    arrow.forward(20)
    arrow.end_fill()

    # 箭尾
    arrow.penup()
    arrow.goto(heart_center_x - 80, heart_center_y)
    arrow.pendown()
    arrow.setheading(150)
    arrow.forward(15)
    arrow.penup()
    arrow.goto(heart_center_x - 80, heart_center_y)
    arrow.pendown()
    arrow.setheading(210)
    arrow.forward(15)

    screen.update()


def show_text(msg):
    try:
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.color('white')
        writer.penup()
        writer.goto(0, heart_center_y - 100)  # 文本位置在心脏下方

        # 逐字显示效果
        for i in range(1, len(msg) + 1):
            writer.clear()
            writer.write(msg[:i], align='center', font=('Arial', 24, 'bold'))
            screen.update()
            time.sleep(0.1)
    except:
        pass


# 全局状态变量
running = True
showing_message = False


def on_click(x, y):
    global running, showing_message

    if showing_message:
        return

    showing_message = True
    stop_all_sounds()

    try:
        # 绘制静态爱心
        draw_heart(1.0)

        # 播放停止音效
        if stop_sound:
            stop_sound.play()

        # 射箭动画
        shoot_arrow()

        # 播放背景音乐
        mixer.music.play()

        # 显示文本
        show_text("I love you ❤")

    except Exception as e:
        print(f"动画错误: {e}")
    finally:
        showing_message = False


def exit_program():
    global running
    running = False
    stop_all_sounds()
    try:
        screen.bye()
    except:
        pass


# 事件绑定
screen.listen()
screen.onkey(exit_program, 'Escape')  # ESC键退出
screen.onclick(on_click)  # 鼠标点击触发动画

# 在后台线程播放心跳声
try:
    heartbeat_thread = threading.Thread(target=play_heartbeat, daemon=True)
    heartbeat_thread.start()
except:
    pass

# 主动画循环
brightness = 1.0
pulse_direction = 0.07

try:
    while running:
        try:
            # 绘制跳动的心脏
            draw_heart(brightness)

            # 调整亮度变化方向
            brightness += pulse_direction
            if brightness >= 1.2 or brightness <= 0.5:
                pulse_direction *= -1

            screen.update()
            time.sleep(0.05)

        except Exception as e:
            print(f"动画循环错误: {e}")
            running = False

except KeyboardInterrupt:
    pass
finally:
    # 清理资源
    stop_all_sounds()
    try:
        screen.bye()
    except:
        pass