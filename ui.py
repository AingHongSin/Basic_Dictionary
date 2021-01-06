from tkinter import *
from tkinter import messagebox
from data import DictionaryBackEnd

BACKGROUND = '#ffe6e6'
FONT = ('Hoefler Text', 28, 'bold')


class DictionaryFrontEnd(Tk):

    def __init__(self, data: DictionaryBackEnd):
        super().__init__()

        self.data = data

        self.title('Dictionary')

        self.config(background = BACKGROUND)

        self.title = PhotoImage(file = './Resourcese/Title.png')
        self.English_Title = PhotoImage(file = './Resourcese/English_title.png')
        self.Khmer_Title = PhotoImage(file = './Resourcese/Khmer_title.png')
        self.switch_off = PhotoImage(file = './Resourcese/switch_off.png')
        self.switch_on = PhotoImage(file = './Resourcese/switch_on.png')
        self.word_background = PhotoImage(file = './Resourcese/Word_background.png')
        self.Go = PhotoImage(file = './Resourcese/Go.png')

        self.Title_canvas = Canvas(width = 326, height = 85, bg = BACKGROUND, highlightthickness = 0)
        self.Title = self.Title_canvas.create_image(163,42, image = self.title)
        self.Title_canvas.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)

        self.right_Title_canvas = Canvas(width = 326, height = 85, bg = BACKGROUND, highlightthickness = 0)
        self.right_title = self.right_Title_canvas.create_image(163,42, image = self.English_Title)
        self.right_Title_canvas.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.Switch_button = Button(width = 110, height = 85, image = self.switch_off
                                    , bg = BACKGROUND, highlightthickness = 0,
                                    command = self.off_switching)
        self.Switch_button.grid(row = 1, column = 1, padx = 10, pady = 20)

        self.Go_button = Button(width = 110, height = 85, image = self.Go
                                    , bg = BACKGROUND, highlightthickness = 0, command = self.translating)
        self.Go_button.grid(row = 2, column = 1)

        self.left_Title_canvas = Canvas(width = 326, height = 85, bg = BACKGROUND, highlightthickness = 0)
        self.left_title = self.left_Title_canvas.create_image(163,42, image = self.Khmer_Title)
        self.left_Title_canvas.grid(row = 1, column = 2, padx = 10, pady = 10)

        self.right_Background_canvas = Canvas(width = 326, height = 145, bg = BACKGROUND, highlightthickness = 0)
        self.right = self.right_Background_canvas.create_image(163,72, image = self.word_background)
        self.right_text = self.right_Background_canvas.create_text(160, 65, text = '', font = FONT, fill = '#FFABE1')
        self.right_Background_canvas.grid(row = 2, column = 2, padx = 10, pady = 10)

        self.left_Background_canvas = Canvas(width = 326, height = 145, bg = BACKGROUND, highlightthickness = 0)
        self.left = self.left_Background_canvas.create_image(163,72, image = self.word_background)
        self.left_Background_canvas.grid(row = 2, column = 0, padx = 10, pady = 10)

        # self.input_word = Text(bg = 'white', width = 10, height = 2, highlightthickness = 0, font = FONT)
        # self.input_word.place(x = 67, y = 281)

        self.input_word = Entry(bg = '#A685E2',
                                highlightthickness = 0,
                                relief = 'flat',
                                width = 14,
                                font = FONT,
                                justify = 'center',
                                fg = '#FFABE1')
        self.input_word.focus()
        self.input_word.place(x = 44, y = 308)


        self.mainloop()

    def off_switching(self):
        self.Switch_button.config(image = self.switch_on, command = self.on_switching)
        self.right_Title_canvas.itemconfig(self.right_title, image = self.Khmer_Title)
        self.left_Title_canvas.itemconfig(self.left_title, image=self.English_Title)

    def on_switching(self):
        self.Switch_button.config(image = self.switch_off, command = self.off_switching)
        self.right_Title_canvas.itemconfig(self.right_title, image = self.English_Title)
        self.left_Title_canvas.itemconfig(self.left_title, image = self.Khmer_Title)

    def translating(self):
        input_word = str(self.input_word.get()).lower()
        if input_word == '':
            messagebox.showinfo(title = 'Oops', message = "Please Enter Something.")
            self.right_Background_canvas.itemconfig(self.right_text, text = None)
        else:
            output = self.data.finding_word(word=input_word)
            if output == []:
                messagebox.showinfo(title='Oops', message=f"Sorry this word {input_word}, didn't exist.")
            else:
                self.right_Background_canvas.itemconfig(self.right_text, text = output)
