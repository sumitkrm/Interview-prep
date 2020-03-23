import math
def check_prime(num):
    if num<2:
        return False
    if num == 2 or num == 3:
        return True
    for i in range(3, int(math.sqrt(num))+1, 2):
        if num%i == 0:
            return False
    return True
  
check_prime(19)
