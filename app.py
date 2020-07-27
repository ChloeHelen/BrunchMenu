import os
import random
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

# Constants
WINDOW_TITLE = 'Brunch Me Up!'
WINDOW_WIDTH = 220
WINDOW_HEIGHT = 650
IMG_HEIGHT = 160
IMG_WIDTH = 200
BACKGROUND_COLOUR = '#ffd1dc'
MAINS = [str("mains/") + file for file in os.listdir("mains/") if not file.startswith('.')]
PASTRIES = [str("pastries/") + file for file in os.listdir("pastries/") if not file.startswith('.')]
DRINKS = [str("drinks/") + file for file in os.listdir("drinks/") if not file.startswith('.')]

class App:

    def __init__(self, root):
        self.root = root

        self.mains_images = MAINS
        self.pastries_images = PASTRIES
        self.drinks_images = DRINKS

        self.main_image_path = self.mains_images[0]
        self.pastry_image_path = self.pastries_images[0]
        self.drink_image_path = self.drinks_images[0]

        # Create Frames
        self.brunch_me_up_frame = tk.Frame(self.root, bg=BACKGROUND_COLOUR)        
        self.main_frame = tk.Frame(self.root, bg=BACKGROUND_COLOUR)
        self.pastry_frame = tk.Frame(self.root, bg=BACKGROUND_COLOUR)
        self.drink_frame = tk.Frame(self.root, bg=BACKGROUND_COLOUR)     
        
        # add main
        self.main_image_label = self.get_image(self.main_image_path, self.main_frame)
        self.main_image_label.pack(side=tk.TOP)

        # add pastry
        self.pastry_image_label = self.get_image(self.pastry_image_path, self.pastry_frame)
        self.pastry_image_label.pack(side=tk.TOP)

        # add drink
        self.drink_image_label = self.get_image(self.drink_image_path, self.drink_frame)
        self.drink_image_label.pack(side=tk.TOP)

        self.create_background()

    def create_background(self):
        self.root.title(WINDOW_TITLE)
        self.root.geometry('{0}x{1}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))

        self.create_buttons()

        # add initial selection
        self.brunch_me_up_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.main_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.pastry_frame.pack(fill=tk.BOTH, expand=tk.YES)
        self.drink_frame.pack(fill=tk.BOTH, expand=tk.YES)
        

    def create_buttons(self):
        create_menu_button = tk.Button(self.brunch_me_up_frame, text="Brunch Me Up!", command=self.create_menu, relief=FLAT)
        create_menu_button.pack(side=tk.BOTTOM)

        main_prev_button = tk.Button(self.main_frame, text="No, go back!", command=self.get_prev_main, relief=FLAT)
        main_prev_button.pack(side=tk.LEFT)

        main_next_button = tk.Button(self.main_frame, text="Something else...", command=self.get_next_main, relief=FLAT)
        main_next_button.pack(side=tk.RIGHT)

        pastry_prev_button = tk.Button(self.pastry_frame, text="No, go back!", command=self.get_prev_pastry, relief=FLAT)
        pastry_prev_button.pack(side=tk.LEFT)

        pastry_next_button = tk.Button(self.pastry_frame, text="Something else...", command=self.get_next_pastry, relief=FLAT)
        pastry_next_button.pack(side=tk.RIGHT)

        drink_prev_button = tk.Button(self.drink_frame, text="No, go back!", command=self.get_prev_drink, relief=FLAT)
        drink_prev_button.pack(side=tk.LEFT)

        drink_next_button = tk.Button(self.drink_frame, text="Something else...", command=self.get_next_drink, relief=FLAT)
        drink_next_button.pack(side=tk.RIGHT)


    def get_image(self, image, frame):
        top_image_file = Image.open(image)
        image = top_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = tk.Label(frame, image=photo, anchor=tk.CENTER)
        image_label.image = photo

        return image_label

    def update_image(self, new_image, image_label):
        new_image_file = Image.open(new_image)
        image = new_image_file.resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

    def _get_next_item(self, current_item, category, increment=True):
        item_index = category.index(current_item)
        final_index = len(category) - 1
        next_index = 0

        if increment and item_index == final_index:
            next_index = 0 
        elif not increment and item_index == 0:
            next_index = final_index 
        else:
            incrementor = 1 if increment else -1
            next_index = item_index + incrementor

        next_image = category[next_index]

        # reset the image object
        if current_item in self.mains_images:
            image_label = self.main_image_label
            self.main_image_path = next_image
        elif current_item in self.pastries_images:
            image_label = self.pastry_image_label
            self.pastry_image_path = next_image
        else:
            image_label = self.drink_image_label
            self.drink_image_path = next_image

        # update the image
        self.update_image(next_image, image_label)

    def get_next_main(self):
        self._get_next_item(self.main_image_path, self.mains_images, increment=True)

    def get_prev_main(self):
        self._get_next_item(self.main_image_path, self.mains_images, increment=False)

    def get_prev_pastry(self):
        self._get_next_item(self.pastry_image_path, self.pastries_images, increment=False)

    def get_next_pastry(self):
        self._get_next_item(self.pastry_image_path, self.pastries_images, increment=True)

    def get_prev_drink(self):
        self._get_next_item(self.drink_image_path, self.drinks_images, increment=False)

    def get_next_drink(self):
        self._get_next_item(self.drink_image_path, self.drinks_images, increment=True)

    def create_menu(self):
        new_main_index = random.randint(0, len(self.mains_images)-1)
        new_pastry_index = random.randint(0, len(self.pastries_images)-1)
        new_drink_index = random.randint(0, len(self.drinks_images)-1)

        self.update_image(self.mains_images[new_main_index], self.main_image_label)
        self.update_image(self.pastries_images[new_pastry_index], self.pastry_image_label)
        self.update_image(self.drinks_images[new_drink_index], self.drink_image_label)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)

    root.mainloop()
