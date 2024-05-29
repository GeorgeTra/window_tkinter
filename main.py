from tkinter import Tk, Frame, GROOVE, RAISED, Label, StringVar, Radiobutton, \
    Checkbutton, Scale, HORIZONTAL, Listbox, SINGLE, END, Button


# Функция для определения характеристик шрифта
def getFont():
    res = []
    name = lst.get(lst.curselection())
    size = scl.get()
    res.append(name)
    res.append(size)
    if bold.get() != "":
        res.append(bold.get())
    if italic.get() != "":
        res.append(italic.get())
    return res


# Функция для применения характеристик шрифта
def setAll(*args):
    fnt = getFont()
    lbl.configure(font=fnt)
    lbl.configure(fg=color.get())
    txt = "\nШрифт "
    txt += fnt[0]
    txt += " размера "+str(fnt[1]) + "\n"
    if "bold" in fnt:
        txt += " жирный"
    if "italic" in fnt:
        txt += " курсивный"
    if color.get() == "red":
        txt += " красного"
    elif color.get() == "blue":
        txt += " синего"
    else:
        txt += " черного"
    txt += " цвета\n"
    text.set(txt)


# Списки с характеристиками шрифтов
fnt_1 = ["Arial", 12, "italic"]
fnt_2 = ["Times New Roman", 13, "bold", "italic"]

# Список названий шрифтов для статического списка
fonts = ["Times New Roman", "Arial", "Courier New"]

# Мин. и макс. размеры шрифта
min_size = 15
max_size = 21

# Ширина и высота окна
w = 640
h = 420

# Высота панели с шаблонным текстом
hf = 140

# Ширина и высота панели со статическим списком
wl = w / 3
hl = h - hf - 15

# Высота панели с кнопкой
hb = 60

# Ширина и высота панели со слайдером и переключателями
ws = w - wl - 15
hs = hl - hb - 5

# Создание главного окна
wnd = Tk()
wnd.title("Параметры шрифта")
wnd.geometry(str(w) + "x" + str(h))
wnd.resizable(False, False)

# Создание панелей
frm_scale = Frame(wnd, bd=3, relief=GROOVE)
frm_text = Frame(wnd, bd=3, relief=GROOVE)
frm_button = Frame(wnd, bd=3, relief=GROOVE)
frm_list = Frame(wnd, bd=3, relief=GROOVE)
frm_check = Frame(frm_list, bd=3, relief=GROOVE)

# Переменные для определения текстового содержимого
# в элементах управления
text = StringVar()
color = StringVar()
bold = StringVar()
italic = StringVar()

# Создание текстовых меток
lbl_text = Label(frm_text, text="Пример текста:", font=fnt_2)
lbl_color = Label(frm_scale, text="Цвет текста:", font=fnt_2)
lbl_size = Label(frm_scale, text="Размер текста:", font=fnt_2)
lbl_font = Label(frm_list, text="Название шрифта:", font=fnt_2)
lbl_style = Label(frm_check, text="Стиль шрифта:", font=fnt_2)

# Метка для отображения шаблонного текста
lbl = Label(frm_text, textvariable=text)
# Фон и рамка для метки
lbl.configure(bg="white", relief=RAISED)

# Переключатели
rb_1 = Radiobutton(frm_scale, text="красный", variable=color)
rb_1.configure(value="red", font=fnt_1)
rb_2 = Radiobutton(frm_scale, text="синий", variable=color)
rb_2.configure(value="blue", font=fnt_1)
rb_3 = Radiobutton(frm_scale, text="черный", variable=color)
rb_3.configure(value="black", font=fnt_1)
# Устанавливается переключатель
color.set("blue")

# Создание слайдера
scl = Scale(frm_scale, orient=HORIZONTAL)
# Диапазон изменения значений
scl.configure(from_=min_size, to=max_size)
# Интервал для отображения подписей и шаг дискретности
# для ползунка
scl.configure(tickinterval=1, resolution=1)
# Обработчик для события, связанного с изменением
# положения слайдера
scl.config(command=setAll)

# Создание опций и настройка их параметров
chb_1 = Checkbutton(frm_check, text="жирный", variable=bold)
chb_1.configure(onvalue=bold, offvalue="", font=fnt_1)
chb_2 = Checkbutton(frm_check, text="курсив", variable=italic)
chb_2.configure(onvalue=italic, offvalue="", font=fnt_1)
# Начальное состояние опций
bold.set("")
italic.set("italic")

# Создание статического списка
lst = Listbox(frm_list, selectmode=SINGLE, font=fnt_1)
# Цвет фона и цвет для выделения пункта
lst.configure(bg="gray96", selectbackground="gray")
# Способ выделеня пункта и высота списка
lst.configure(activestyle="none", height=len(fonts) + 1)
# Заполнение статического списка пунктами
for n in fonts:
    lst.insert(END, n)
# По умолчанию выбран первый пункт
lst.select_set(0)
# Обработчик для статического списка
lst.bind("<<ListboxSelect>>", setAll)

# Создание кнопки
btn = Button(frm_button, text="OK", font=fnt_2)
# Обработчик для кнопки
btn.configure(command=wnd.destroy)

# Размещение меток и слайдера на панелях
lbl_text.pack(side="top", fill="x", padx=5, pady=5)
lbl.pack(side="top", fill="both", padx=5, pady=5)
lbl_color.pack(side="top", fill="x", padx=5, pady=5)
scl.pack(side="bottom", fill="x", padx=5, pady=5)
lbl_size.pack(side="bottom", fill="x", padx=5, pady=[25, 5])
lbl_font.pack(side="top", fill="x", padx=5, pady=5)
lbl_style.pack(side="top", fill="x", padx=5, pady=5)

# Размещение переключателей
rb_1.pack(side="left", fill="x", padx=5, pady=5)
rb_2.pack(side="left", fill="x", padx=5, pady=5)
rb_3.pack(side="left", fill="x", padx=5, pady=5)

# Размещение опций
chb_1.pack(side="left", fill="x", padx=5, pady=5)
chb_2.pack(side="left", fill="x", padx=5, pady=5)

# Размещение статического списка
lst.pack(side="top", fill="x", padx=5, pady=5)

# Размещение кнопки
btn.pack(side="bottom", fill="x", padx=50, pady=10)

# Размещение панелей
frm_text.place(x=5, y=5, width=w-10, height=hf)
frm_check.pack(side="bottom", fill="both", padx=5, pady=5)
frm_list.place(x=5, y=hf+10, height=hl, width=wl)
frm_scale.place(x=wl+10, y=hf+10, width=ws, height=hs)
frm_button.place(x=wl+10, y=hf+hs+15, width=ws, height=hb)

# Применение параметров шрифта к шаблонному тексту
setAll()

# Режим отслеживания значений переменных
color.trace("w", setAll)
bold.trace("w", setAll)
italic.trace("w", setAll)

# Отображение окна
wnd.mainloop()











