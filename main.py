import discord
from discord.ext import commands
import random
import json
import os

# Default data structure
default_db = {
    "Social_credits": {},
    "luck_boost": {},
    "sac_active": False,
    "sac_amount": 0,
    "sac_spins": 0,
    "spins_count": {},
    "sac_spins_limit": 10,
    "custom_luck_multiplier": 1,
    "market": {}
}

# Ensure the database file exists
if not os.path.exists("db.json"):
    with open("db.json", "w") as f:
        json.dump(default_db, f, indent=4)

# Load the database file
with open("db.json", "r") as f:
    db = json.load(f)

# Function to save the database
def save_db():
    with open("db.json", "w") as f:
        json.dump(db, f, indent=4)

# Ensure user data exists
def ensure_user_data(user_id):
    user_id_str = str(user_id)
    if user_id_str not in db["Social_credits"]:
        db["Social_credits"][user_id_str] = 0
    if user_id_str not in db["spins_count"]:
        db["spins_count"][user_id_str] = 0

# Get user credits
def get_user_credits(user_id):
    return db["Social_credits"].get(str(user_id), 0)

# Set user credits
def set_user_credits(user_id, credits):
    db["Social_credits"][str(user_id)] = credits

# Initialize bot with command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Rarity names, credits, and colors
rarityNames = [
    'Common', 'Uncommon', 'Rare', 'Epic', 'Legendary', 'Mythic', 'Ultra', 'Super', 'Omega', 
    'Fabled', 'Divine', 'Supreme', 'Omnipotent', 'Astral', 'Celestial', 'Seraphic', 'Transcendent', 
    'Quantum', 'Galactic', 'Eternal', 'cHa0s', 'Quantum Shard'
]
rarityCredits = [
    -5, 1, 2, 5, 10, 25, 100, 250, 1000, 2500, 10000, 25000, 100000, 250000, 1000000, 2500000, 
    10000000, 25000000, 100000000, 250000000, 1000000000, 10**20
]
rarityColors = {
    'Common': 0x66cdaa,
    'Uncommon': 0xf0e68c,
    'Rare': 0xadd8e6,
    'Epic': 0xd8bfd8,
    'Legendary': 0xcc0000,
    'Mythic': 0x00008b,
    'Ultra': 0xffb6c1,
    'Super': 0x32cd32,
    'Omega': 0x404040,
    'Fabled': 0xff8c00,
    'Divine': 0x4b0082,
    'Supreme': 0xff1493,
    'Omnipotent': 0x808080,
    'Astral': 0x004d00,
    'Celestial': 0x87cefa,
    'Seraphic': 0xff69b4,
    'Transcendent': 0xffffff,
    'Quantum': 0x000000,
    'Galactic': 0xa64d79,
    'Eternal': 0x13426d,
    'cHa0s': 0x4c1130
}

# Mob types and multipliers
mobType = [
    'Ladybug', 'Bee', 'Hornet', 'Spider', 'Baby Ant', 'Worker Ant', 'Soldier Ant', 'Queen Ant', 
    'Ant Hole', 'Dandelion', 'Rock', 'Centipede', 'Evil Centipede', 'Dark Ladybug', 'Beetle', 
    'Scorpion', 'Cactus', 'Sandstorm', 'Fire Ant Burrow', 'Fire Ant', 'Fire Queen Ant', 'Desert Centipede', 
    'Locust', 'Desert Moth', 'Shiny Ladybug', 'Crab', 'Jellyfish', 'Shell', 'Starfish', 'Sponge', 
    'Leech', 'Sea Urchin', 'Bubble', 'Plastic', 'Square', 'Pentagon', 'Hexagon'
]
mobMulti = [
    1, 1.5, 1, 1, 1, 1, 1, 1.5, 1, 1.5, 1, 1, -1, -2, 1, 1, 1, 1.5, 2, 1, 1.5, 1.5, 1, 1.5, 5, 
    1, 1, 1.5, 1, 1, 1, 1.5, 1, 3, 10, 1000, -666
]

# Event when bot is ready
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    @bot.event
    async def on_command_error(ctx, error):
        print(f"Error occurred: {error}")
        await ctx.send("An error occurred. Please check the bot logs for details.")

