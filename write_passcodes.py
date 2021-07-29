from PIL import Image, ImageColor, ImageDraw, ImageFont
import csv
import sys


# CONFIGURATION
FONT_FILENAME = "RobotoMono-Regular.ttf"
BASE_FONTSIZE = 25
BASE_WIDTH = 674
BASE_HEIGHT = 484
COLOR_TEXT = ImageColor.getrgb('#000000')
HORIZONTAL_POSITION = 1/2 # portion of the width from the left
VERTICAL_POSITION = 4/7 # portion of the height from the top
ROTATE_ANGLE = 270 # degrees to rotate image, 0 for no rotation


# CONSTANTS
PASSCODES_FILENAME = "passcodes.csv"
COLOR_TRANSPARENT = ImageColor.getrgb('#00000000')


# PRINT PASSCODE ON IMAGE
def print_passcode(passcode, image, out_filename):
  draw = ImageDraw.Draw(image)
  width, height = image.size
  text_width, text_height = draw.textsize(passcode, font)
  position = ((width-text_width)*HORIZONTAL_POSITION,
              (height-text_height)*VERTICAL_POSITION)
  draw.text(position, passcode, COLOR_TEXT, font=font)

  image = image.rotate(ROTATE_ANGLE, expand=True)
  if len(sys.argv) > 2:
    image.show()
  image.save(out_filename, "PNG")


# TEST PASSCODE ON BASE IMAGE
if len(sys.argv) > 2 and sys.argv[1] == "test":
  font = ImageFont.truetype(FONT_FILENAME, BASE_FONTSIZE)
  test_num = int(sys.argv[2])

  base_image_filename = "reply_card.png"
  with Image.open(base_image_filename) as base_image:

    with open(PASSCODES_FILENAME, 'r') as passcodes_file:
      passcodes_reader = csv.reader(passcodes_file)

      count = 0
      for passcode_row in passcodes_reader:
        passcode = passcode_row[0]
        count += 1
        if count*10 == test_num:
          passcode_image = base_image.copy()
          passcode_card_filename = f"test_{count*10:03d}.png"
          print_passcode(passcode, passcode_image, passcode_card_filename)


# TEST GIVEN PASSCODE ON BASE IMAGE
elif len(sys.argv) > 2 and sys.argv[1] == "faketest":
  passcode = sys.argv[2]
  passcode_card_filename = f"faketest_{passcode}.png"

  font = ImageFont.truetype(FONT_FILENAME, BASE_FONTSIZE)

  base_image_filename = "reply_card.png"
  with Image.open(base_image_filename) as base_image:
    passcode_image = base_image.copy()
    print_passcode(passcode, passcode_image, passcode_card_filename)


# PRINT GIVEN PASSCODE
elif len(sys.argv) > 2 and sys.argv[1] == "fake":
  passcode = sys.argv[2]
  passcode_card_filename = f"fake_{passcode}.png"

  multiplier = 3
  size = (BASE_WIDTH*multiplier, BASE_HEIGHT*multiplier)
  font = ImageFont.truetype(FONT_FILENAME, BASE_FONTSIZE*multiplier)

  passcode_image = Image.new('RGBA', size, COLOR_TRANSPARENT)
  print_passcode(passcode, passcode_image, passcode_card_filename)

# print passcodes
else:
  multiplier = 3
  size = (BASE_WIDTH*multiplier, BASE_HEIGHT*multiplier)
  font = ImageFont.truetype(FONT_FILENAME, BASE_FONTSIZE*multiplier)
  print_num = int(sys.argv[2]) \
      if len(sys.argv) > 2 and sys.argv[1] == "print" \
      else None

  with open(PASSCODES_FILENAME, 'r') as passcodes_file:
    passcodes_reader = csv.reader(passcodes_file)

    count = 0
    for passcode_row in passcodes_reader:
      passcode = passcode_row[0]
      count += 1
      if not print_num or count*10 == print_num:
        passcode_image = Image.new('RGBA', size, COLOR_TRANSPARENT)
        passcode_card_filename = f"passcode_cards/{count*10:03d}_{passcode}.png"
        print_passcode(passcode, passcode_image, passcode_card_filename)
