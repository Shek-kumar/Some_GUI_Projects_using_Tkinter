import io
import webbrowser
import requests
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image

Country_code = None

class NewsApp:

    def __init__(self):
        # initial GUI load
        self.load_gui()
        self.root.mainloop()  # Call mainloop() here

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x650')
        self.root.resizable(0, 0)
        self.root.iconbitmap('icon.ico')
        self.root.title('News App')
        self.root.configure(background='black')


        # Adding the buttons for different country
        India = Button(self.root, text='Press for loading news article of India', fg='white', bg='#00a65a',
                       width=36, height=2, command=lambda: self.handle_country_name('in'))
        India.pack(pady=(5, 5))
        India.config(font=('verdana', 13))

        USA = Button(self.root, text='Press for loading news article of USA', fg='white', bg='#00a65a',
                     width=36, height=2, command=lambda: self.handle_country_name('us'))
        USA.pack(pady=(5, 5))
        USA.config(font=('verdana', 13))

        Canada = Button(self.root, text='Press for loading news article of Canada', fg='white', bg='#00a65a',
                        width=36, height=2, command=lambda: self.handle_country_name('ca'))
        Canada.pack(pady=(5, 5))
        Canada.config(font=('verdana', 13))

        China = Button(self.root, text='Press for loading news article of China', fg='white', bg='#00a65a',
                       width=36, height=2, command=lambda: self.handle_country_name('cn'))
        China.pack(pady=(5, 5))
        China.config(font=('verdana', 13))

        Ukraine = Button(self.root, text='Press for loading news article of Ukraine', fg='white', bg='#00a65a',
                         width=36, height=2, command=lambda: self.handle_country_name('ua'))
        Ukraine.pack(pady=(5, 5))
        Ukraine.config(font=('verdana', 13))

        Australia = Button(self.root, text='Press for loading news article of Australia', fg='white', bg='#00a65a',
                           width=36, height=2, command=lambda: self.handle_country_name('au'))
        Australia.pack(pady=(5, 5))
        Australia.config(font=('verdana', 12))


        Argentina = Button(self.root, text='Press for loading news article of Argentina', fg='white', bg='#00a65a',
                       width=36, height=2, command=lambda: self.handle_country_name('ar'))
        Argentina.pack(pady=(5, 5))
        Argentina.config(font=('verdana', 12))


        Poland = Button(self.root, text='Press for loading news article of Poland', fg='white', bg='#00a65a',
                     width=36, height=2, command=lambda: self.handle_country_name('pl'))
        Poland.pack(pady=(5, 5))
        Poland.config(font=('verdana', 13))

        Romania = Button(self.root, text='Press for loading news article of Romania', fg='white', bg='#00a65a',
                        width=36, height=2, command=lambda: self.handle_country_name('ro'))
        Romania.pack(pady=(5, 5))
        Romania.config(font=('verdana', 12))

        Russia = Button(self.root, text='Press for loading news article of Russia', fg='white', bg='#00a65a',
                       width=36, height=2, command=lambda: self.handle_country_name('ru'))
        Russia.pack(pady=(5, 5))
        Russia.config(font=('verdana', 13))

    def handle_country_name(self, code):
        global Country_code
        Country_code = code
        self.fetch_news_data()  # Fetch new data based on selected country

    def fetch_news_data(self):
        # fetch the news articles for the given country code
        try:
            response = requests.get(
                f'https://newsapi.org/v2/top-headlines?country={Country_code}&apiKey=07ce6431517e45c5b04b589c36e5bed6'
            )
            response.raise_for_status()
            self.data = response.json()
            self.load_news_item(0)  # Load the first news item
        except requests.RequestException as e:
            print(f"Error fetching news: {e}")

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
        # clear the screen for the new news item
        self.clear()


        # for a country news articles loading the author details at top
        author_text = self.data['articles'][index]['author']
        # Combine author and source into one string
        label_text = f"Source: {author_text} "
        Author = Label(self.root, text=label_text, fg='orange', bg='black', wraplength=350, justify='center')
        Author.pack(pady=(10, 10))
        Author.config(font=('verdana', 15))

        # Loading the time and date of the published news article
        Time_Date = Label(self.root, text=self.data['articles'][index]['publishedAt'], bg='black', fg='blue',
                          wraplength=350, justify='center')
        Time_Date.pack(pady=(5, 10))
        Time_Date.config(font=('verdana', 15))

        # image
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://media.gettyimages.com/id/1318698827/vector/breaking-news.jpg?s=2048x2048&w=gi&k=20&c=uaLCWps3hPTgEyca016pP505tOda7QxwkI04XWgzIL4='
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        # creating a label for the image
        label = Label(self.root, image=photo)
        label.image = photo  # keep a reference to avoid garbage collection
        label.pack()

        # creating a label for the heading of the news article
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white',
                        wraplength=350, justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        # creating a label for the description of the news article
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        # creating a frame in order to load three functionality buttons
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        # adding a prev button which will lead to previous news article if present
        if index != 0:
            prev = Button(frame, text='Prev', fg='white', bg='#00a65a', width=16, height=3,
                          command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        # adding a read button in order to read the whole news article on the web
        read = Button(frame, text='Read More', fg='white', bg='#00a65a', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        # adding a next button to move to the next news article if available
        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', fg='white', bg='#00a65a', width=16, height=3,
                          command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

    # defining a function in order to load the full news article
    def open_link(self, url):
        webbrowser.open(url)


if __name__ == '__main__':
    NewsApp()
