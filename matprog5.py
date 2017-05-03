# -*- coding: utf-8 -*-
dosya = open("ornek.mps")
v=1
x=dosya.readlines()
t=len(x)

asl="y"
nzl="y"
asl=raw_input("1.asama icin iterasyon.iterasyon yok (y)")
nzl=raw_input("2.asama icin iterasyon.iterasyon yok (y)")
k=[]
a=[]
a1=[]
deneme=[]
rows=[]
n=[]
han=[]
bounds=0
for i in range(0,t):
    k=x[i].split()
    #print k
    if k[0]=="*":
        pass
    if k[0]=="OBJSENSE":
        OBJ=x[i+1].split()
        print OBJ
        if OBJ[0]== "MIN" :
            print "minimum"

    if k[0]=="ROWS":
        row=i
    if k[0]=="COLUMNS":
        colum=i
    if k[0]=="RHS":
        rhs=i
    if k[0]=="BOUNDS":
        bounds=i
    if k[0]=="ENDATA":
        end=i
#fonksiyon adlarini ekle buyukmu kucukmu onlar
for s in range(row+1,colum):
    k=x[s].split()
    a.append(k[1])
    a1.append(k[0])
###################################################
##print a ,"kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
##print a1

############----------buraya eklenicek yeni tek kistaslar

#degiskenleri ekleme yeri ###############
for i in range(colum+1,rhs):
    k=x[i].split()
    han.append(k[0])

kisitsayisi=colum-row -1
        
print "row =" + str(row) 
print "colum =" +str(colum)
print "rhs = " +str(rhs)
print "bounds ="+str(bounds)
print "end ="+str(end)
       
for i in range(0,len(a)):
    rows.append([])
    rows[i].append(a[i])
    rows[i].append(a1[i])

print rows


for i in range(0,len(a)):
    n.append([])

q=len(han)
cd=[]
deleted=[]
for i in range(0,q):
    
    cd.append(han[i])
              
for i in range(0,q-1): 
    
    if han[i]==han[i+1]: 
        s=han[i]        
        deleted.append(s)
        
for i in range(0,len(deleted)):
    cd.remove(deleted[i])

cdd=[] #ln 283
for i in range(0,len(cd)):
    cdd.append(cd[i])

##print n
##print cd,"--------------------------------------------"
####################################################
##-----hangi degisken hangi fonksiyonda rows satirlerina bakmak
ee=[]
for i in range(colum+1,rhs):
    
    l=x[i].split()
    ee.append(l)

##print ee
#############n dizinini 0 larla doldurmak icin
for i in range(0,len(n)):
    for d in range(0,len(cd)):
        
        n[i].append("0")
######################################################

#########333 matrise degiskenlerin katsayilarini atamak
for i in range(0,len(ee)):
    if len(ee[i])>3:
        sepet=ee[i][1]
        sepetindex=a.index(sepet)
        
        yuva=ee[i][0]
        yuvaindex=cd.index(yuva)
        
        yumurta1=ee[i][2]

        sepet2=ee[i][3]
        sepet2index=a.index(sepet2)

        yumurta2=ee[i][4]

        n[sepetindex][yuvaindex]=yumurta1
        n[sepet2index][yuvaindex]=yumurta2
    else:
        sepet=ee[i][1]
        sepetindex=a.index(sepet)

        yuva=ee[i][0]
        yuvaindex=cd.index(yuva)
        
        yumurta1=ee[i][2]

        n[sepetindex][yuvaindex]=yumurta1



#free degeskene bak

bond=[]
bnd=[]
sst=1
wwq=["UP","BND1","X1","0"]
if bounds==0: 
    for i in range(0,len(cd)):
       wwq[2]=cd[i]
       bnd.append(wwq)
    bounds=end-1
    sst=0
else:
    
    for i in range(bounds+1,end):
        l=x[i].split()
        bond.append(l)

##    print bond

    for i in range(0,len(bond)):

        if bond[i][0]=="FR":
            dg=bond[i][2]
        
            index=cd.index(dg)
            cd.insert(index,"-"+dg)
            for t in range(0,len(n)):
                deg2="-"+n[t][index]
                n[t].insert(index,deg2)
            


#

