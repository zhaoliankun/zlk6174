#--coding:utf-8--
# 6174猜想，6174猜想 ，1955年，卡普耶卡(D.R.Kaprekar)研究了对四位数的一种变换：
# 任给出四位数k0,用它的四个数字由大到小重新排列成一个四位数m,再减去它的反序数rev(m),
# 得出数k1=m-rev(m),然后，继续对k1重复上述变换，得数k2.如此进行下去，卡普耶卡发现，
# 无论k0是多大的四位数， 只要四个数字不全相同，最多进行7次上述变换，就会出现四位数6174.
number = input()
bingo = True
while bingo:
    nn = []
    for k in range(0,4):
        a = number % 10
        nn.append(a)
        number = number / 10
    order = sorted(nn)
    large = order[0]*1+order[1]*10+order[2]*100+order[3]*1000
    small = order[3]*1+order[2]*10+order[1]*100+order[0]*1000
    dif = large - small
    strsmall = str(order[0])+str(order[1])+str(order[2])+str(order[3])
    strlarge = str(order[3])+str(order[2])+str(order[1])+str(order[0])
    print strlarge,'-',strsmall,'=',dif
    number = dif
    if dif == 6174:
        bingo = False
    if dif == 0:
        print 'wrong input!'
        bingo = False
