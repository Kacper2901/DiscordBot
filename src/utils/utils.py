import asyncio
import os
import datetime as dt
import random

from discord import *

from data import audioConfig
from data.BotConfig import MAIN_TEXT_CHANNEL_ID


def member_joined_any_channel(before, after):
    return before.channel == None and after.channel != None

async def join_and_play_audio(channel, audio_path):
    print("trying to play audio")
    source = FFmpegPCMAudio(audio_path)
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
    voice_client.play(source, after= after_playing)

    await done_playing.wait()
    await voice_client.disconnect()

async def greet_new_member(member):
    voice_state = member.voice
    if voice_state is None: return
    channel = voice_state.channel

    member_id = member.id
    dir_path = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.dirname(os.path.abspath(dir_path))
    try:
        member_audio_path = os.path.join(dir_path, audioConfig.id_audio.get(member_id))
        await join_and_play_audio(channel,member_audio_path)
    except AttributeError:
        return

async def ban_sixty_seconds(member, message, bot):
    main_text_channel = bot.get_channel(MAIN_TEXT_CHANNEL_ID)
    await main_text_channel.send(message)

    for i in range(3,0,-1):
        await asyncio.sleep(2)
        await main_text_channel.send(i)
    await asyncio.sleep(2)

    if (member.guild.owner == member):
        await main_text_channel.send("Wasz dyktator was ułaskawił")
        return

    try:
        await member.timeout(dt.timedelta(0,60), reason= message)
    except:
        print("timeout error")

    await main_text_channel.send(member.name + "!")

async def wheel_ban(channel, bot):
    members = channel.members
    members_count = len(members)


    if members_count <= 1: return
    random_member = members[random.randint(0, members_count - 1)]



    await ban_sixty_seconds(random_member, "Przerwe zrobi sobie...", bot)



