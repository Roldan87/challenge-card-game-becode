import typing # COACHES' NOTES: Don't import stuff you don't use in the current file
from utils.game import Board
from utils.card import Card, Symbol # COACHES' NOTES: Don't import stuff you don't use in the current file
from utils.player import Player, Deck # COACHES' NOTES: Don't import stuff you don't use in the current file


new_game = Board()
new_game.start_game()


# COACHES' NOTES: Use a .gitignore file to ignore files and folders such as __pycache__
# https://www.freecodecamp.org/news/gitignore-what-is-it-and-how-to-add-to-repo/

# COACHES' NOTES:
# - You understand the general concept of OOP well. Some little details to polish
# it, but it's good. Your code generates an error when I run it, but it looks good,
# just need to debug that small little problem.
# Overall, I am very happy with the code. GOOD JOB!
