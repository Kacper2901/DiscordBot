import asyncio
import os
import datetime as dt
import random

from discord import *

from data import audioConfig
from data.servers import *
from data.users import get_users_guild


def member_joined_any_channel(before, after):
    return before.channel == None and after.channel != None



async def greet_new_member(new_member):
    member_voice_state = new_member.voice
    if member_voice_state is None:
        return

    member_channel = member_voice_state.channel
    member_id = new_member.id
    audio_directory_path = os.path.dirname(os.path.abspath(__file__))
    audio_directory_path = os.path.dirname(os.path.abspath(audio_directory_path))
    try:
        member_audio_path = os.path.join(audio_directory_path, "assets/audioFiles", audioConfig.users_id_audio.get(member_id))
        await join_and_play_audio(member_channel,member_audio_path)
    except AttributeError:
        return



async def join_and_play_audio(channel, audio_path):
    print("trying to play audio")
    audio_source = FFmpegPCMAudio(audio_path)
    try:
        voice_client = await channel.connect()
    except Exception as e:
        print(f'couldnt join voice channel {channel.name} : {e}')
        return

    def after_playing(error):
        if error:
            print("couldnt play audio")
        else:
            print("end of audio")
        done_playing.set()

    done_playing = asyncio.Event()
    voice_client.play(audio_source, after= after_playing)

    await done_playing.wait()
    await voice_client.disconnect()



async def ban_sixty_seconds(member, message, bot):
    members_guild = member.guild
    main_text_channel_id = get_guild_main_text_channel(members_guild.id)
    main_text_channel = bot.get_channel(main_text_channel_id)


    await main_text_channel.send(message)

    #countdown
    for i in range(3,0,-1):
        await asyncio.sleep(2)
        await main_text_channel.send(i)
    await asyncio.sleep(2)

    if (members_guild.owner == member):
        await main_text_channel.send("Wasz dyktator was ułaskawił")
        return

    try:
        await member.timeout(dt.timedelta(0,60), reason= message)
    except:
        print("timeout error")

    await main_text_channel.send(f" {member.name}!")



async def wheel_ban(channel, bot):
    members = channel.members
    members_count = len(members)

    if members_count <= 1: return
    random_member = members[random.randint(0, members_count - 1)]

    await ban_sixty_seconds(random_member, "Przerwe zrobi sobie...", bot)



