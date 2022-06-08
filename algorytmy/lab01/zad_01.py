import math
from timeit import default_timer as timer


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


# F1    Fn = n
print('Sprawdzanie F1')
for n in range(100000, 900001, 100000):
    start = timer()
    f1(n)
    stop = timer()
    Tn = stop - start
    Fn = n
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# F2    Fn = n*n
print('Sprawdzanie F2')
for n in range(1000, 9001, 1000):
    start = timer()
    f2(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# F3    Fn = n*n
print('Sprawdzanie F3')
for n in range(1000, 9001, 1000):
    start = timer()
    f3(n)
    stop = timer()
    Tn = stop - start
    Fn = n * n
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# F4    Fn = n * math.log(n, 2)
print('Sprawdzanie F4')
for n in range(100000, 900001, 100000):
    start = timer()
    f4(n)
    stop = timer()
    Tn = stop - start
    Fn = n * math.log(n, 2)
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# F4    Fn = math.log(n, 2)
print('Sprawdzanie F5')
for n in range(100000, 900001, 100000):
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn = math.log(n, 2)
    print(n, '\t', format(Tn, '.8f'), '\t', int(Fn / Tn))

# inne funkcje czasu:

# Fn=math.log(n,2)
# Fn=n
# Fn=100*n
# Fn=n*math.log(n,2)
# Fn=n*n

"""
Sprawdzanie F1
100000 	 0.00601090 	 16636443
200000 	 0.01201050 	 16652096
300000 	 0.02409880 	 12448752
400000 	 0.02459290 	 16264856
500000 	 0.02886120 	 17324296
600000 	 0.03448390 	 17399424
700000 	 0.04045800 	 17301893
800000 	 0.04582580 	 17457414
900000 	 0.05234270 	 17194374

Sprawdzanie F2
1000 	 0.05681800 	 17600056
2000 	 0.22960030 	 17421580
3000 	 0.51409040 	 17506648
4000 	 0.91067950 	 17569298
5000 	 1.42249910 	 17574703
6000 	 2.05448310 	 17522655
7000 	 2.82807210 	 17326290
8000 	 3.89449690 	 16433444
9000 	 5.03029980 	 16102419

Sprawdzanie F3
1000 	 0.02856200 	 35011553
2000 	 0.20957200 	 19086519
3000 	 0.33422670 	 26927830
4000 	 0.48213890 	 33185457
5000 	 0.82145040 	 30433973
6000 	 1.06721290 	 33732725
7000 	 1.42748590 	 34326083
8000 	 1.85666740 	 34470363
9000 	 2.34372210 	 34560411

Sprawdzanie F4
100000 	 0.14656910 	 11332293
200000 	 0.30994610 	 11363034
300000 	 0.48306600 	 11299451
400000 	 0.64158230 	 11602340
500000 	 0.82741070 	 11440248
600000 	 1.01942470 	 11297314
700000 	 1.22088310 	 11132840
800000 	 1.37120930 	 11440786
900000 	 1.55110700 	 11476712

Sprawdzanie F5 - po chwili sie stabilizuje i daje wyniki w okolicach 95...
100000 	 0.00000390 	 4258881
200000 	 0.00000230 	 7656404
300000 	 0.00000210 	 8664150
400000 	 0.00000200 	 9304884
500000 	 0.00000190 	 9964060
600000 	 0.00000200 	 9597228
700000 	 0.00000200 	 9708423
800000 	 0.00000200 	 9804745
900000 	 0.00000200 	 9889851
"""
