# Электронные часы-2
n = int(input())
ss = n % 60
mm = (n//60) % 60
h = (n//60)//60 % 24
print('{}:{:0>2}:{:0>2}'.format(h, mm, ss))
