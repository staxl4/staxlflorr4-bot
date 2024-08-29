![Static Badge](https://img.shields.io/badge/Version_Alpha_1.0.0-blue)

## Information
This bot is taking a while.
This project started of as a complete joke and has turned into something decent.

## Commands
"!spin" you roll a mob and a rarity and get credits depending on what you got\n
"!credit [user {optional}]" checks how many Social credits a user has. If someone is mentioned they will be checked. If no one is mentioned the author will be checked.\n
"!sac [amount]" sacrifice an amout of credits for a luck boost (min 100)\n
"!leaderboard" show top 10 people with the most credits in the server (can bug easily if it does dm one of us so we can fix it)\n
"!giveaway [duration in minutes] [prize]" start a giveaway (admin only)\n
    "!enter" enter the current giveaway (dont do 2 at the same time it usually breaks)\n
    "!endgiveaway" end the current giveaway (admin only)\n
"!endsac" ends the current sacrifice (admin only) Great for trolling!\n
"!addcredits [user] [amount]" add credits to a user (admin only)\n
"setcredits [user] [amount]" set a users credits (admin only)\n
"removecredits [user] [amount {in positive amount}]" remove credits from a user (admin only)\n

## Instructions for setup
Use python. (This bot is written in python. To edit the code use a code editor such as VScode).
to start copy the code down or download it whatever you prefer.
In terms of adding this bot to your own server replace the "your-bot-token" at the bottom of the code, with your bot token. in the "!spin" command change the line:

```
    "if ctx.channel.name != 'spin':
        await ctx.send("This command can only be used in the #spin channel.")
        return" 
```

replace the "spin" with the channel name you want the bot to be used in or delete it entirely depending on how you want to use this bot.

*Optional*

If you would like to make your own bot and pair the code with it you have to use the [discord devoloper portal](https://discord.com/developers).

## Help us please
As this bot is still being developed, if you have any suggestions or find any bugs (there will be), please DM one of us on discord with the usernames below

![Static Badge](https://img.shields.io/badge/Discord-_apollo147-blue?style=plastic&labelColor=%23000000)
![Static Badge](https://img.shields.io/badge/Discord-_staxlflorr-blue?style=plastic&labelColor=%23000000)

## Credits 
apollo147 and staxl4 made the bot.

Thank you to peterpeterp who made the flowr discord server bot, as this one is heavily inspired by it.
