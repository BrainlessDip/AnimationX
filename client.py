## Client Of Animation X 
import os 
import colour
import random
import time
import json
import sys
import requests
import threading
from pick import pick
from colour import Color
# Code Info
verison = 1.4

def logo(delay):
  art = """                 _                 _   _              __   __
     /\         (_)               | | (_)             \ \ / /
    /  \   _ __  _ _ __ ___   __ _| |_ _  ___  _ __    \ V / 
   / /\ \ | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \    > <  
  / ____ \| | | | | | | | | | (_| | |_| | (_) | | | |  / . \ 
 /_/    \_\_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_| /_/ \_\ """
  generate_gradient_text(art,delay)
  print("\n")
def random_color_hex():
   color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
   return color
def generate_gradient_text(input_text,delay):
   delay = delay/len(input_text)
   start = Color(random_color_hex())
   end = Color(random_color_hex())
   colors = list(start.range_to(end, len(input_text)))
   for char, color in zip(input_text, colors):
     hex_color = color.hex
     random_space = 1
     print(f"\033[38;2;{int(color.red*255)};{int(color.green*255)};{int(color.blue*255)}m{char}", end="", flush=True)
     time.sleep(delay)
   print("\033[0m",end=" ", flush=True)
def custom_generate_gradient_text(input_text,start,end,delay):
   delay = delay/len(input_text)
   start = Color(start)
   end = Color(end)
   colors = list(start.range_to(end, len(input_text)))
   for char, color in zip(input_text, colors):
     hex_color = color.hex
     random_space = 1
     print(f"\033[38;2;{int(color.red*255)};{int(color.green*255)};{int(color.blue*255)}m{char}", end="", flush=True)
     time.sleep(delay)
def color_x(input_text):
   color = Color(random_color_hex())
   hex_color = color.hex
   random_space = 1
   print(f"\033[38;2;{int(color.red*255)};{int(color.green*255)};{int(color.blue*255)}m{input_text}", end="", flush=True)
def loading_server_data():
  global verison
  logo(0.00001)
  custom_generate_gradient_text(f"[ - ] Verison {verison}\n\n","#FFFFFF","#FFFFFF",0.5)
  menu_thread = threading.Thread(target=loaded_menu)
  menu_thread.start()
def version_verify(verison_api):
  global verison
  if verison_api != verison:
     custom_generate_gradient_text("[ - ] Script Is Outdated\n\n","#006400","#CCFF33",0.5)
     custom_generate_gradient_text(f"[ - ] Are You Want To Update This Script To {verison_api} [Y\\N]","#006400","#CCFF33",0.5)
     ask = input(" ")
     if ask.lower() == "n":
       custom_generate_gradient_text("\n[ - ] Permission Declined\n\n","#006400","#CCFF33",0.5)
     else:  
       custom_generate_gradient_text("\n[ - ] Updating Script\n\n","#006400","#CCFF33",0.5)
       update_script(verison_api)
     return "Update"
def update_script(verison_api):
   script = requests.get("https://animation-x.dipdey.repl.co/script").text
   filename = sys.argv[0]
   with open(filename, 'w') as f:
     f.write(script)
   custom_generate_gradient_text(f"[ - ] Script Updated [{verison_api}]\n\n","#007200","#CCFF33",0.5)
   custom_generate_gradient_text(f"[ - ] Restarting Script\n\n","#007200","#CCFF33",0.5)
   os.system("python client.py")
def loaded_menu():
   try:
     server_data = requests.get("https://animation-x.dipdey.repl.co/main").json()
   except Exception as e:
     custom_generate_gradient_text("[ - ] No Internet Connection Found\n\n","#38B000","#CCFF33",0.5)
     return 0
   verison = server_data["version"]
   check = version_verify(verison)
   if check == "Update":
     return 
   notice = server_data['notice']
   custom_generate_gradient_text(f"[ MESSAGE ] {notice}\n","#008000","#00FF00",0.5)
   animations = server_data["animations"]
   custom_generate_gradient_text("[ - ] Press Enter To Select Animation :","#008000","#00FF00",0.5)
   input(" ")
   index = pick(animations,indicator="> ",title="> ANIMATION LIST <")
   start_animation(index[1],animations)
def start_animation(index,animations):
   animation_name = animations[index]
   custom_generate_gradient_text(f"\n[ - ] Starting {animation_name} \n","#008000","#00FF00",0.5)
   os.system("clear")
   os.system(f"curl -s https://animation-x.dipdey.repl.co/code/{index} | python")
def main_menu():
  os.system("clear")
  loading_server_data()
main_menu()