#ilk olarak denklemi esitleme kat sayilari
#degsayi=len(cd)
degsayiS=0
degsayiS=degsayiS+1
##print a,"999999999999999999999999999999999999999999999999999999999999"
for i in range(0,len(a)):
    
    deger = rows[i][1]
    if deger=="N" or "E":
        pass
    if deger=="L":
        deger2=rows[i][0]
        deger3=a.index(deger2)
        for t in range(0,len(n)):
            if t==deger3:
                n[deger3].append("1.0")
            else:
                n[t].append("0")
        cd.append("S"+str(degsayiS))
        degsayiS=degsayiS+1

    if deger=="G":
        deger2=rows[i][0]
        deger3=a.index(deger2)
        for t in range(0,len(n)):
            if t==deger3:
                n[deger3].append("-1.0")
            else:
                n[t].append("0")       
    
        cd.append("S"+str(degsayiS))
        degsayiS=degsayiS+1

############ R lerin katsayilarini ekleme
yenminbel=[]
for i in range(0,len(rows)):
    if rows[i][1]=="E" or rows[i][1]=="G" :
        yenminbel.append([])

tt=0
for i in range(0,len(rows)):
    if rows[i][1]=="E" or rows[i][1]=="G" :
        yenminbel[tt].append(rows[i][0])
        tt=tt+1
    

        
degsayiR=0
degsayiR=degsayiR+1
yenimindenklemi=[]
for i in range(0,len(a)):
    
    deger = rows[i][1]
    if deger=="N" or "L":
        pass
    if deger=="E" or deger=="G":
        deger2=rows[i][0]
        deger3=a.index(deger2)
        for t in range(0,len(n)):
            if t==deger3:
                n[deger3].append("1.0")
            else:
                n[t].append("0")
        cd.append("R"+str(degsayiR))
        yenimindenklemi.append("R"+str(degsayiR))
        degsayiR=degsayiR+1
        
for i in range(0,len(yenminbel)):
    yenminbel[i].append(yenimindenklemi[i])

################3 RRRR degiskenlerini ekledikten sonra en son sag tarafi ekle
rh=[]
for i in range(rhs+1,bounds):
    l=x[i].split()
    rh.append(l)

print rh

for i in range(0,len(n)):
    n[i].append("0")

inds=len(n[0])-1

for i in range(0,len(rh)):
    if len(rh[i])>3:
        sepet=rh[i][1]
        sepetindex=a.index(sepet)
        
        n[sepetindex][inds]=rh[i][2]

        sepet2=rh[i][3]
        sepetindex=a.index(sepet2)

        n[sepetindex][inds]=rh[i][4]
        
    else:
        sepet=rh[i][1]
        sepetindex=a.index(sepet)

        n[sepetindex][inds]=rh[i][2]
        
print "--------------------------------------------------------"
if sst != 0:
    
    bnd=[]
    for i in range(bounds+1,end):
        l=x[i].split()
        bnd.append(l)
    fd=[]
    for i in range(0,len(cdd)): # tum degiskenler icin deger alir
        fd.append(["0","0","0"])
    for i in range(0,len(bnd)):
        sagsol=bnd[i][0]
        ortadeg=bnd[i][2]
        index=cdd.index(ortadeg)
        fd[index][1]=ortadeg
        if sagsol=="UP":
            fd[index][2]=bnd[i][3]
        if sagsol=="LO":
            fd[index][0]=bnd[i][3]
        if sagsol=="FR":
            fd[index][0]="NN"
else:
    fd=[]
    for i in range(0,len(cdd)): # tum degiskenler icin deger alir
        fd.append(["0","0","0"])
    for i in range(0,len(bnd)):
        sagsol=bnd[i][0]
        ortadeg=bnd[i][2]
        index=cdd.index(ortadeg)
        fd[index][1]=ortadeg
        if sagsol=="UP":
            fd[index][2]=bnd[i][3]
        if sagsol=="LO":
            fd[index][0]=bnd[i][3]
        if sagsol=="FR":
            fd[index][0]="NN"
    
for i in range(0,len(cdd)): ##fd dizisinin orta degerlerin 0 la degil kisitlari ekleme
    fd[i][1]=cdd[i]
    

