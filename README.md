- Installation for Linux
```
sudo apt update
apt install tmux python3-pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

nano .env   # refer to .env example section
nano last_id.json   # refer to last_id.json section
```

- Installation for Mac

Open terminal and execute below commands
```
# install Homebrew( you can skip if you already have brew installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> ~/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)


brew install tmux python3

cd go/to/this/directory   # Go to directory where this README file is located.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

nano .env   # refer to .env example section
nano last_id.json   # refer to last_id.json section
deactivate   # leave from python venv
```

- Starting Bot
```
tmux new -s discordbot
source .venv/bin/activate
python bot.py
Ctrl + B -> D   # detach from tmux
```

- Stopping Bot
```
tmux kill-session -t discordbot
```


- .env example
[Discord documents](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID#h_01HRSTXPS5FMK2A5SMVSX4JW4E)
```
TOKEN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"   # token needed for running bot
CHANNEL_LIST = "123456789011111, 0987654321111"   # more info above discord Discord documents
RSS_URL = "https://example.hatenablog.com/rss"
```

- last_id.json
```
{"last_id": "hoge(なんでもいい)"}
```



<!-- 以下は、Botの起動にsystemdを用いていたが、Botが動かなくなったため上記のtmuxに変更 -->
<!-- - Installation
```
sudo apt update
apt install python3-pip
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

sudo nano /etc/systemd/system/discordbot.service    # refer to service registration section
nano .env   # refer to .env example section
nano last_id.json   # refer to last_id.json section

sudo systemctl enable discordbot    # For Product
sudo systemctl start discordbot     # For Product

python bot.py # For Test(Bot will be offline when console is closed)
```


- service registration
sudo nano /etc/systemd/system/discordbot.service

write your user directory name instead of $GCP_USER$
```
[Unit]
Description = DiscordBot

[Service]
ExecStart = /home/$GCP_USER$/.venv/bin/python /home/$GCP_USER$/bot.py
Restart = always
Type = simple

[Install]
WantedBy = multi-user.target
```

- .env example
```
TOKEN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHANNEL_LIST = "123456789011111, 0987654321111"
RSS_URL = "https://example.hatenablog.com/rss"
```

- last_id.json
```
{"last_id": "any words"}
``` -->