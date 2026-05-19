
from utils.utils import *
from data.BotConfig import *

intents = Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True
client = Client(intents = intents)


@client.event
async def on_ready():
    await client.change_presence(status= Status.invisible)
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if(message.content == "!gambling"):
            author_voice_state =  message.author.voice

            #timeout author if their not in any voice channel
            if author_voice_state is None or author_voice_state.channel is None:
                print("timeout penalty for not being in any voice channel")
                await ban_sixty_seconds(
                    message.author,
            "Ojoj kolego... Nastepnym razem wbij na kanal jak chcesz sie bawic",
                    client
                )
                return

            channel = author_voice_state.channel
            print("starting the wheel")
            await wheel_ban(channel,client)

@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user: return
    if member_joined_any_channel(before, after):
        print(f'{member.name} joined {after.channel.name}')
        await asyncio.sleep(2)
        await greet_new_member(member)


client.run(BOT_TOKEN)
