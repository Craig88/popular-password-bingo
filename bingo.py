from pygame import display
import pgzrun
import random

WIDTH = 800
HEIGHT = 600
BG_COLOR = (54, 57, 92)
TEXT_COLOR = "white"
FONT = "open-sans"
WORDS_FILE = "words.txt"


def get_words():
    list_words = []

    with open(WORDS_FILE) as file:
        for line in file:
            line = line.rstrip('\n')
            list_words.append(line)

    return list_words


def get_random_word(w):
    global current_word
    global used_words

    if not words:  # if remaining words is empty
        screen.clear()
        current_word = "Finished!"
        print("Finished")
        return

    chosen_word = random.choice(w)
    used_words.append(chosen_word)
    words.remove(chosen_word)

    screen.clear()
    current_word = chosen_word
    print(current_word)


def on_mouse_down():
    get_random_word(words)


def on_key_up(key):
    if key == keys.SPACE:
        print("Words used so far: ")
        print(used_words)


def draw():
    display.set_caption("Bingo App")
    w, h = screen.surface.get_width(), screen.surface.get_height()
    main_box = Rect(0, 0, w, h)
    screen.fill(BG_COLOR)
    screen.draw.textbox(current_word, main_box,
                        color=TEXT_COLOR, fontname=FONT)


words = get_words()
used_words = []
current_word = "Password Bingo"


pgzrun.go()
