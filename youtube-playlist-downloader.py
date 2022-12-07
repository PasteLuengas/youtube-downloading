from pytube import *
import moviepy.editor as mp
import os

#Se define la duncion para descargar en MP3
def DownloadMP3(url, W):
    download_folder = W
    format_list2 = YouTube(url).streams.filter(mime_type='audio/mp4').first().download(download_folder)
    os.chdir(download_folder)
    print(os.getcwd())
    
    videotitle = YouTube(url).title
    character = ",'"
    
    for x in range(len(character)):
        videotitle = videotitle.replace(character[x],"")
    
    mp4_file = videotitle + '.mp4'
    mp3_file = videotitle + '.mp3'
    clip = mp.AudioFileClip(mp4_file)
    clip.write_audiofile(mp3_file)
    clip.close()
    os.remove(mp4_file)
    
    
#Se define la duncion para descargar en MP4
def DownloadMP4(url, W):
    download_folder = W
    format_list2 = YouTube(url).streams.filter(mime_type='video/mp4').first().download(download_folder)
    os.chdir(download_folder)
    print(os.getcwd())
    
    videotitle = YouTube(url).title
    character = ",'"
    
    for x in range(len(character)):
        videotitle = videotitle.replace(character[x],"")
    
    mp4_file = videotitle + '.mp4'

#Se definen Variables
video_title= ""
video_filename = ""

#El usuario inserta el URL de la lista y donde la quiere guardar
plist = input("URL: ")
place = input("Where you wanna save the playlist files?")
typefile = input("Save as (MP3/MP4)")

if "https://www.youtube.com/playlist?list=" in plist and typefile.lower() == "mp3":
    playlist = Playlist(plist)
    print(f'Downloading: ' + playlist.title)

    for video in playlist.videos:
        videoLink = "https://www.youtube.com/watch?v=" + video.video_id
        DownloadMP3(videoLink, place)
        
if "https://www.youtube.com/playlist?list=" in plist and typefile.lower() == "mp4":
    playlist = Playlist(plist)
    print(f'Downloading: ' + playlist.title)

    for video in playlist.videos:
        videoLink = "https://www.youtube.com/watch?v=" + video.video_id
        DownloadMP4(videoLink, place)
        
if "https://www.youtube.com/watch?v=" in plist and typefile.lower() == "mp3":
    DownloadMP3(plist, place)
    
if "https://www.youtube.com/watch?v=" in plist and typefile.lower() == "mp4":
    DownloadMP4(plist, place)
    

    




    
    










