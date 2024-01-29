import time
import random
from colour import Color
import random
from colour import Color
import random
from threading import Thread
## Animation Seed
animation_seed = [1,2,3,-1,-2,-3]
max_terminal_size = 500

def color_text(text):
    red = int(random.randint(0,1))
    green = int(random.randint(0,1))
    blue = int(random.randint(0,1))
    random_color = Color(rgb=(red, green, blue))
    hex_color = random_color
    return f"\033[38;2;{hex_color.rgb[0]*255:.0f};{hex_color.rgb[1]*255:.0f};{hex_color.rgb[2]*255:.0f}m{text}\033[0m"
def random_num():
  global animation_seed 
  return random.choice(animation_seed)
def snake():
  global max_terminal_size 
  i = 20
  incrementing = True
  while True:
    text = " " * (i-1)
    print(text + "*")
    print(color_text(text + "*"))
    i += random_num()
    if i < 10:
      i = 20
    if i > max_terminal_size:
      i = 65
    
    time.sleep(random.uniform(0.015,0.02))
threads = []
for _ in range(2):
   t = Thread(target=snake)
   t.start()
   threads.append(t)
for t in threads:
   t.join()
