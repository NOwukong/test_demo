import time

# print(time.asctime())
# print(time.time())
# # 1606035773.6378877
# # 1606035842.7798426
# print(time.localtime())
print(time.strftime('%Y{y}%m{m}%d{d} %H:%M:%S %A', time.localtime()).format(y='年', m='月', d='日'))

now_time = time.time()
tow_day_before = now_time - 60 * 60 * 24 * 3
time_tuple = time.localtime(tow_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S %A", time_tuple))
