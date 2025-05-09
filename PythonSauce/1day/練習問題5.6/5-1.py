def weather():
    print("今日は晴れです")

# weather()

def calc_circle_area(n):
    print(n*3.14)

# calc_circle_area(5)

import datetime
def nowstr():
    now = datetime.datetime.now()
    print(now.strftime('%H時%M分%S秒'))

# nowstr()

def nowint():
    now = datetime.datetime.now()
    print(now.strftime('%H:%M:%S'))

# nowint()

def is_leapyear(n):
    if(n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
        print("閏年です")
    else:
        print("閏年ではありません")

is_leapyear(int(input()))