# Spin command
@bot.command()
async def spin(ctx):
    if ctx.channel.name != 'spin':
        await ctx.send("This command can only be used in the #spin channel.")
        return

    try:
        user_id = ctx.author.id
        ensure_user_data(user_id)

        # Set default luck multiplier to 1
        luck_multiplier = db.get("custom_luck_multiplier", 1)

        # Apply sacrifice luck boost if active
        if db.get("sac_active", False):
            sac_amount = db.get("sac_amount", 0)
            luck_multiplier = round(max(0.207125 * (2.34915 * sac_amount + 463.458) ** 0.5 - 4.48083, 1), 1)

        randomValue = random.random()
        rng = randomValue / (((luck_multiplier - 1) * 0.7) + 1)

        rarity = 0

        if rng < 0.55:
            rarity+=1
        if rng < 0.35:
            rarity+=1
        if rng < 0.2:
            rarity+=1
        if rng < 0.1:
            rarity+=1
        if rng < 0.05:
            rarity+=1
        if rng < 0.02:
            rarity+=1
        if rng < 0.01:
            rarity+=1
        if rng < 0.005:
            rarity+=1
        if rng < 0.0025:
            rarity+=1
        if rng < 0.001:
            rarity+=1
        if rng < 0.00044:
            rarity+=1
        if rng < 0.00014:
            rarity+=1
        if rng < 0.00004:
            rarity+=1
        if rng < 0.00001:
            rarity+=1
        if rng < 0.000004:
            rarity+=1
        if rng < 0.000001:
            rarity+=1
        if rng < 0.0000004:
            rarity+=1
        if rng < 0.0000001:
            rarity+=1
        if rng < 0.00000004:
            rarity+=1
        if rng < 0.00000001:
            rarity+=1
        if rng == 0:
            rarity+=1

        # Determine mob type and multiplier
        mob_index = random.randint(0, len(mobType) - 1)
        mob_name = mobType[mob_index]
        mob_multiplier = mobMulti[mob_index]

        final_credits = rarityCredits[rarity] * mob_multiplier

        current_credits = get_user_credits(user_id)
        new_credits = current_credits + final_credits
        set_user_credits(user_id, new_credits)

        # Get the color for the rarity
        raritycolor = rarityColors[rarityNames[rarity]]

        embed = discord.Embed(color=raritycolor)
        embed.add_field(name=f"{rarityNames[rarity]} {mob_name}", value=f"You got a {rarityNames[rarity]} {mob_name}!", inline=False)
        if float(luck_multiplier) > 1:
            embed.add_field(name="Frenzy!", value=f"{luck_multiplier}x luck from a sacrifice", inline=False)
        embed.add_field(name="Rare Mob Multiplier!", value=f"x{mob_multiplier}", inline=False)
        embed.add_field(name=f"+{final_credits} CREDITS", value=f"{rarityCredits[rarity]} ({rarityNames[rarity]}) x{mob_multiplier} ({mob_name})", inline=False)

        if db.get("sac_active", False):
            sac_spins = db.get("sac_spins", 0)
            if sac_spins >= db.get("sac_spins_limit", 10):
                if not db.get("sac_limit_reached", False):
                    await ctx.send("Sacrifice spins limit reached.")
                    db["sac_limit_reached"] = True
                    # Reset luck boost and other sacrifice-related values
                    db["custom_luck_multiplier"] = 1
                    db["sac_amount"] = 0
                    db["sac_active"] = False
                    db["sac_spins"] = 0
                # Send the result embed even if the limit is reached
                await ctx.send(embed=embed)
            else:
                db["sac_spins"] += 1
                await ctx.send(embed=embed)
        else:
            await ctx.send(embed=embed)
            db["spins_count"][str(user_id)] += 1

        save_db()

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

# Market Add Modal class (for adding market items)
class MarketAddModal(discord.ui.Modal):
    def __init__(self, user_id):
        super().__init__(title="Add Market Item")
        self.user_id = user_id
        # Add TextInputs to the Modal
        self.add_item(discord.ui.TextInput(label="Name of Service", placeholder="Enter the name of the service", custom_id="name_input", required=True))
        self.add_item(discord.ui.TextInput(label="Description of Service", placeholder="Enter a description", custom_id="description_input", required=True))
        self.add_item(discord.ui.TextInput(label="Price of Service (min 10k)", placeholder="Enter the price", custom_id="price_input", required=True))

    async def callback(self, interaction: discord.Interaction):
        # Retrieve TextInput values
        name = self.children[0].value
        description = self.children[1].value
        price_str = self.children[2].value

        try:
            price = int(price_str)
            if price < 10000:
                await interaction.response.send_message("Price must be at least 10,000 credits.", ephemeral=True)
                return
        except ValueError:
            await interaction.response.send_message("Invalid price format.", ephemeral=True)
            return
        
        item_id = len(db["market"]) + 1
        db["market"][str(item_id)] = {
            "owner": str(self.user_id),
            "name": name,
            "description": description,
            "price": price
        }
        save_db()
        await interaction.response.send_message(f"Market item '{name}' added successfully.", ephemeral=True)

# Button to trigger the modal
class MarketAddButton(discord.ui.Button):
    def __init__(self):
        super().__init__(label="Add Market Item", style=discord.ButtonStyle.blurple)

    async def callback(self, interaction: discord.Interaction):
        # Show the modal when the button is clicked
        modal = MarketAddModal(interaction.user.id)
        await interaction.response.send_modal(modal)

