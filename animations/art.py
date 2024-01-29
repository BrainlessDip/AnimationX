import random
import string
import time
import os
import colour
from colour import Color
# Animation Adjustment
max_space = 250
random_time = True
custom_text = False
custom_string = "Dip" # if custom_text is True
def generate_gradient_text(input_text, start_color, end_color):
   start = Color(start_color)
   end = Color(end_color)
   colors = list(start.range_to(end, len(input_text)))
   for char, color in zip(input_text, colors):
     hex_color = color.hex
     random_space = random.randint(1,max_space)
     if custom_text is False:
       space = ' '
     else:
       space = ''
     print(f"\033[38;2;{int(color.red*255)};{int(color.green*255)};{int(color.blue*255)}m{char}", end=space*random_space, flush=True)
   if custom_text is False:
     end = ''
   else: 
     end = ' ' * random.randint(1,500)
   print("\033[0m",end=end, flush=True)
   if random_time:
     delay_time = random.uniform(0.01,0.1)
   else:
     delay_time = 0.02
   time.sleep(delay_time)
def random_color_hex():
   color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
   return color
def art():
   while True:
     random_multi = random.randint(1,70)
     if custom_text is False:
       text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(random_multi))
     else:
       text = custom_string
     generate_gradient_text(text,random_color_hex(),random_color_hex())
art()