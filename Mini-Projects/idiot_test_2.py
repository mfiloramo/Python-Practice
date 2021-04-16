from Modules import gen_answers

sex = gen_answers.confirm("Are you a male? ")
height = gen_answers.confirm("Are you tall? ")
intelligence = not(gen_answers.confirm("Are you a dumbass? "))

if sex:
    sex = "man"
else:
    sex = "woman"

if height:
    height = "tall"
else:
    height = "short"

if intelligence:
    intelligence = "smart"
else:
    intelligence = "dumbass"

print(f"You are a {sex}, who has a {height} height, and, cognitively, is pretty {intelligence}.")

#  Ctrl + L flushes lines across the entire file.
#  Ctrl + / hashes lines.
