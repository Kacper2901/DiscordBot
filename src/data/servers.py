guild_id_data = {
    #server_id: (server_name, main_text_channel_id)
    1423123: ("Server name", 124212312),
}

def get_guild_name(server_id):
    return guild_id_data.get(server_id)[0]

def get_guild_main_text_channel(server_id):
    return guild_id_data.get(server_id)[1]