import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@app_commands.command(name="ส่งของ", description="ส่งใบยืนยันคำสั่งซื้อสินค้า")
async def send_order(
    interaction: discord.Interaction,
    user: discord.Member,
    item: str,
    baht: str,
    amount: int = 1,
    channel: discord.TextChannel = None,
    image: discord.Attachment = None
):
    target_channel = channel or interaction.channel

    content_text = f"၄၃ {user.mention} <a:7319bunnycarrot:1556275397719498813>   Order submission complete."

    embed = discord.Embed(
        title="🍬. Order.     complete                        ♡",
        description=(
            f"<a:sl2:1534360785508372510> vortex\n\n"
            f"            <a:VL44:1556149117552693330> ผู้ซื้อสินค้า : {user.mention}\n"
            f"           <a:41672lovemail:1556150893643309088>   รายการ สินค้า<a:802491365723865116:1556148675909255199> {item}"
        ),
        color=discord.Color.from_rgb(46, 204, 113)
    )

    embed.add_field(
        name="<:205667glowingdotwhite:1556330625089413210> จำนวน",
        value=f"```  {amount}  ```",
        inline=False
    )

    embed.add_field(
        name="<:205667glowingdotwhite:1556330625089413210>  รวมทั้งหมด",
        value=f"```  {baht}  ```",
        inline=False
    )

    if image:
        embed.set_image(url=image.url)

    await target_channel.send(content=content_text, embed=embed)

    await interaction.response.send_message(
        f"✅ ส่งใบยืนยันไปยังช่อง {target_channel.mention} เรียบร้อยแล้ว!",
        ephemeral=True
    )

bot.run(os.getenv("DISCORD_TOKEN"))