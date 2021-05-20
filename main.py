import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
import xlrd

t = np.linspace(0, 12, 185)
a1 = 10.22
b1 = 0.3158
c1 = 0.81
a2 = 12.77
b2 = 0.3943
c2 = 3.468
a3 = 3.39
b3 = 0.5463
c3 = 5.665
a4 = 0.2409
b4 = 1.769
c4 = -0.00536

# Goodness of fit:
#   SSE: 0.09598
#   R-square: 0.9194


k1 = 0.8
d = 20
k2 = 0.01
L = 2
v=[]
counts = 0
lists = []
v = []
counts = 0
lists = []
nums = 20
red = 40
for t in t:
    p = (a1 * math.sin(b1 * t + c1) + a2 * math.sin(b2 * t + c2) + a3 * math.sin(b3 * t + c3) + a4 * math.sin(b4 * t + c4))
    v.append((-k1+(k1**2*p**2-4*L*p+4*d)**(1/2))/(2*k2*p))
    lists.append(d / v[counts])
    counts += 1
std_lists = []
for i in lists:
    std_lists.append((i-min(lists))/(max(lists)-min(lists)))
copy_lists = [(x+1)*30 for x in std_lists]
std_lists = [(x+1)*30 for x in std_lists]
v_lists = [d/(x/60) for x in std_lists]
gap = d/nums
wait_time = [0 for x in std_lists]  # 等红绿灯的时间
used_time = [0 for x in std_lists]  # 路上花费的时间
for i in range(len(v_lists)):
    v_light = v_lists[i]
    for j in range(nums):
        used_time[i] += 1/v_light*3600
        if used_time[i] % (red*2) < red:
            wait_time[i] += red-used_time[i] % (red*2)
        else:
            pass
    std_lists[i] += wait_time[i]/60


def plt1():
    my_x_ticks = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    t = np.linspace(0, 12, 185)
    x = range(1, 13, 1)
    lists_arr = np.array(std_lists)
    plt.xticks(x, my_x_ticks)
    plt.plot(t, lists_arr)
    #plt.plot(t, copy_lists) # 没有红绿灯

readbook = xlrd.open_workbook(r'机场人流.xlsx')
sheet = readbook.sheets()[0]
nrows = sheet.nrows#行
ncols = sheet.ncols#列
nums = sheet.col_values(0)
t = np.linspace(0, 24, len(nums))
v = 24


def avgnums():
    avg_nums = [x for x in range(len(nums))]
    for i in range(len(nums)-v):
        avg_nums[i] = sum(nums[j]for j in range(i,i+v))/v
    return avg_nums


def plt2():
    plt.plot(t,nums)
    plt.plot(t,avgnums())
    plt.show()


def plt3():
    plt.plot(np.linspace(0, 12, len(airport_time_cut)), Total_time)
    plt.legend(['time in road', "time in airport", "Total_time"])


airport_time = [0 for i in range(len(avgnums()))]
for i in range(len(airport_time)):
    airport_time[i] = avgnums()[i]/500
airport_time_cut = airport_time[int(405*(8/24)):int(405*(19/24))]
print(len(airport_time_cut))
my_x_ticks = [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
x = range(1, 13, 1)
plt.xticks(x, my_x_ticks)
airport_time_cut = [x*60 for x in airport_time_cut]


Total_time = []
airport_time_cut_more = airport_time_cut+airport_time[int(405*(19/24)):]
for i in range(len(std_lists)):
    Total_time.append(std_lists[i]+airport_time_cut_more[i+int(185*(used_time[i]/3600)/24)])

plt1()
#plt.plot(np.linspace(0, 12, len(airport_time_cut)), airport_time_cut)
#plt3()
plt.show()
