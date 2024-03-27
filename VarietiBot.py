#replace YOURCHANNELID with the channel you want annoucements in
#replace YOURBOTSTOKEN with your bots token
#replace OWNERSUSERID with the owners user id
#replace OWNERSROLEID with the owners role id
import discord
from discord.ext import commands

bvar = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@bvar.event
async def on_ready():
    await bvar.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="VARIETI"))

@bvar.event
async def on_member_join(member):
    channel = bvar.get_channel(YOURCHANNELID)
    embed = discord.Embed(
        title=f"VARIETI",
        description=f"Welcome to VARIETI! Check out our bug bounties and stay active {member.mention}",
        color=discord.Color.random()
    )
    
    embed.set_footer(text="https://discord.gg/28mFzDeG6U")
    await channel.send(embed=embed)
    
    try:
        await member.send("Welcome to VARIETI! Make sure to be active, boost and participate in giveaways for rewards and special roles")
    except discord.Forbidden:
        pass


@bvar.command()
async def dropad(ctx):
    user_id = OWNERSUSERID
    role_id = OWNERSROLEID
    
    if ctx.author.id == user_id:
        role = ctx.guild.get_role(role_id)
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} granted 0")
    else:
        await ctx.send("You are not the owner")

bvar.run("YOURBOTSTOKEN")
