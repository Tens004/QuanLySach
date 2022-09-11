class Book:
	def __init__(self, stt, name, author, date, month, year):
		self.stt = stt
		self.name = name
		self.author = author
		self.date = date #int
		self.month = month #int
		self.year = year #int
	@property
	def info(self):
		s =  '{stt}/ {name} | {author} | {date}/{month}/{year}\n'
		Info = s.format(stt=str(self.stt).zfill(3), name='{:<60}'.format(self.name), author='{:<40}'.format(self.author), date=str(self.date).zfill(2), month=str(self.month).zfill(2), year=str(self.year).zfill(4))
		return Info
	@classmethod
	def from_ReadData(cls, book_list_info):
		stt = int(book_list_info[0])
		name = book_list_info[1].strip(' ')
		author = book_list_info[2].strip(' ')
		date = book_list_info[3]
		date = int(str(date).zfill(2))
		month = book_list_info[4]
		month = int(str(month).zfill(2))
		year = book_list_info[5]
		year = int(str(year).zfill(4))
		return cls(stt, name, author, date, month, year)
def Read_data():
	# s = stt/name | author | date/month/year
	# s = stt/name | author | date/month/year\n
	fileSach = open('Data.txt', mode='r', encoding='utf8')
	lst_line = fileSach.readlines()
	obs_lst = []
	for line in lst_line:
		if line.isspace(): continue
		obs = line.split('/ ') # obs = [stt, name | author | date/month/year\n]
		a = obs[-1].split(' | ') # a = [name, author, date/month/year\n]
		obs.pop()
		obs.extend([a[0], a[1]]) # obs = [stt, name, author]
		a = a[-1].split('/') # a = [date, month, year\n]
		obs.extend([a[0], a[1]]) # obs = [stt, name, author, date, month]
		a = a[-1].split('\n')
		obs.append(a[0]) #[stt, name, author, date, month, year]
		obs_lst.append(obs)
	fileSach.close()

	book = [] 
	for line in obs_lst: # Moi doi tuong Book la mot phan tu trong list 'book'
		book.append(Book.from_ReadData(line)) 
	return book
def Write_temporarily(para):
	fileTemporay = open('DataTemporary.txt', mode='w', encoding='utf8')

	lst = [s.info + '\n' for s in para]
	fileTemporay.writelines(lst)
	fileTemporay.close()
def Sort(para_book):
	def convention(obj_book):
		return (obj_book.year, obj_book.month, obj_book.date)
	para_book = sorted(para_book, key=convention)
	stt = 0
	for obj in para_book:
		stt += 1
		obj.stt = stt
	return para_book
def Write_data(para):
	fileData = open('Data.txt', mode='w', encoding='utf8')
	lst = [s.info + '\n' for s in para]
	fileData.writelines(lst)
	fileData.close()
def Read_dataTemporary():
	# s = stt/name | author | date/month/year
	# s = stt/name | author | date/month/year\n
	fileSach = open('DataTemporary.txt', mode='r', encoding='utf8')
	lst_line = fileSach.readlines()
	obs_lst = []
	for line in lst_line:
		if line.isspace(): continue
		obs = line.split('/ ') # obs = [stt, name | author | date/month/year\n]
		a = obs[-1].split(' | ') # a = [name, author, date/month/year\n]
		obs.pop()
		obs.extend([a[0], a[1]]) # obs = [stt, name, author]
		a = a[-1].split('/') # a = [date, month, year\n]
		obs.extend([a[0], a[1]]) # obs = [stt, name, author, date, month]
		a = a[-1].split('\n')
		obs.append(a[0]) #[stt, name, author, date, month, year]
		obs_lst.append(obs)
	fileSach.close()

	book = [] 
	for line in obs_lst: # Moi doi tuong Book la mot phan tu trong list 'book'
		book.append(Book.from_ReadData(line)) 
	return book
