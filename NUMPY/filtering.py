import numpy as np

ages = np.array([[15, 20, 19, 18, 22], 
                   [36, 22, 74, 28, 56]])

teens = ages[ages < 18]
print(teens)

phd_guys = ages[ages >= 20]
print(phd_guys)

suspicous_guys = ages[ages >= 36]
print(suspicous_guys)

adults = ages[ages >= 18]
print(adults)

even = ages[ages % 2 == 0]
print(even)

odd = ages[ages % 2 == 1]
print(odd)

adultsvai = np.where(ages >= 18, ages, 0)
print(adultsvai)
