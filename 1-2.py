from tkinter import Tk, Frame, Label, Entry, Button
import requests
def z2():
    s = requests.get('https://catfact.ninja/fact')
    o = s.json()
    return o['fact']
print("Факт о кошках:")
print(z2())
z2()
def z1():
    root = Tk()
    root['bg'] = '#fafafa'
    root.title('Прогноз погоды')
    root.geometry('600x450')
    root.resizable(width=False, height=False)
    def w():
        city = cityField.get()
        key = 'fc09d0d42a69bb902d64d8ac903a70d1'
        s = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        res = requests.get(s, params=params)
        t = res.json()
        info['text'] = f'{t['main']['t_m']}'

    frame = Frame(root, bg='cornflower blue', bd=4)
    frame.place(relx=0.15, rely=0.09, relwidth=0.7, relheight=0.7)

    title = Label(frame, text='Прогноз', bg='SteelBlue4', font=60)
    title.pack()

    frame_top = Frame(root, bg='#fafafa', bd=3)
    frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.4)

    frame_bottom = Frame(root, bg='#fafafa', bd=5)
    frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)

    cityField = Entry(frame_top, bg='steel blue', font=30)
    cityField.place(relx=0.15, rely=0.30, relwidth=0.7, relheight=0.2)

    btn = Button(frame_top, text='Узнать температуру', command=w)
    btn.place(relx=0.30, rely=0.55, relwidth=0.4, relheight=0.4)

    info = Label(frame_bottom, text='Максимальная температура', bg='#fafafa', font=40)
    info.pack()
    root.mainloop()
z1()

