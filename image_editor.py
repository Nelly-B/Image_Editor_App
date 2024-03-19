from tkinter import ttk, Tk, PhotoImage, RIDGE, Canvas, GROOVE, Scale, HORIZONTAL, filedialog
import cv2
from PIL import Image, ImageTk

class Frontend():
    def __init__(self, master):
        self.master = master
        self.master.geometry('750x630+250+10')
        self.master.title('Image Editor App with Tkinter and Opencv')
        self.frame_hearder = ttk.Frame(self.master)
        self.frame_hearder.pack()

        self.logo = PhotoImage(file="python-logo-notext.svg.png").subsample(20, 20)
        ttk.Label(self.frame_hearder, image=self.logo).grid(row=0, column=0, rowspan=2)

        ttk.Label(self.frame_hearder, text="Welcome to the Image Editor App! ").grid(row=0, column=1)
        ttk.Label(self.frame_hearder, text="Upload, Edit and Save your images Easily!").grid(row=1, column=1)

        # ....................Menu start.........................................
        self.frame_menu = ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50, 15))

        # ttk.Label(self.frame_menu, text="Welcome to the Image Editor App!").grid(row=0, column=0)
        # ttk.Label(self.frame_menu, text="the Image Editor App! ").grid(row=0, column=0)
        # ttk.Label(self.frame_hearder, text="Upload, edit and save your images Easily!").grid(row=1, column=0)

        ttk.Button(self.frame_menu, text="Upload An Image", command=self.uplaod_action).grid(row=0, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Crop Image", command=self.crop_action).grid(row=1, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Add text", command=self.text_action1).grid(row=2, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Draw Over Image", command=self.draw_action).grid(row=3, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Apply Filter", command=self.filter_action).grid(row=4, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Blur/Smoothening", command=self.blur_action).grid(row=5, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(row=6, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Rotate", command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Flip", command=self.flip_action).grid(row=8, column=0, padx=5, pady=5, sticky="sw")

        ttk.Button(self.frame_menu, text="Save As", command=self.save_action).grid(row=9, column=0, padx=5, pady=5, sticky="sw")

    # .............................End of menu.................................

    # ...............................image canvas..........................   
        self.canvas = Canvas(self.frame_menu, bg="gray", width=300, height=400)
        self.canvas.grid(row=0, column=1, rowspan=10)
    # ................................End image canvas.......................
        
    # ..........................submenu....................................
    def refresh_side_frame(self):
        try:
            self.side_frame.grid_forget()
        except:
            pass
        # self.canvas.unbind("<ButtonPress>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease>")
        # self.display_image(self.edited_image)
        self.side_frame = ttk.Frame(self.frame_menu)
        self.side_frame.grid(row=0, column=2, rowspan=10)
        self.side_frame.config(relief=GROOVE, padding=(50, 15))

        # ttk.Label(self.side_frame, text="Upload an image").grid(row=0, column=0)


    # ..............................End submenu.............................

    # ..................................Footer start........................
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        self.apply = ttk.Button(self.apply_and_cancel, text="Apply", command=self.apply_action).grid(row=0, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(row=0, column=1, padx=5, pady=5, sticky='sw')

        ttk.Button(self.apply_and_cancel, text="Revert All Changes", command=self.revert_action).grid(row=0, column=2, padx=5, pady=5, sticky="sw")
        # ..........................Endof fotter.............................


    def uplaod_action(self):
        self.canvas.delete('all')
        self.filename = filedialog.askopenfilename()
        self.original_image = cv2.imread(self.filename)

        self.edited_image = cv2.imread(self.filename)
        self.filtered_image = cv2.imread(self.filename)
        self.display_image(self.edited_image)

    def crop_action(self):
        pass
    def text_action1(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text='Please enter a text').grid(row=0, column=0)

    def draw_action(self):
        pass

    def filter_action(self):
        self.refresh_side_frame()

        ttk.Button(self.side_frame, text="Negative", command=self.negative_action).grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Black and White", command=self.bw_action).grid(row=1, column=2, padx=5, pady=5,  sticky='sw')

        ttk.Button(self.side_frame, text="Stylisation", command=self.stylisation_action).grid(row=2, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Sketch Effect", command=self.sketch_action).grid(row=3, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Emboss", command=self.emb_action).grid(row=4, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Sepia", command=self.sepia_action).grid(row=5, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Binary Thresholding", command=self.binary_threshold_action).grid(row=6, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Erosion", command=self.erosion_action).grid(row=7, column=2, padx=5, pady=5, sticky='sw')

        ttk.Button(self.side_frame, text="Dilation", command=self.dilation_action).grid(row=8, column=2, padx=5, pady=5, sticky='sw')
        # .......................End of filter menu option......................
        

    def blur_action(self):
        self.refresh_side_frame()

        ttk.Label(self.side_frame, text="Averaging Blur").grid(row=0, column=2, padx=5, sticky='sw')

        self.average_slider = Scale(self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.averaging_action)
        self.average_slider.grid(row=1, column=2, padx=5, sticky='sw')

        ttk.Label(self.side_frame, text='Gaussian Blur').grid(row=2, column=2, padx=5, sticky='sw')

        self.gaussian_slider = Scale(self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.gaussian_action)
        self.gaussian_slider.grid(row=3, column=2, padx=5, sticky='sw')

        ttk.Label(self.side_frame, text='Median Blur').grid(row=4, column=2, padx=5, sticky='sw')

        self.median_slider = Scale(self.side_frame, from_=0, to=256, orient=HORIZONTAL, command=self.median_action)
        self.median_slider.grid(row=5, column=2, padx=5, sticky='sw')

        # ...........................End of blur menu option......................

    def adjust_action(self):
        self.refresh_side_frame()
        ttk.Label(self.side_frame, text="Brightness").grid(row=0, column=2, padx=5, pady=5, sticky='sw')

        self.brightness_slider = Scale(self.side_frame, from_=0, to=2, resolution=0.1, orient=HORIZONTAL, command=self.brightness_action)
        self.brightness_slider.grid(row=1, column=2, padx=5, sticky='sw')
        self.brightness_slider.set(1)

        ttk.Label(self.side_frame, text='Saturation').grid(row=2, column=2, padx=5, pady=5, sticky='sw')

        self.saturation_slider = Scale(self.side_frame, from_=-200, to=200, resolution=0.5, orient=HORIZONTAL, command=self.saturation_action )
        self.saturation_slider.grid(row=3, column=2, padx=5, sticky='sw')
        self.saturation_slider.set(0)

    def rotate_action(self):
        self.refresh_side_frame()
        ttk.Button(self.side_frame, text='Rotate Left', command=self.rotate_left_action).grid(row=0, column=2, padx=5, sticky='sw')

        ttk.Button(self.side_frame, text='Rotate Right', command=self.rotate_right_action).grid(row=1, column=2, padx=5, sticky='sw')
        # .........................End of rotate menu option...................

    def flip_action(self):
        self.refresh_side_frame()
        ttk.Button(self.side_frame, text="Vertical Flip", command=self.vertical_action).grid(row=0, column=2, padx=5, sticky='sw')

        ttk.Button(self.side_frame, text="Horizontal Flip", command=self.horizontal_action).grid(row=1, column=2, padx=5, sticky='sw')

        # ...............................End of flip menu option ................................

    def save_action(self):
        pass

    def apply_action(self):
        self.edited_image = self.filtered_image
        self.display_image(self.edited_image)
        
    def cancel_action(self):
        self.display_image(self.edited_image)

    def revert_action(self):
        self.edited_image = self.original_image.copy()
        self.display_image(self.original_image)



    def negative_action(self):
        pass

    def bw_action(self):
        pass

    def stylisation_action(self):
        pass

    def sketch_action(self):
        pass

    def emb_action(self):
        pass

    def sepia_action(self):
        pass

    def binary_threshold_action(self):
        pass

    def erosion_action(self):
        pass

    def dilation_action(self):
        pass



    def averaging_action(self):
        pass

    def gaussian_action(self):
        pass

    def median_action(self):
        pass

    def brightness_action(self):
        pass

    def saturation_action(self):
        pass

    def rotate_left_action(self):
        pass

    def rotate_right_action(self):
        pass

    def vertical_action(self):
        pass

    def horizontal_action(self):
        pass


    def display_image(self, image=None):
        self.canvas.delete("all")
        if image is None:
            image = self.edited_image.copy()
        else:
            image = image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
        height, width, channels = image.shape
        ratio = height/width

        new_width = width
        new_height = height

        if height>400 or width>300:
            if ratio < 1:
                new_width = 300
                new_height = int(new_width*ratio)
            else:
                new_height = 400
                new_width = int(new_height*(width/height))

        self.ratio = height/new_height
        self.new_image = cv2.resize(image, (new_width, new_height))

        self.new_image = ImageTk.PhotoImage(Image.fromarray(self.new_image))

        self.canvas.config(width=new_width, height=new_height)
        self.canvas.create_image(new_width/2, new_height/2, image=self.new_image) 
        


root = Tk()
Frontend(root)

root.mainloop()