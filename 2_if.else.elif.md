
![Ekran Alıntısı](https://github.com/user-attachments/assets/ec95f6f3-869c-44fe-94e9-5b792fec23b0)



```python
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20: 
    print("Not Weird")
```
