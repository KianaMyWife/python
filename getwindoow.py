import pygetwindow as gw

# 获取所有打开的窗口
windows = gw.getAllTitles()

# 遍历窗口列表并打印标题
for window in windows:
    print(window)
