def is_leap(year):
    
    if year % 400 == 0: # 400 e tam bölünüyorsa artık yıl.
        return True
    elif year % 100 == 0: # 100 e tam bölünüyorsa artık yıl değil
        return False
    elif year % 4 == 0: # 4 e tam bölünüyorsa artık yıl.
        return True
    else:
        return False # diğer durumlarda, artık yıl değildir.



year = int(input())
print(is_leap(year))

# 400 e tam bölünüyorsa artık yıl.
# 100 e tam bölünüyorsa artık yıl değil
# 4 e tam bölünüyorsa artık yıl.
# diğer durumlarda, artık yıl değildir.

