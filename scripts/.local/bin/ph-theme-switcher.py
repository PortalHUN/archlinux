import subprocess
from time import sleep
from os import setsid

WALLPAPER_PATH="/home/portal/Pictures/Wallpapers"
ROFI_TITLE="Select a wallpaper"
ROFI_THEME="material"

def get_wallpapers():
  return subprocess.run(["ls", WALLPAPER_PATH], capture_output=True).stdout.decode("utf-8").strip().split('\n') 

def input_string():
  string = ""
  for wallpaper in get_wallpapers():
    name = wallpaper.strip().split('.')[0]
    string += f"{name.capitalize()}\0icon\x1f{WALLPAPER_PATH}/{wallpaper}\n"
  return string.encode("utf-8")

def get_names():
  wallpapers = []
  for wallpaper in get_wallpapers():
    wallpapers.append(wallpaper.strip().split('.')[0].capitalize())
  return wallpapers

def Rofi():
  return subprocess.run(["rofi", "-dmenu", "-i", "-show-icons" "-p", ROFI_TITLE, "-theme", ROFI_THEME], input=input_string(), capture_output=True)

def HandleRofi():
  rof =  Rofi()
  if rof.returncode == 0:
    subprocess.run(["matugen", "image", f"{WALLPAPER_PATH}/{get_wallpapers()[get_names().index(rof.stdout.decode("utf-8").split('\n')[0])]}"]) 
    subprocess.run(["killall","waybar"])
    subprocess.Popen(["waybar"], preexec_fn=setsid)

HandleRofi()