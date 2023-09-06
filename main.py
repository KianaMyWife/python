import pygetwindow as gw
import keyboard

# 指定要隐藏的窗口标题
window_title_to_hide = "Clash for Windows"

# 获取所有打开的窗口
all_windows = gw.getAllTitles()

# 查找要隐藏的窗口并显示状态
for window_title in all_windows:
    if window_title == window_title_to_hide:
        window = gw.getWindowsWithTitle(window_title)[0]
        print(f"窗口 '{window_title_to_hide}' 当前可见")

# 初始化隐藏状态
hidden = False

# 按下F12键时的回调函数
def toggle_visibility(e):
    global hidden
    if not hidden:
        window.hide()
        print(f"窗口 '{window_title_to_hide}' 已隐藏")
    else:
        window.show()
        print(f"窗口 '{window_title_to_hide}' 已显示")
    hidden = not hidden

# 监听F12键盘事件
keyboard.on_press_key('F12', toggle_visibility)

# 启动监听键盘事件的循环
keyboard.wait()
