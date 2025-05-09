def is_leapyear(n):
    if(n % 400 == 0 or (n % 4 == 0 and n % 100 != 0)):
        print(f'西暦{n}年は、閏年です')
    else:
        print(f'西暦{n}年は、閏年ではありません')

is_leapyear(int(input("西暦を入力してください。")))