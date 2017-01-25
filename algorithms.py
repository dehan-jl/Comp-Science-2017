def validate(x, m):
   if (x > m):
      return False
   elif (x <= 0):
      return False
   else:
      return True

A = 42
A = A + 10
vali = False
c_total = 0
c_max = 0

if (A > 40):
   while (vali == False):
      B = int(input("Enter an int less than 10: "))
      vali = validate(B, 10)

vali = False

for i in range(B):
   while (vali == False):
      C = int(input("Enter an int less than 100: "))
      vali = validate(C, 100)
   c_total += C
   if (C > c_max):
      c_max = C

ave = c_total/B
print("Average:", ave, "Max:", c_max)
