<h1 align="center">
  Steam ID Checker
</h1>

<p align="center">
  An easy-to-use and open-source tool to check the validity of Steam IDs with real-time notification support via Discord and Telegram.
</p>

<p align="center">
  This project is licensed under the <a href="LICENSE">MIT License</a>. See the LICENSE file for more details.
</p>

### Key Features

* **Easy to Use:** Intuitive interface for quick verification.
* **Open-Source:** Transparency and the possibility to contribute to the project.
* **Discord Webhook Support:** Receive real-time results directly in your Discord channels.
* **Telegram Bot/Webhook Support:** Get notifications via Telegram, either through a Bot or Webhook.
* **Real-time Results Saving:** Verification results are automatically saved as they are processed.

### Prerequisites

* [Python](https://www.python.org/downloads/) installed on your system.

### How to Install and Use?

1.  Go to the [Releases](https://github.com/ripsaku/steam-id-checker/releases) section and download the latest available version of the program.
2.  Open the downloaded `.exe` file.
3.  Enter your Discord webhook URL when prompted (optional).
4.  Select the text file (`.txt`) containing the list of Steam IDs you want to check.

### How to Set Up a Discord Webhook?

1.  Open Discord in your browser or desktop application.
2.  Create a new server or use an existing one (you'll need the "Manage Webhooks" permission).
3.  Go to **Server Settings** > **Webhooks**.
4.  Click on **Create Webhook**.
5.  Choose a name for the webhook, an avatar (profile picture), and the channel where you want to receive messages.
6.  Copy the provided **Webhook URL** and paste it into the program when prompted.

### How to Set Up a Telegram Bot API?

#### Getting Your Bot API Token

1.  Start a chat with [@BotFather](https://t.me/BotFather) on Telegram.
2.  Create a new bot or use an existing one.
3.  Get the **Token**. You will receive it when creating a new bot. Alternatively, use the `/mybots` command, select your bot, and click on "API Token".
4.  Copy the Token and paste it into the program when prompted.

#### Getting Your Chat ID

1.  Start a chat with [@RawDataBot](https://t.me/RawDataBot) on Telegram.
2.  In the message it sends you, look for the "chat" section, and below it, you'll see "id:".
3.  Copy the **Chat ID** and paste it into the program when prompted.
