# Wedding Reply Cards with Passcodes
Take a .csv list of passcodes and create individual images for each, to be physically printed on a set of reply cards.

## Setup
Add .csv file in the top directory named "passcodes.csv" with each passcode on a new line

Add base image file in the top directory named "reply_card.png" to test out the passcode positioning

## Configuration
### Image Size
Edit variable values `BASE_WIDTH` and `BASE_HEIGHT`

### Passcode Position
Edit variable values `HORIZONTAL_POSITION` and `VERTICAL_POSITION`

### Font
Add .ttf file

Edit variable value `FONT_FILENAME` to the new font file path

### Text Color
Edit variable value `COLOR_TEXT`

## Usage
### Create image files for each passcode in csv file:
    python write_passcodes.py

Make sure you have a .csv file in the top directory named "passcodes.csv" with each passcode on a new line

Writes to files called "passcode_cards/<number>_<passcode>.png"

### Create image files for one passcode in csv file:
    python write_passcodes.py print <number>

where `<number>` is the 1-indexed passcode multiplied by ten (e.g. to print the 7th passcode in the list, `<number>` would be `70`)

Make sure you have a .csv file in the top directory named "passcodes.csv" with each passcode on a new line

Writes to file called "passcode_cards/<number>_<passcode>.png"

### Create test images with the passcode overlaid onto another image:
    python write_passcodes.py test <number>

where `<number>` is the 1-indexed passcode multiplied by ten (e.g. to print the 7th passcode in the list, `<number>` would be `70`)

Make sure you have a base image file in the top directory named "reply_card.png"

### Create image file for given passcode:
    python write_passcodes.py fake <passcode>

Writes to file called "fake_<passcode>.png"

### Create test image with the given passcode overlaid onto another image:
    python write_passcodes.py faketest <passcode>

Make sure you have a base image file in the top directory named "reply_card.png"

Writes to file called "faketest_<passcode>.png"
