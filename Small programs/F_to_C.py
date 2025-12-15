def f_to_c(f):
    return 5* (f-32) /9
f = int(input('Enter temperature in F.  :  '))
a= f_to_c(f)
print(f'Temperature is :  {round(a,2)}°C')