# Add Market Command
@bot.command()
async def addmarket(ctx):
    # Send a message with a button to trigger the modal
    view = discord.ui.View()
    view.add_item(MarketAddButton())
    await ctx.send("Click the button below to add a market item.", view=view)

# Market Command
@bot.command()
async def market(ctx, page: int = 1):
    items_per_page = 5
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    
    market_items = list(db["market"].values())[start_index:end_index]
    if not market_items:
        await ctx.send("No items found on this page.")
        return
    
    embed = discord.Embed(title=f"Market - Page {page}", color=0x00ff00)
    for item in market_items:
        embed.add_field(
            name=item["name"],
            value=f"**Description:** {item['description']}\n**Price:** {item['price']} credits\n**Owner:** <@{item['owner']}>",
            inline=False
        )
    
    await ctx.send(embed=embed)

# Remove Market Command
@bot.command()
@commands.has_permissions(administrator=True)
async def delmarket(ctx, item_id: int):
    item_id_str = str(item_id)
    item = db["market"].get(item_id_str)
    
    if not item:
        await ctx.send("Item not found.")
        return
    
    if item["owner"] != str(ctx.author.id):
        await ctx.send("You are not the owner of this item.")
        return
    
    del db["market"][item_id_str]
    save_db()
    await ctx.send(f"Market item '{item['name']}' removed successfully.")

