import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from PIL import Image
import glob

country='China'

df=pd.read_csv("covid_19_confirmed.csv")
df=df.drop(["Province/State","Lat","Long"],1)
df=df.loc[df['Country/Region']==country] # Taking the cases for a particular country
df_sum=df.sum(axis=0,skipna=True) # taking sum of each column
df_sum['Country/Region']=country


df_rec=pd.read_csv("covid_19_recovered.csv")
df_rec=df_rec.drop(["Province/State","Lat","Long"],1)
df_rec=df_rec.loc[df_rec['Country/Region']==country]
df_sum_rec=df_rec.sum(axis=0,skipna=True)
df_sum_rec['Country/Region']=country


df_death=pd.read_csv("covid_19_deaths.csv")
df_death=df_death.drop(["Province/State","Lat","Long"],1)
df_death=df_death.loc[df_death['Country/Region']==country]
df_sum_death=df_death.sum(axis=0,skipna=True)
df_sum_death['Country/Region']=country


n=10000
X=np.random.rand(n);
Y=np.random.rand(n);
area=np.pi/2

X.sort()
#Y.sort()
fig=plt.figure();

i=0;mid=5000;
infectedx=[];infectedy=[];
recx=[];recy=[];
deathx=[];deathy=[];
#prevf=0;prevg=0;prevh=0;

while i<len(df_sum):
    if df_sum[i]!=country: # first data is the name of country
        
        f=df_sum[i]//20
        infected=random.sample(range(max(0,mid-f),min(mid+f,n)),f)
        # prevf=f
        
        g=df_sum_rec[i]//20
        recovered=random.sample(range(max(0,mid-g),min(mid+g,n)),g)
        # prevg=g
        
        h=df_sum_death[i]//20
        death=random.sample(range(max(0,mid-h),min(mid+h,n)),h)
        # prevh=h
        
        for inf in infected:
            infectedx.append(X[inf])
            infectedy.append(Y[inf])
        
        for rec in recovered:
            recx.append(X[rec])
            recy.append(Y[rec])
            
        for dt in death:
            deathx.append(X[dt])
            deathy.append(Y[dt])
        
        plt.scatter(X,Y,color='blue',s=area)
        plt.scatter(infectedx,infectedy,color='red',s=area)
        plt.scatter(recx,recy,color='green',s=area)
        plt.scatter(deathx,deathy,color='black',s=area)
        
        
        if i<10:
            ans='covid_00'+str(i)+'.png'
        elif i<100:
            ans='covid_0'+str(i)+'.png'
        else:
            ans='covid_'+str(i)+'.png'
            
        title_s='Day '+str(i)
        noc='No. of cases (In red) '+str(df_sum[i])
        nor='No. of Recovery (In green) '+str(df_sum_rec[i])
        nod='No. of Deaths (In black) '+str(df_sum_death[i])
        plt.title(title_s)
        fig.text(0.5,0.04,noc,ha='center')
        fig.text(0.5,0.02,nor,ha='center')
        fig.text(0.5,0,nod,ha='center')
        # plt.xlabel(noc+'\n'+nor+'\n'+nod)
        plt.savefig(ans)
        
    if i>10:
        break;
        
    i+=1

# Creating a GIF from all the png files
frames = []
imgs = glob.glob("*.png")
for i in imgs:
    new_frame = Image.open(i)
    frames.append(new_frame)

# Save into a GIF file that loops forever
frames[0].save('covid19_china.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)

'''def animate(i):
    e=df_sum[i]
    if e!='China':
        infected=random.sample(range(0,100000),e)
        xnew=[];ynew=[];
        for inf in infected:
            xnew.append(X[inf])
            ynew.append(Y[inf])
        plt.scatter(X,Y,color='b',s=area)
        plt.scatter(xnew,ynew,color='r',s=area)
    return plt

anim=animation.FuncAnimation(fig,animate,frames=100,interval=20,blit=True)
plt.show()'''