#w1 gerektirmeyen denklemlerde sag sol esitlemek s leri eklemek ve denklemi matrise atmak
cd.append("cz")
say=1
sepet=[]
sdeg="s1"
degdg=[]
degtek=["N","N","N","N"] # degdg nin icine atilicak seyleri tut
Wdeg=1
for i in range(0,len(fd)):
    if fd[i][0]=="0":
        a.append("Nn"+str(say))
        say=say+1
        cd.insert(len(cd)-1,"S"+str(degsayiS))
        sdeg="S"+str(degsayiS)
        degsayiS=degsayiS+1
        a1.append("E")
        
        
        for t in range(0,len(n)): #0 doldurmak icin
            n[t].insert(len(n[t])-1,0)
            
        for c in range(0,len(n[0])): 
            sepet.append("0")
            
        for k in range(0,len(sepet)):
            sepet[k]="0"

        index=cdd.index(fd[i][1])
        sepet[index]="1.0"
        index=cd.index(sdeg)
        sepet[index]="1.0"
        sepet[len(sepet)-1]=fd[i][2]#sonada eklese olur

        n.append(sepet)
        sepet=[]

    if fd[i][0]=="NN":
        pass

    
    if fd[i][0]!="NN" and(float(fd[i][0])>0 or float(fd[i][0])<0):

        W="W"+str(Wdeg)
        Wdeg=Wdeg+1

        degtek[0]=fd[i][1]
        degtek[1]=W
        degtek[2]=fd[i][0]
        degtek[3]=float(fd[i][2])-float(fd[i][0])

        degdg.append(degtek)    

 #
 #
 #
 #
 #
#degisen degerin katsayi carpimi ve sag taraf toplama cikarma
for i in range(0,len(degdg)):
    index=cdd.index(degdg[i][0])
    for s in range(0,len(n)):
        n[s][len(n[0])-1]=float(n[s][len(n[0])-1])-float(n[s][index])*float(degdg[i][2])
        
       # print n[s][len(n)-1]

#x1 leri w1 lere donusturme
for i in range(0,len(degdg)):
    index=cdd.index(degdg[i][0])
    cd[index]=degdg[i][1]


k=[]
for i in range(0,len(n[0])):
    k.append("0")
               
for i in range(0,len(degdg)):
    index=cd.index(degdg[i][1])
    k[index]="1.0"
    cd.insert(len(cd)-1,"S" + str(degsayiS))
    degsayiS=degsayiS+1
    
    for s in range(0,len(n)):
        n[s].insert(len(n[0])-2,"0")
        
    k.insert(len(k)-1,"1.0")
    k[len(k)-1]=degdg[i][3]
    n.append(k)
    a.append("Nn" + str(say))
    say=say+1
    a1.append("E")


##print "--------",cd

##for i in range(0,len(n)):
##    print a[i] ,"--" ,n[i]
print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6"
print "--------",cd
for i in range(0,len(n)):
    print a[i] ,"--" ,n[i]
print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&6"
####Birinci asama cozume basla --------**********----------**********-----

b=[] # cozum matrisinin ilk sutunu ayni zamanda denklem adlari 
sepetb=[]
for i in range(0,len(cd)):
    if len(cd[i].split("R"))==2:
        b.append(cd[i])
       
        
for i in range(0,len(cd)):
    if len(cd[i].split("S"))==2:
        index=cd.index(cd[i])
        for k in range(0,len(n)):
            if n[k][index]=="1.0" or n[k][index]==1:
                b.append(cd[i])
                
                
                
b.insert(0,"C")
nb=[]
for i in range(0,len(b)):
    nb.append([])

toplam=[]
for i in range(0,len(cd)):
    toplam.append("0")
    
for i in range(0,len(cd)):
    if len(cd[i].split("R"))==2:
        index=cd.index(cd[i]) # i zaten index oluyor neyse...
        for k in range(0,len(n)):
            if n[k][index]=="1.0" or n[k][index]==1:
                for s in range(0,len(n[k])):
                    toplam[s]=float(toplam[s])+float(n[k][s])
for i in range(0,len(cd)):
    if len(cd[i].split("R"))==2:
        index=cd.index(cd[i])
        toplam[index]=0.0
        
