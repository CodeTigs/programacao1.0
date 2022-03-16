"""hi, mi, hf, mf = map(int, input().split())

if (hf-hi == 1) and (mi > mf):
    a = 60 - mi
    m = a+mf
    h = 0
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif (hi == hf) and (mi == mf):
    h = 24
    m = 0
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif (hi < hf) and (mi < mf):
    h = hf-hi
    m = mf-mi
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif (hi < hf) and (mi > mf):
    h = (hf - hi)-1
    a = 60 - mi
    m = a + mf
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif hi == hf and (mi < mf):
    h = 0
    m = mf - mi
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif hi < hf and (mi == mf):
    m = 0
    h = hf - hi
    print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
elif hi > hf:
    h = (24-hi)+hf
    m = mf-mi
    if mi > mf:
        h = h-1
        m = (60-mi)+mf
        print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S)")
    else:
        print("O JOGO DUROU", h, "HORA (S) E", m, "MINUTO (S) HORA(S)")
"""
x = input().split()
hi, mi, hf, mf = x

hi = int(x[0])
mi = int(x[1])
hf = int(x[2])
mf = int(x[3])

if hi < hf:
    h = hf - hi
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi > hf:
    h = (24 - hi) + hf
    if mi < mf:
        m = mf - mi
    if mi > mf:
        h = h - 1
        m = (60 - mi) + mf
    if mi == mf:
        m = 0
if hi == hf:
    if mi < mf:
        m = mf - mi
        h = 0
    if mi > mf:
        m = (60 - mi) + mf
        h = 23
    if mi == mf:
        h = 24
        m = 0

print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(h, m))

