version = "1.0.0"

print("By using this bot you agree to the terms and conditions of the bot's creator found here: https://notdabenjamin.neocities.org/98karrots/terms")
con = input("Continue w/ logs? (y/n): ")
if con.lower() == "y":
    exec(open("log.py").read())
elif con.lower() == "n":
    exec(open("nlog.py").read())
else:
    print("Invalid input. Exiting...")