for i in range(0,len(toplam)):
    nb[0].append(toplam[i])



for i in range(1,len(b)):
    index=cd.index(b[i])
    for k in range(0,len(n)):
        if n[k][index]=="1.0" or n[k][index]==1:
            for s in range(0,len(n[0])):
                nb[i].append(n[k][s])


## BU noktaya kadar R lerin toplamini aliyor ve cozum satirini olusturuyor.

print "*----------------------*-------------------*---------------------"        

##print "------",cd
##for i in range(0,len(nb)):
##    print b[i] ,"--" ,nb[i]

print "0000000000000000000000000000000000000000000000000000000000000000000"
qw=1
#nb,cd,b
enk=10000000000
enb=-1000000000
iterasyon=0
oran=[]
anahtarSatir=[]
tt=0
sss=1
al=0
print cd
##for i in range(0,len(nb)):
##    
##    print b[i],"-----", nb[i]
if sss==1:
    while qw==1:
        
##        for i in range(0,len(nb[0])-1):
##            if float(nb[0][i])<=0:
##                tt=tt+1
##        if tt==len(nb[0])-1:
##            print "cozum satirinda deger kalmadi"
##            qw=2


#---------------------SATIR ISLEMLERI-----------------------------------------

        
        
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])>enb:
                enb=nb[0][i]
                indexSutun=i
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])<=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            print "------",cd
            for i in range(0,len(nb)):
                print b[i] ,"--" ,nb[i]
            qw=2
        
        
        for i in range(1,len(nb)):
            if float(nb[i][indexSutun])==0:
                oran.append("T?")
            else:
                
                oran.append(float(nb[i][len(cd)-1])/float(nb[i][indexSutun]))
        
        ##################################-----cozumu kontrol et
        for i in range(0,len(oran)):
            if oran[i]<=0:
                oran[i]="T?" # negatif ve sifirlardan kurtulmak icin
               
        kk=0 #su noktaya dikkat et
        for i in range(0,len(oran)):
            if oran[i]=="T?":
                kk=kk+1

        if kk==len(oran):
            print "sonsuz cozum var"
            print "------",cd
            for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
            qw=2
            
        ##################################################################
            
        
        for i in range(0,len(oran)):
            if oran[i]<enk and oran[i] != "T?":
                enk=oran[i]
               
        
        indexSatir=oran.index(enk)+1
        enk=100000000
        #hep sonuyor ama enk ayni
        #indexte ayni
        
        for i in range(0,len(nb[indexSatir])):
            
            anahtarSatir.append(float(nb[indexSatir][i])/float(nb[indexSatir][indexSutun]))
            
        for i in range(0,len(nb[indexSatir])):
            nb[indexSatir][i]=anahtarSatir[i]
        b[indexSatir]=cd[indexSutun]
        #anahtar satir ile diger satirlarin islemi    
        #for i in range(0,len(n)):
            
           
        yenisatir=[]
        for i in range(0,len(nb)):
            if i==indexSatir:
                pass
            else:
                #yenisatir=nb[i]-nb[indexSatir][indexSutun]*anahtarSatir[]
                for k in range(0,len(nb[0])):
                    yenisatir.append(float(nb[i][k])-((float(nb[i][indexSutun])*float(anahtarSatir[k]))))
                    #print yenisatir
                nb[i]=yenisatir
                yenisatir=[]
        nb[indexSatir]=anahtarSatir
        #qw=2        
        anahtarSatir=[]
        indexSatir=[]
        oran=[]
        enb=-1000000000
        tt=0
##        print "------",cd
##        for i in range(0,len(nb)):
##            print b[i] ,"--" ,nb[i]

        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])<=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            print "------",cd
            for i in range(0,len(nb)):
                print b[i] ,"--" ,nb[i]
            qw=2
        if type(asl)!=str:
            if al==float(asl):
                print "------",cd
                for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
                qw==2
            al=al+1
        
###################################################################

#------------------------IKINCI ASAMA---------------------
## eksi negatif olanlarin hepsini cikar
##nb,cd,b,n,a?
sil=[]
asd=0
cde=[]
for i in range(0,len(cd)):
    cde.append(cd[i])



