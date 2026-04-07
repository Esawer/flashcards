import hashlib
import io
import os
from django.conf import settings
import random
from random import randint
from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont, ImageChops, ImageFilter


def generate_strings():
    """
    Generates random strings and saves them to the `str_combinations` dictionary.
    The function filters out characters that are hard for humans to read or easily confused (e.g., -, _, 1, ~, I, l, ), ().
    If a chosen character is easy to read and not already in the string, it is added; otherwise, the process repeats.
    Each string is composed of 5 to 8 characters.

    :param IMG_NUMBER: The total number of strings to generate.

    ##############################
    I used AI for the random module, as well as for general syntax.
    ##############################
    """

    str_combination = ""

    n = random.randrange(5, 9)  # Randomized string length.
    comb = ""  # Temporary string placeholder.

    for _ in range(n):
        while True:
            character = random.randint(
                35, 123
            )  # If the chosen character is not in the excluded list and not already in the string, it is added.
            if (
                chr(character)
                not in (
                    "-",
                    "_",
                    "1",
                    "~",
                    "`",
                    "!",
                    "I",
                    "l",
                    "0",
                    "O",
                    '"',
                    "'",
                    "}",
                    "{",
                    "(",
                    ")",
                    ";",
                    ":",
                    "/",
                    "\\",
                    ",",
                    ".",
                    "[",
                    "]",
                    "i",
                    "t",
                    "&",
                    "=",
                    "+",
                    ">",
                    "<",
                    "j",
                    "o",
                )
                and chr(character) not in comb
            ):
                comb += chr(character)
                break

    str_combination = comb

    return str_combination


def encrypt_string(str_combination: str):
    return hashlib.sha512(str_combination.strip("\n").strip(" ").encode()).hexdigest()


def create_images(str_combination: str):
    """
    First, strings are stripped of their indices, leaving bare strings
    that are then used for image generation.
    Afterwards, the images are generated using Pillow (PIL).

    :param IMG_NUMBER: The number of images to generate.
    ##############################
    I used AI for the Pillow library work (as I had never used it before).
    ##############################
    """

    font_dir = os.path.join(settings.BASE_DIR, "application", "utils")

    fonts = [
        os.path.join(font_dir, "ARIALBD.TTF"),
        os.path.join(font_dir, "ARIALBI.TTF"),
    ]

    reverse_colors = (
        False  # Boolean; determines the color of both the text and the background.
    )
    color = ["white", "black"]  # Colors of text and background.

    reverse_colors = bool(random.randint(0, 2))
    color = sorted(color, reverse=reverse_colors)

    code = str_combination
    text = "".join((code[i] + (random.randint(0, 3) * " ")) for i in range(len(code)))
    # Text generation with a random number of spaces between characters.

    im_width = 350  # Image width.
    im_height = 75  # Image height.
    img = Image.new(
        "L", (im_width, im_height), color[0]
    )  # Image object of the corresponding size, color, and mode ('L' mode is monochrome).
    draw = ImageDraw.Draw(img)

    current_x = 10  # First character starting position.
    for j in range(len(text)):
        ft = ImageFont.truetype(
            fonts[(random.randint(0, 1))],
            random.randint(35, 40),
        )
        # Font type and size are randomized.
        draw.text((current_x, random.randint(5, 18)), text[j], fill=color[1], font=ft)
        # The character is drawn with a randomized Y position.
        current_x += draw.textlength(text[j], ft)

    for _ in range(random.randint(3, 7)):  # A random number of lines is generated.
        draw.line(
            (
                random.uniform(0, im_width),
                random.uniform(0, im_height),
                random.uniform(0, im_width),
                random.uniform(0, im_height),
            ),
            fill=color[1],
            width=random.randrange(3, 5),
        )
        # The start and end points of the line are randomized.

    for _ in range(randint(5000, 7000)):  # Points / grain effect.
        draw.point(
            ((random.randint(0, im_width)), (random.randint(0, im_height))),
            fill=color[1],
        )

    noise = Image.effect_noise(
        (350, 75), random.randrange(30, 45)
    )  # Noise effect with randomized strength.

    img = ImageChops.add(img, noise)  # The noise effect is added.
    img = img.filter(
        ImageFilter.GaussianBlur(radius=random.uniform(1, 1.5))
    )  # Gaussian blur.

    buffor = io.BytesIO()
    img.save(buffor, format="JPEG", optimized=True)  # The image is saved.

    return HttpResponse(buffor.getvalue(), content_type="image/jpeg")
