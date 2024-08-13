import requests
import os 
from dotenv import load_dotenv
import subprocess
from pyfiglet import figlet_format
from termcolor import colored

load_dotenv()

logo_name = 'Orange Downloader'
ascii_banner = figlet_format(logo_name)
print(colored(ascii_banner,'light_yellow'))
print(colored("Made By Nishant.",'light_blue'))
print(colored("This Application helps user to download all videos of an playlist just by iputing playlist id.\n",'light_blue'))
print(colored("CAUTION : DO NOT Enter Wrong Video id or Playlist id because Of lack or exception handling in application.\n",'light_magenta'))
print(colored("Applicatin Version: V2 \n",'light_red'))

Ask = input("Choose one option from below:\n1.Single video download\n2.Complete playlist download\nEnter:")

if Ask == "1":

    video_id = input(f"{colored("\nEnter video id:",'green')}")

    url = "https://yt-api.p.rapidapi.com/video/info"
    querystring = {"id":video_id}

    headers = {
	    "x-rapidapi-key": os.getenv('API_KEY'),
	    "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 401:
        print(colored("API Key is invalid. Please check your API key.",'red'))
    elif response.status_code == 200:
        data = response.json()
        print(f"Video Title:{data['title']}")
        print(f"Lenght :{data['lengthSeconds']} seconds")
        print(f"Video Views :{data['viewCount']}")
        print(f"Channel Title :{data['channelTitle']}")
        print(f"Video Description :{data['description']}")
        process = subprocess.Popen('cmd', stdin=subprocess.PIPE, shell=True, text=True)
        process.stdin.write(f'y2mate -f mp4 -q best {video_id}\n')
        process.stdin.write('exit\n')
        process.stdin.flush()
        process.communicate()
        print(colored("Your Videos Has Been Downloaded Successfully.\n",'light_green'))

elif Ask == '2':

    url = "https://yt-api.p.rapidapi.com/playlist"

    query = input(f"{colored('Enter Playlist id :','green')}")
    querystring = {"id":query}

    headers = {
	    "x-rapidapi-key": os.getenv('API_KEY'),
	    "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 401:
         print(colored("API Key is invalid. Please check your API key.",'red'))
    elif response.status_code == 200:
        main = response.json()
        print(f"Video Title:{main['meta']['title']}\n")
        print(f"Video Title:{main['meta']['description']}")
        print(f"Total Videos:{main['meta']['videoCountText']}") 
        print(f"Toral Views:{main['meta']['viewCountText']}")
        total_video = int(main['meta']['videoCount'])
        process = subprocess.Popen('cmd', stdin=subprocess.PIPE, shell=True, text=True)
        for i in range(total_video):
            v_id = main['data'][i]['videoId']
            process.stdin.write(f'y2mate -f mp4 -q best {v_id}\n')
        process.stdin.write('exit\n')
        process.stdin.flush()
        process.communicate()
        print(colored("Your playlist Has Been Downloaded Successfully.\n",'light_green'))
else:
    print(colored("Your Have Entered Wrong Option. Restart The Application.\n",'light_red'))