for i in range(0,len(nb[0])):
    if i==len(nb[0])-1:
        pass
    if nb[0][i] != 0:
        sil.append(i-asd)
        asd=asd+1

for i in range(0,len(sil)):
    if cde[i]!="cz":
        cde.pop(sil[i])
        for ll in range(0,len(nb)):
            nb[ll].pop(sil[i])
nb[0][len(nb[0])-1]=0.0
print "---------ikinci asama cozume gecis noktasi------"
print "------",cde
for i in range(0,len(nb)):
    print b[i] ,"--" ,nb[i]

#Ikinci Asama Cozum
nbb=[]
nn=[]
for i in range(0,len(nb)):
    nbb.append([])

for i in range(0,len(nb)):
    for k in range(0,len(nb[0])):
        nbb[i].append(nb[i][k])

for i in range(0,len(n[0])):
    nn.append(n[0][i])
for i in range(0,len(sil)):
    nn.pop(sil[i])


for i in range(1,len(b)):
    deg=b[i]
    index=cde.index(deg)
    nn[index]=0              #sonda toplanacak


for i in range(1,len(b)):

    index=cde.index(b[i])
    nbb[i][index]=0

for i in range(1,len(b)):
    
    index=cd.index(b[i])
    carpsayi=float(n[0][index])
    carpsayi=float(carpsayi)*(-1)
    for k in range(0,len(nbb[0])):
        nn[k]=float(nn[k])+(carpsayi*nbb[i][k])
    

for i in range(0,len(nb[0])):
    nb[0][i]=nn[i]
    
##print "------",cde
##for i in range(0,len(nb)):
##    print b[i] ,"--" ,nb[i]


qw=1
#nb,cd,b
cd=cde
enk=10000000000
enb=-1000000000
iterasyon=0
oran=[]
anahtarSatir=[]
tt=0
sss=1    
al=0
if OBJ[0]=="MIN":
    
    while qw==1:
        
##        for i in range(0,len(nb[0])-1):
##            if float(nb[0][i])<=0:
##                tt=tt+1
##        if tt==len(nb[0])-1:
##            print "cozum satirinda deger kalmadi"
##            qw=2


#---------------------SATIR ISLEMLERINDE HATA OLUYOR -----------------------------------------


        
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])>enb:
                enb=nb[0][i]
                indexSutun=i
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])<=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            print "------",cd
            for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
            qw=2 
        
        for i in range(1,len(nb)):
            if float(nb[i][indexSutun])==0:
                oran.append("T?")
            else:
                
                oran.append(float(nb[i][len(cd)-1])/float(nb[i][indexSutun]))
        
        ##################################-----cozumu kontrol et
        for i in range(0,len(oran)):
            if oran[i]<=0:
                oran[i]="T?" # negatif ve sifirlardan kurtulmak icin
               
        kk=0 #su noktaya dikkat et
        for i in range(0,len(oran)):
            if oran[i]=="T?":
                kk=kk+1

        if kk==len(oran):
            print "sonsuz cozum var"
            print "------",cd
            for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
            qw=2
            
        ##################################################################
            
        
        for i in range(0,len(oran)):
            if oran[i]<enk and oran[i] != "T?":
                enk=oran[i]
               
        
        indexSatir=oran.index(enk)+1
        enk=100000000
        #hep sonuyor ama enk ayni
        #indexte ayni
        
        for i in range(0,len(nb[indexSatir])):
            
            anahtarSatir.append(float(nb[indexSatir][i])/float(nb[indexSatir][indexSutun]))
            
        for i in range(0,len(nb[indexSatir])):
            nb[indexSatir][i]=anahtarSatir[i]
        b[indexSatir]=cd[indexSutun]
        #anahtar satir ile diger satirlarin islemi    
        #for i in range(0,len(n)):
            
           
        yenisatir=[]
        for i in range(0,len(nb)):
            if i==indexSatir:
                pass
            else:
                #yenisatir=nb[i]-nb[indexSatir][indexSutun]*anahtarSatir[]
                for k in range(0,len(nb[0])):
                    yenisatir.append(float(nb[i][k])-((float(nb[i][indexSutun])*float(anahtarSatir[k]))))
                    #print yenisatir
                nb[i]=yenisatir
                yenisatir=[]
        nb[indexSatir]=anahtarSatir
        #qw=2        
        anahtarSatir=[]
        indexSatir=[]
        oran=[]
        enb=-1000000000
        tt=0
