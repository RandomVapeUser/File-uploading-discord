from discord_webhook import DiscordWebhook as dc
import sys
import os
import time

print("""

    File Sender
    [1] - Send file to discord
    [2] - Test

    """)

X = input(" ")

while True: 

    if X == 1:
        os.system("cls")
        Y = input("Name: ")
        time.sleep(2)
        Z = input("File name: ")
        break
    elif X == 2:
        print("Test")
        time.sleep(2)
        print("Exiting...")
        time.sleep(2)
        sys.exit()
    else:
        print("No such number!")
        os.system("cls")
        time.sleep(2)
        continue

webhook = dc(url = "https://discord.com/api/webhooks/1172913800006094888/2wYTsKqbvPfiDE4mCIxous-hDZcJzYKhr6JMIitQuPWvZZSpkYN7jufZpiUlu9eN6jKN")

embed = DiscordEmbed(title = "Discord File", description = "Success")
webhook.add_embed(embed)

try:
    with ex
print("File Successfully sent!")
print("Goodbye!")