@bot.command()
@commands.is_owner()
async def assign_role(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Assigned {role.name} to {user.name}.")

    save_db()

@bot.command()
@commands.is_owner()
async def remove_role(ctx, user: discord.Member, role: discord.Role):
    await user.remove_roles(role)
    await ctx.send(f"Removed {role.name} from {user.name}.")

    save_db()

@bot.command()
async def credit(ctx):
    try:
        user_id = ctx.author.id
        ensure_user_data(user_id)
        credits = get_user_credits(user_id)

        embed = discord.Embed(title="Credit Balance", color=0x00ff00)
        embed.add_field(name="Your Credits", value=f"You have {credits} credits.", inline=False)

        await ctx.send(embed=embed)

        save_db()

    except Exception as e:
        print(f"Error in !credit command: {e}")
        await ctx.send("An error occurred while retrieving your credits.")

@bot.command()
@commands.has_permissions(administrator=True)
async def addcredits(ctx, user: discord.Member, amount: int):
    if amount < 0:
        await ctx.send("Cannot add negative credits.")
        return

    user_id = user.id
    ensure_user_data(user_id)
    current_credits = get_user_credits(user_id)
    new_credits = current_credits + amount
    set_user_credits(user_id, new_credits)

    await ctx.send(f"Added {amount} credits to {user.mention}. They now have {new_credits} credits.")
    
    save_db()

@bot.command()
@commands.has_permissions(administrator=True)
async def removecredits(ctx, user: discord.Member, amount: int):
    if amount < 0:
        await ctx.send("Cannot remove negative credits.")
        return

    user_id = user.id
    ensure_user_data(user_id)
    current_credits = get_user_credits(user_id)

    if amount > current_credits:
        await ctx.send(f"{user.mention} does not have enough credits to remove {amount}. They currently have {current_credits} credits.")
        return

    new_credits = current_credits - amount
    set_user_credits(user_id, new_credits)

    await ctx.send(f"Removed {amount} credits from {user.mention}. They now have {new_credits} credits.")
    
    save_db()

@bot.command()
@commands.has_permissions(administrator=True)
async def setcredits(ctx, user: discord.Member, amount: int):
    if amount < 0:
        await ctx.send("Cannot set negative credits.")
        return

    user_id = user.id
    ensure_user_data(user_id)
    set_user_credits(user_id, amount)
    await ctx.send(f"Set {user.name}'s credits to {amount}.")

    save_db()

@bot.command()
@commands.has_permissions(administrator=True)
async def endsac(ctx):
    if not db.get("sac_active", False):
        await ctx.send("No sacrifice is currently active.")
        return

    db["custom_luck_multiplier"] = 1
    db["sac_amount"] = 0
    db["sac_active"] = False
    db["sac_spins"] = 0
    db["sac_limit_reached"] = False
    await ctx.send("Sacrifice ended.")

    save_db()

@bot.command()
@commands.has_permissions(administrator=True)
async def unsac(ctx):
    db["sac_active"] = False
    db["sac_amount"] = 0
    db["custom_luck_multiplier"] = 1
    db["sac_spins"] = 0
    db["sac_limit_reached"] = False
    await ctx.send("Sacrifice has been disabled.")
    save_db()

@bot.command()
@commands.has_permissions(administrator=True)
async def rig(ctx, rarity: int):
    if rarity < 1 or rarity >= len(rarityNames):
        await ctx.send("Invalid rarity level.")
        return

    user_id = ctx.author.id
    ensure_user_data(user_id)

    # Set rigged result
    db["rigged_result"] = rarity
    await ctx.send(f"Set rigged result to {rarityNames[rarity]}.")

    save_db()

@bot.command()
async def leaderboard(ctx):
    sorted_users = sorted(db["Social_credits"].items(), key=lambda x: x[1], reverse=True)
    top_users = sorted_users[:10]

    embed = discord.Embed(title="Leaderboard", color=0x00ff00)
    for i, (user_id, credits) in enumerate(top_users):
        member = ctx.guild.get_member(int(user_id))
        username = member.name if member else "Unknown User"
        embed.add_field(name=f"{i + 1}. {username}", value=f"{credits} credits", inline=False)

    await ctx.send(embed=embed)

    save_db()

@bot.command()
async def pay(ctx, user: discord.Member, amount: int):
    if amount <= 0:
        await ctx.send("Amount must be positive.")
        return

    sender_id = ctx.author.id
    recipient_id = user.id

    ensure_user_data(sender_id)
    ensure_user_data(recipient_id)

    sender_credits = get_user_credits(sender_id)
    if sender_credits < amount:
        await ctx.send("You don't have enough credits.")
        return

    tax = int(amount * 0.1)
    net_amount = amount - tax

    # Transfer credits
    set_user_credits(sender_id, sender_credits - amount)
    set_user_credits(recipient_id, get_user_credits(recipient_id) + net_amount)

    embed = discord.Embed(color=0xFFFF00)
    embed.add_field(name="Success!", value=f"{ctx.author.mention} has given {user.mention} {net_amount} credits! (after 10% tax of {tax})", inline=False)
    await ctx.send(embed=embed)

    save_db()

@bot.command()
async def sac(ctx, amount: int):
    if amount <= 0:
        await ctx.send("Amount must be positive.")
        return

    user_id = ctx.author.id
    ensure_user_data(user_id)

    if db.get("sac_active", False):
        await ctx.send("A sacrifice is already active.")
        return

    credits = get_user_credits(user_id)
    if credits < amount:
        await ctx.send("You don't have enough credits to sacrifice.")
        return

    tax = int(amount * 0.1)
    net_amount = amount - tax

    db["sac_amount"] = net_amount
    db["sac_active"] = True
    db["sac_spins"] = 0
    db["sac_limit_reached"] = False
    db["custom_luck_multiplier"] = round(max(0.207125 * (2.34915 * net_amount + 463.458) ** 0.5 - 4.48083, 1), 1)

    luck_multiplier = db["custom_luck_multiplier"]

    set_user_credits(user_id, credits - amount)
    embed = discord.Embed(color=0xFFFF00)
    embed.add_field(name="The Flowr gods heed your sacrifice...", value="\u200b", inline=False)
    embed.add_field(name=f"A {luck_multiplier}x luck boost has been activated!", value="\u200b", inline=False)
    embed.add_field(name="Sacrificed Social Credit", value=f"{net_amount} (after 10% tax of {tax})", inline=False)
    embed.add_field(name="Successful Sacrifice", value=f"{ctx.author.mention} sacrificed {amount} credits!", inline=False)

    await ctx.send(embed=embed)

    save_db()

@bot.command()
async def help1(ctx):
    embed = discord.Embed(title="Help", color=0x00ff00)
    embed.add_field(name="!spin", value="Spin the wheel to earn credits and receive a random rarity based on luck and mob type.", inline=False)
    embed.add_field(name="!credit", value="Check your current credit balance.", inline=False)
    embed.add_field(name="!addcredits <user> <amount>", value="Add credits to a user. Admins only.", inline=False)
    embed.add_field(name="!removecredits <user> <amount>", value="Remove credits from a user. Admins only.", inline=False)
    embed.add_field(name="!setcredits <user> <amount>", value="Set a user's credits to a specific amount. Admins only.", inline=False)
    embed.add_field(name="!endsac", value="End the current sacrifice. Admins only.", inline=False)
    embed.add_field(name="!unsac", value="Disable sacrifices. Admins only.", inline=False)
    embed.add_field(name="!assign_role <user> <role>", value="Assign a role to a user. Owner only.", inline=False)
    embed.add_field(name="!remove_role <user> <role>", value="Remove a role from a user. Owner only.", inline=False)
    embed.add_field(name="!rig <rarity>", value="Set a rigged spin result to a specific rarity. Admins only.", inline=False)
    embed.add_field(name="!pay <user> <amount>", value="Pay credits to another user with a 10% tax.", inline=False)
    embed.add_field(name="!sac <amount>", value="Sacrifice credits to increase your luck boost.", inline=False)
    embed.add_field(name="!leaderboard", value="Show the top 10 users based on credits.", inline=False)
    await ctx.send(embed=embed)

    save_db()

bot.run('your-bot-token')
