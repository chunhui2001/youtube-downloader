from asyncio import streams
from pytube import YouTube

print("LK Developers YouTube Downloader Bot")

url = input("🍓 ☠  𝗘𝗻𝘁𝗲𝗿 𝗬𝗼𝘂𝗿 𝗨𝗥𝗟 𝗛𝗲𝗿𝗲 🐸 ♚ : ")
my_video = YouTube(url)

print("💞💲  𝚅𝙸𝙳𝙴𝙾 𝚃𝙸𝚃𝙻𝙴  🐝♟") 
print(my_video.title)


print("💞💲  𝚅𝙸𝙳𝙴𝙾 THUMBNAIL URL  🐝♟") 
print(my_video.thumbnail_url)

my_video = my_video.streams.get_highest_resolution()

my_video.download()

print("🍉 ⋆ 🍉 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝐃🍪𝐰𝐧𝐥🏵𝐚𝐝𝐞𝐝 𝐕𝐢𝐝𝐞🍬 🍉 ⋆ 🍉")

