from __future__ import annotations


import discord
from discord.ext import commands
from discord import app_commands, Embed
from datetime import datetime, timedelta
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from setup import BaseBot
    

class Test(commands.Cog):
    def __init__(self, bot: BaseBot) -> None:
        self.bot: BaseBot = bot
    
    @commands.command(description="Test me...")
    async def test(self, ctx: commands.Context) -> None:
        """This is an test command."""
        await ctx.reply(f"Hello! there...")

    @commands.command(description="Insert dummy data for a user")
    async def insert_data(
                        self, 
                        ctx: commands.Context, 
                        email: str | None = "test@gmail.com", 
                        password: str| None = "test") -> None:
        
        """Insert dummy data for a user."""

        query = "INSERT INTO users (user_id, username, email, password) VALUES (?, ?, ?, ?)"
        values = (ctx.author.id, ctx.author.display_name, email, password)
        try:
            async with ctx.bot.db.connection.execute(query, values) as cursor:
                await ctx.bot.db.connection.commit()
            await ctx.send("Data inserted successfully!")
        except Exception as e:
            await ctx.send(f"Failed to insert data. Error: {e}")
            

async def setup(bot: BaseBot):
    await bot.add_cog(Test(bot))