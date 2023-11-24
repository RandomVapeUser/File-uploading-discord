from discord_webhook import DiscordWebhook, DiscordEmbed
import sys
import os
import time

print("""

    File Sender
    [1] - Send file to discord
    [2] - Test

    """)

X = int(input(" "))

file_name2 = " "
user = os.environ.get("USERNAME")

def file_name():
    
    global file_name2

    while True:
        
        try: 
            if X == 1:
                os.system("cls")
                Y = input("Name: ")
                time.sleep(2)
                Z = input("File name: ")
                file_name2 = Z
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
                os.system("cls")
                continue
        except SyntaxError:
            print("Nuh uh print numbers not words you idiot")
            os.system("cls")
            continue



webhook = DiscordWebhook(url = "https://discord.com/api/webhooks/1172913800006094888/2wYTsKqbvPfiDE4mCIxous-hDZcJzYKhr6JMIitQuPWvZZSpkYN7jufZpiUlu9eN6jKN")

embed = DiscordEmbed(title="Test", description="New File!", color="03b2f8")
webhook.add_embed(embed)

def send_file():

    global Z
    global user

    with open(fr"C:\Users\{user}\Downloads\{file_name2}", 'rb') as file:
        content = file.read()
        webhook.add_file(file=content, filename="Test File")
        webhook.execute()
        print("File Successfully sent!")
        print("Goodbye!")
        time.sleep(2)
        sys.exit()

while True:
    try:
        file_name()
        send_file()
    except FileNotFoundError:
        print("File not found, please try again")
        time.sleep(2)
        os.system("cls")
        continue
