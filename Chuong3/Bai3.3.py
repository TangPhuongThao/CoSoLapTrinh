a=float(input('Tieu thu='))
if a<=101: t=a*550
elif a<=150: t=(100*550)+((a-100)*750)
elif a<=200: t=(100*550)+(50*750)+((a-150)*950)
else: t=(100*550)+(50*750)+(200*950)+((a-200)*1350)
VAT=0.1
print('Phai tra=',t+t*VAT,sep='')
