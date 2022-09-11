import tkinter, SapXepSach
from tkinter import*
from tkinter import scrolledtext
from tkinter import messagebox
from SapXepSach import*
from time import sleep

screen = Tk()
screen.title('Quản Lý Sách v4.0')
screen.geometry('860x600')
screen.iconbitmap('book_library.ico')

bg_color = 'gray'
bt_color = '#21211a'
text_color = 'white'
box_color = '#e6e5df'
scroll_color = '#b0b0b0'
font_14 = ('arial', 14)
save = True
textEntry1 = StringVar()
textEntry2= StringVar()
textEntry3 = StringVar()
textEntry4 = StringVar()
textEntry5 = StringVar()

screen.configure(background=bg_color)
en_focus = 0
def dichuyen_right(key):
	global en_focus
	if en_focus < 4:
		en_focus += 1
		lst_en[en_focus].focus()
def dichuyen_left(key):
	global en_focus
	if en_focus > 0:
		en_focus -= 1
		lst_en[en_focus].focus()

def func_them():
	name = en_ten.get()
	author = en_tacGia.get()
	date = en_ngayNhan_date.get()
	month = en_ngayNhan_month.get()
	year = en_ngayNhan_year.get()
	if name!='' or author!='' or date!='' or month!='' or year!='':
		s = '{}/ {} | {} | {}/{}/{}\n'
		new_info = s.format('000', '{:<60}'.format(name), '{:<40}'.format(author), str(date).zfill(2), str(month).zfill(2), str(year).zfill(4))
		fileDataTemporary = open('DataTemporary.txt', mode='a', encoding='utf8')
		fileDataTemporary.write(new_info)
		fileDataTemporary.close()
		global save
		save = False
		func_display_full()
		messagebox.showinfo('Add', 'Add successfully!' + ' '*20)

def func_tim(default=None): # Truyền default để nhân đối số tự động truyền vào khi dùng chức năng nhấn enter để tìm kiếm
	name = en_ten.get()
	author = en_tacGia.get()
	date = en_ngayNhan_date.get() 
	month = en_ngayNhan_month.get()
	year = en_ngayNhan_year.get()
	
	global ans# dung cho func_delete
	ans = []
	data = Read_data()
	if name!='':	
		for book in data:
			if book.name == name: ans.append(book)
		if author!='':
			for book in ans:
				if book.author != author: ans.remove(book)
		if date!='':
			for book in ans:
				if book.date != int(date): ans.remove(book)
		if month!='':
			for book in ans:
				if book.month != int(month): ans.remove(book)
		if year!='':
			for book in ans:
				if book.year != int(year): ans.remove(book)
	elif author!='':
		for book in data:
			if book.author == author: ans.append(book)
		if date!='':
			for book in ans:
				if book.date != int(date): ans.remove(book)
		if month!='':
			for book in ans:
				if book.month != int(month): ans.remove(book)
		if year!='':
			for book in ans:
				if book.year != int(year): ans.remove(book)
	elif date!='':
		for book in data:
			if book.date == int(date): ans.append(book)
		if month!='':
			for book in ans:
				if book.month != int(month): ans.remove(book)
		if year!='':
			for book in ans:
				if book.year != int(year): ans.remove(book)
	elif month!='':
		for book in data:
			if book.month == int(month): ans.append(book)
		if year!='':
			for book in ans:
				if book.year != int(year): ans.remove(book)
	elif year!='':
		for book in data:
			if book.year == int(year): ans.append(book)

	display.delete(1.0, END)
	for book in ans:
		display.insert(INSERT, book.info + '\n')
	bt_back.place(x = 720, y = 115)


def func_save():
	Write_data(book_display)
	func_reset()
	global save
	save = True
def func_display_full():
	bt_back.place_forget()
	display.delete(1.0, END)
	book_lst = Read_dataTemporary()
	book_lst.reverse()
	for book in book_lst:
		display.insert(INSERT, book.info + '\n')
	# Dung cho func_save de du lieu save giong voi du lieu dang hien thi
	global book_display
	book_display = book_lst
def func_reset():
	display.delete(1.0, END)
	a = Read_data()
	Write_temporarily(a)
	func_display_full()
def func_delete():
	if messagebox.askokcancel('Delete!', 'Do you really want to Delete?'):
		data = Read_dataTemporary()
		for a in ans:
			for d in data:
				if d.name==a.name and d.author==a.author and d.date==a.date and d.month==a.month and d.year==a.year:
					print(a)
					data.remove(d)
					continue
		Write_temporarily(data)
		global save
		save = False
		func_display_full()
		messagebox.showinfo('Delete', 'Deleted!' + ' '*50)

