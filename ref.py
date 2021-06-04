from discord.ext import commands
import random
import os

TOKEN = os.environ['PUB_REF_TOKEN']

bot = commands.Bot(command_prefix='$')


@bot.command(name='avatar')
async def avatar(ctx: commands.Context):
    base = 'Profile Pictures:\n{}\n{}'
    mentioned_lines = [f'\t{person.name} ({person.nick}) - <{person.avatar_url}>' for person in ctx.message.mentions]
    mentioned_portion = '\n'.join(mentioned_lines)
    mentioned_role_portions_list = []
    for mentioned_role in ctx.message.role_mentions:
        mentioned_role_lines = []
        mentioned_role_portion = '\t{}:\n{}'
        for user in mentioned_role.members:
            mentioned_role_lines.append(f'\t\t{user.name} ({user.nick}) - <{user.avatar_url}>')
        mentioned_role_portions_list.append(mentioned_role_portion.format(mentioned_role.name, '\n'.join(mentioned_role_lines)))
    mentioned_roles_portion = '\n'.join(mentioned_role_portions_list)
    fin = base.format(mentioned_portion, mentioned_roles_portion)
    await ctx.send(fin)


@bot.command(name='flip')
async def flip(ctx: commands.Context, *args):
    if args:
        base = 'Drafting Order:\n{}'
        pool = []
        for member in ctx.message.mentions:
            pool.append(member)
        random.shuffle(pool)
        lines = []
        for i, member in enumerate(pool):
            lines.append(f'\t{i+1}. {member.name} ({member.nick})')
        await ctx.send(base.format('\n'.join(lines)))
    else:
        await ctx.send(random.choice(['Heads', 'Tails']))


if __name__ == '__main__':
    bot.run(TOKEN)

