import numpy as np
import random
from random import shuffle
#mob marks obtained,ma part a mark, mb part b mark, mc part c mark
#pending work questions options
def marks (mob,ma,mb,mc,qna,qnb,qnc,qnat,qnbt,qnct,qla,qlb,qlc):
    #ma = 0;#np.zeros(qna, dtype = int)
    #mb = 0;#np.zeros(qnb, dtype = int)
    #mc = 0;#np.zeros(qnc, dtype = int)
    ans=0,#ma+mb+mc;
    ans1=0;
    global maa,mba,mca,prt_a,prt_b,prt_c
    prt_a=0;
    prt_b=0;
    prt_c=0;
    while ans != mob:
        prt_a = random.choice(np.arange(0,(ma*qnat)+0.25,0.5));
        prt_b = random.choice(np.arange(0,(mb*qnbt)+0.25,0.5));
        prt_c = random.choice(np.arange(0,(mc*qnct)+0.25,0.5));
        ans=prt_a+prt_b+prt_c;
    print(prt_a,prt_b,prt_c);
    maa = np.zeros(qna);
    mba=np.zeros(qnb);
    mca=np.zeros(qnc);
    while ans1 != mob:
        maas=0;
        mbas=0;
        mcas =0;
        maa = np.zeros(qna);
        mba=np.zeros(qnb);
        mca=np.zeros(qnc);
        while maas != prt_a:
            if qla != 0:
                qna=qna-qla;
                maa=np.random.choice(np.arange(0, ma+0.25, 0.5), size=qna);
                r1 = np.zeros(qla);
                maa=np.concatenate([r1,maa]);
                maa=random.shuffle(maa)
            else:
                maa = np.random.choice(np.arange(0, ma+0.25, 0.5), size=qna);
                maas=sum(maa);
        while mbas != prt_b:
            if qlb != 0:
                qnb=qnb-qlb;
                mba=np.random.choice(np.arange(0, mb+0.25, 0.5), size=qnb);
                r2 = np.zeros(qlb);
                mba=np.concatenate([r2,mba]);
                mba=random.shuffle(mba)
            else:
                mba = np.random.choice(np.arange(0, mb+0.25, 0.5), size=qnb);
                mbas = sum(mba)
        while mcas != prt_c:
            if qlc != 0:
                qnc=qnc-qlc;
                print(abs(qnc))
                mca=np.random.choice(np.arange(0, mc+0.25, 0.5), size=abs(qnc));
                print(mca)
                r3 = np.zeros(qlc);
                mca=np.concatenate((r3,mca));
                mca=np.asarray(mca)
                print(mca)
                mca=mca.tolist()
                mca=random.sample(mca,len(mca))
                
                print(mca)
                mca=np.asarray(mca)
                mcas =sum(mca)
            else:
                mca = np.random.choice(np.arange(0, mc+0.25, 0.5), size=qnc);
                mcas =sum(mca)
        
        mas=sum(maa)
        mbs=sum(mba)
        mcs=sum(mca)
        ans1 = mas+mbs+mcs;
    return maa,mba,mca
    

#mo_array=np.arange(0.0, 50.25, 0.5);

#for mo in range(0,50):  
#no of questions
parta_q = 5;
partb_q = 3;
partc_q = 4;

#marks 
parta_m = 1;
partb_m = 5;
partc_m = 10;

#no of questions to be attended
parta_qa = 5;
partb_qa = 3;
partc_qa = 3;

#no of questions to be leave
parta_ql = parta_q-parta_qa;
partb_ql = partb_q-partb_qa;
partc_ql = partc_q-partc_qa;
print(parta_m,partb_m,partc_m,parta_q,partb_q,partc_q,parta_qa,partb_qa,partc_qa,parta_ql,partb_ql,partc_ql)

#Marks Division
#Mark obtained
abc= np.arange(0, 50+0.25, 0.5)
for i in abc:
    mo = i;
    a,b,c=marks(mo,parta_m,partb_m,partc_m,parta_q,partb_q,partc_q,parta_qa,partb_qa,partc_qa,parta_ql,partb_ql,partc_ql);
    mo_by_calculate = sum(a)+sum(b)+sum(c);
    print('mo_by_calculate',mo_by_calculate)
    print("a is ",a,"bis " ,b,"c is " ,c)

