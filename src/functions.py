import mcpi.minecraft as minecraft
import mcpi.block as block

def chat(mc, string, type=3):
    if type == 0:
        start = "(ERROR:" # Danger
        pystart = '\033[91m'
    elif type == 1:
        start = "(warn: " # Warning
        pystart = '\033[93m'
    elif type == 2:
        start = "(info: " # Info
        pystart = '\033[94m'
    else:
        start = "(" # Normal
        pystart = '\033[0m'
    chat_string = start + "PyMcBuilder) " + string
    mc.postToChat(chat_string)
    print(pystart+string+'\033[0m')
