
import random
import matplotlib.pyplot as plt

cts   = 36.5  #basal temp
al    = 1.0
gamma = 18.88 * 18.88 
sigma = 18.88 * 18.88 # fit 
b0    = -7887.1
b1    = 384.4286
b2    = -4.5714
v     = 0.0

for y in range(1, 120):
   heartrate = random.randrange(130, 145, 1)
   x=cts
   x_pred = al * x
   v_pred = (al  * al ) * (v+gamma)
   z      = heartrate
   c_vc   = 2.0 *  b2 * x_pred + b1
   k      = (v_pred * c_vc)/((c_vc*c_vc) * v_pred+sigma)
   x      = x_pred+k * (z-(b2 * (x_pred*x_pred)+b1 * x_pred+b0))
   v      = (1-k * c_vc) * v_pred
   CTS    = x
   plt.plot(x)

   
plt.show()   



