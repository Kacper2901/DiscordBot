# Private Server Discord Bot

A self-hosted Discord bot developed using Python and the `discord.py` library. The project is designed for private friend servers and is developed iteratively as a personal codebase to experiment with new features and automation.

## Features

### 1. Dynamic Voice Channel Welcomer
* **Trigger:** Monitors voice states and triggers when a user joins a voice channel (ensuring they did not just switch from another channel).
* **Action:** Connects to the respective voice channel and plays a personalized audio file welcoming the user by their name.

### 2. Voice Channel Roulette (`!gambling`)
* **Logic:** Selects a random user from the command caller's current voice channel and applies a **60-second timeout**.
* **Validation:** The command requires at least two users in the channel to execute normally.
* **Anti-Exploit Measure:** If a user executes the command without being connected to any voice channel, the bot applies a **100% chance of a 60-second timeout** to the caller.

## Work in Progress

* **Birthday Recognition System:** Developing a module that compares the current date with registered member birthdays. When a match is detected, the standard welcome audio is replaced with a personalized birthday greeting.

## Future Roadmap

* **Database Migration:** The application currently relies on in-memory Python dictionaries for data persistence. Future updates will involve migrating this structure to a relational or non-relational database management system to ensure data persistence and scalability.

## Tech Stack

* **Language:** Python
* **API Wrapper:** discord.py
* **Data Storage:** Python Dictionaries (In-memory)
