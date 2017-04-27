
C=[53.6233,53.59,53.6266,53.7133,53.63]

toplam=0
tp=0
OF=53.7133


for i in range(0,5):#14 gunluk periyot aldik

    toplam=toplam+C[i]

OFHO=toplam/float(5)

for i in range(0,5):

    snc=abs(C[i]-OFHO)
    tp=tp+snc

SPO=tp/float(5)

CCI=(OF-OFHO)/float((SPO*0.015))

print CCI
