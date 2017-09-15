#!/usr/bin/python3
import re
from pibot.PiBot import PiBot
import tools.youtube

bot = PiBot("407840078:AAGEZ5wxVFr9veIjv1apy0U0L9J4tLQZsHw")


def main():
    new_offset = None
    while True:
        bot.get_updates(new_offset)

        last_update = bot.get_last_update()

        last_update_id = last_update["update_id"]
        last_chat_text = last_update["message"]["text"]
        last_chat_id = last_update["message"]["chat"]["id"]

        # Simple ping-pong dialog
        if last_chat_text.lower() == "ping":
            bot.send_message(last_chat_id, "Pong")

        # Matches YouTube link
        # noinspection PyPep8
        yt_regex = r"^(?:https?://)?(?:www\.)?(?:youtu\.be/|youtube\.com(?:/embed/|/v/|/watch\?v=))([\w-]{10,12})$"
        matches = re.search(
            yt_regex,
            last_chat_text,
            re.VERBOSE | re.IGNORECASE
        )
        if matches:
            tools.youtube.play(matches.group(), True)
            bot.send_message(
                last_chat_id,
                "Playing video from YouTube",
                PiBot.MARKDOWN
            )

        new_offset = last_update_id + 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