def func_sort():
	book_sort = Sort(book_display)
	fileDataTemporary = open('DataTemporary.txt', mode='w', encoding='utf8')
	for book in book_sort:
		fileDataTemporary.write(book.info)
	fileDataTemporary.close()
	global save
	save = False
	func_display_full()
	messagebox.showinfo('Sort', 'Sorted!' + ' '*50)
def func_saveQuit():
	func_save()
	screen.destroy()
	global save
	save = True
def on_closing():
	if save == False:
		res = messagebox.askyesnocancel('Quit', 'Do you want to save changes?')
		if res:
			func_saveQuit()
		elif res == False:
			screen.destroy()
	else:
		screen.destroy()
def func_clean():
	textEntry1.set('')
	textEntry2.set('')
	textEntry3.set('')
	textEntry4.set('')
	textEntry5.set('')
	en_ten.focus()
	global en_focus
	en_focus = 0

lb_ten = Label(screen, text='Name:', bg=bg_color, font=font_14, fg=text_color)
en_ten = Entry(screen, width=50, bg=box_color, textvariable=textEntry1)
lb_tacGia = Label(screen, text='Author:', bg=bg_color, font=font_14, fg=text_color)
en_tacGia = Entry(screen, width=15, bg=box_color, textvariable=textEntry2)
lb_ngayNhan = Label(screen, text='Date:', bg=bg_color, font=font_14, fg=text_color)
en_ngayNhan_date = Entry(screen, width=3, bg=box_color, textvariable=textEntry3)
en_ngayNhan_month = Entry(screen, width=3, bg=box_color, textvariable=textEntry4)
en_ngayNhan_year = Entry(screen, width=4, bg=box_color, textvariable=textEntry5)
bt_tim = Button(screen, text=' Search ', width = 10, height =1, command=func_tim, bg=bt_color, fg=text_color)
bt_them = Button(screen, text=' Add... ', width = 10, height=1, command=func_them, bg=bt_color, fg=text_color)
display = scrolledtext.ScrolledText(screen, width=98, height=20, bg=bg_color, font=('arial', 11))
bt_Save = Button(screen, text='Save', command=func_save, width=10, height=2, bg=bt_color, fg=text_color)
bt_reset = Button(screen, text='Reset', width = 5, height=1, command=func_reset, bg='#696969', fg='black')
bt_delete = Button(screen, text='Delete', command=func_delete, bg='#696969', fg='black', font=('arial', 9))
bt_sort = Button(screen, text=' Sort ', width=8, height=1, command=func_sort, bg=bt_color, fg=text_color)
bt_saveQuit = Button(screen, text='Save & Quit', width=15, height=2, bg=bt_color, fg=text_color, command=func_saveQuit)
bt_back = Button(screen, text='Back', width=10, height=1, command=func_display_full, bg=bt_color, fg=text_color)
bt_clean = Button(screen, text='Clean', width=7, command=func_clean, bg=bt_color, fg='white', font=('arial', 8))
lb_email = Label(screen, text='Email: thanhtien.vn2004@gmail.com', font=('arial', 10), fg='black', bg=bg_color)

lb_ten.place(x = 70, y = 20)
en_ten.place(x = 130, y = 25)
lb_tacGia.place(x = 450, y = 20)
en_tacGia.place(x = 515, y = 25)
lb_ngayNhan.place(x = 625, y = 20)
en_ngayNhan_date.place(x = 675, y =25)
en_ngayNhan_month.place(x = 705, y = 25)
en_ngayNhan_year.place(x = 735, y = 25) 
bt_tim.place(x = 310, y = 70)
bt_them.place(x = 410, y = 70)
display.place(x = 30, y = 150)
bt_Save.place(x = 330, y = 525)
bt_saveQuit.place(x = 440, y = 525)
bt_reset.place(x = 760, y = 500)
bt_delete.place(x = 510, y = 70)
bt_sort.place(x = 680, y = 500)
bt_clean.place(x = 775, y = 22)
lb_email.place(x = 5, y = 575)

en_ten.focus()
a = Read_data()
Write_temporarily(a)
func_display_full()

lst_en = [en_ten, en_tacGia, en_ngayNhan_date, en_ngayNhan_month, en_ngayNhan_year]
screen.bind('<Return>', func_tim)
screen.bind('<Right>', dichuyen_right)
screen.bind('<Left>', dichuyen_left)
screen.protocol("WM_DELETE_WINDOW", on_closing)
screen.mainloop()