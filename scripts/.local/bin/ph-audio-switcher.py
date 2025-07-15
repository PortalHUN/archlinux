import subprocess

ROFI_THEME="gruvbox-light"
ROFI_TITLE="Audio devices"
SINK_ID=0

IDs = []
Titles = []
chosen = ""

def get_sinks():
  return subprocess.run(["pactl","list","sinks"],capture_output=True, text=True).stdout.split('Ports:')[1].split('Active Port:')[0].strip().replace("\t","").split('\n')

def split_into_arrays(string):
  for item in string:
    manipulated = item.split('(')[0].split(':')
    IDs.append(manipulated[0].strip())
    Titles.append(manipulated[1].strip())

def input_string():
  return "\n".join(Titles).encode("utf-8")

def launch_rofi():
  return subprocess.run(["rofi", "-dmenu", "-i", "-theme", ROFI_THEME, "-p", ROFI_TITLE], input=input_string(), capture_output=True)


#Main
split_into_arrays(get_sinks())
rofi = launch_rofi()

if rofi.returncode == 0:
  chosen = rofi.stdout.__str__().strip()[2:-3]
  subprocess.run(["pactl", "set-sink-port", f"{SINK_ID}", IDs[Titles.index(chosen)]])