##        print "------",cd
##        for i in range(0,len(nb)):
##            print b[i] ,"--" ,nb[i]

        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])<=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            print "------",cd
            for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
            qw=2
        if type(nzl)!=str:
            if al==float(nzl):
                print "------",cde
                for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
                qw==2
            al=al+1

qw=1
#nb,cd,b
enk=10000000000
enb=-1000000000
iterasyon=0
oran=[]
anahtarSatir=[]
tt=0
sss=1
bbb=100000000
if OBJ[0]=="MAX":
    
    while qw==1:
        
##        for i in range(0,len(nb[0])-1):
##            if float(nb[0][i])<=0:
##                tt=tt+1
##        if tt==len(nb[0])-1:
##            print "cozum satirinda deger kalmadi"
##            qw=2


#---------------------SATIR ISLEMLERI-----------------------------------------


        
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])<enk:
                enk=nb[0][i]
                indexSutun=i
        
        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])>=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            qw=2 
        
        for i in range(1,len(nb)):
            if float(nb[i][indexSutun])==0:
                oran.append("T?")
            else:
                
                oran.append(float(nb[i][len(cd)-1])/float(nb[i][indexSutun]))
        
        ##################################-----cozumu kontrol et
        for i in range(0,len(oran)):
            if oran[i]<=0:
                oran[i]="T?" # negatif ve sifirlardan kurtulmak icin
               
        kk=0 #su noktaya dikkat et
        for i in range(0,len(oran)):
            if oran[i]=="T?":
                kk=kk+1

        if kk==len(oran):
            print "sonsuz cozum var"
            qw=2
            
        ##################################################################
            
        
        for i in range(0,len(oran)):
            if oran[i]<bbb and oran[i] != "T?":
                bbb=oran[i]
               
        
        indexSatir=oran.index(bbb)+1
        
        bbb=100000000
        #hep sonuyor ama enk ayni
        #indexte ayni
        
        for i in range(0,len(nb[indexSatir])):
            
            anahtarSatir.append(float(nb[indexSatir][i])/float(nb[indexSatir][indexSutun]))
            
        for i in range(0,len(nb[indexSatir])):
            nb[indexSatir][i]=anahtarSatir[i]
        b[indexSatir]=cd[indexSutun]
        #anahtar satir ile diger satirlarin islemi    
        #for i in range(0,len(n)):
            
           
        yenisatir=[]
        for i in range(0,len(nb)):
            if i==indexSatir:
                pass
            else:
                #yenisatir=nb[i]-nb[indexSatir][indexSutun]*anahtarSatir[]
                for k in range(0,len(nb[0])):
                    yenisatir.append(float(nb[i][k])-((float(nb[i][indexSutun])*float(anahtarSatir[k]))))
                    #print yenisatir
                nb[i]=yenisatir
                yenisatir=[]
        nb[indexSatir]=anahtarSatir
        #qw=2        
        anahtarSatir=[]
        indexSatir=[]
        oran=[]
        enk=1000000000
        tt=0
        print "------",cd
        for i in range(0,len(nb)):
            print b[i] ,"--" ,nb[i]

        for i in range(0,len(nb[0])-1):
            if float(nb[0][i])>=0:
                tt=tt+1
        if tt==len(nb[0])-1:
            print "cozum satirinda deger kalmadi"
            qw=2
        if type(nzl)!=str:
            if al==float(nzl):
                print "------",cde
                for i in range(0,len(nb)):
                    print b[i] ,"--" ,nb[i]
                qw==2
            al=al+1


print "cozum = " , nb[0][len(nb[0])-1]

for i in range(1,len(b)):
    if len(b[i].split("W"))>=2:
        for k in range(0,len(degdg)):
            for s in range(0,len(degdeg[0])):
                if degdg[k][1]==b[i]:
                    
                    print degdeg[k][0] , " = ", float(nb[i][len(nb[0])-1]) + float(degdg[k][2])
    else:
        
        print b[i], " = ", nb[i][len(nb[0])-1]

    
           
        



            














