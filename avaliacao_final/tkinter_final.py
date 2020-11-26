# Grafico Animado -------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import matplotlib.animation as animation #sudo apt install python3-tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

global xs, ys, n, tempo, fig, ax, intervalo

intervalo = 4000 # tempo em milisegundos para cada plot do grafico

fig = plt.figure() # cria a figura
ax = fig.add_subplot(1,1,1) # proporções da figura animada

#define o maximo de pontos plotados no grafico
n=15

xs = [0.0] # valore inicial de x
ys = [0.0] # valor inicial de y
tempo = 0 # numero de iteração inicial

def animate(i, xs, ys, tabela, coluna):

	global tempo

	connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='') # conecta no banco de dados

	cursor = connection.cursor(buffered=True) # cria o ponteiro para acessar o banco

	cursor.execute("SELECT %s from %s ORDER BY Data_Hora DESC LIMIT 1 "%(coluna,tabela)) # busca o ultimo valor registrado na tabela e coluna pedida

	records = cursor.fetchall()

	record = str(records).strip("(),[]").split(".")[0] # trata o valor retornado do banco para transformar em um inteiro

	tempo+=1 # iteração do x

	#incremento do novo valor
	xs.append(tempo)
	ys.append(int(record))

	#mantem grafico dentro do intervalo de n plots
	if tempo > n:
		xs = xs[tempo-(n-1):tempo]
		ys = ys[tempo-(n-1):tempo]

	ax.clear() # limpa plot anterior

	# desenhar x e y
	ax.plot(xs, ys)

	plt.title(tabela)
	plt.ylabel(coluna)
	plt.xlabel('Iteração')


# Grafico Estático -------------------------------------------------------------------------

def graf(coluna):

	# encontra a tabela a ser usada de acordo com a coluna que foi pedida
	if (coluna == "CPU_Uso" or coluna == "GPU_Uso" or coluna == "GPU_MB" or coluna == "RAM_Livre" or coluna == "RAM_Usada"):
		tabela = "Ocupação"

	elif (coluna == "CPU_Mhz" or coluna == "GPU_Mhz" or coluna == "Rede_Kbps"):
		tabela = "Performance"

	elif (coluna == "CPU_ºC" or coluna == "GPU_ºC" or coluna == "HDD_ºC" or coluna == "SSD_ºC"):
		tabela = "Temperaturas"
	else:
		return

	connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='') # conecta no banco

	cursor = connection.cursor(buffered=True)
	cursor2 = connection.cursor(buffered=True)

	cursor.execute("SELECT %s from %s "%(coluna,tabela)) # busca os valores da coluna pedida
	cursor2.execute("SELECT %s.Data_Hora from %s "%(tabela,tabela)) # busca os valores de data e hora da mesma tabela buscada

	records = cursor.fetchall()
	records2 = cursor2.fetchall()

	xlabel = []
	yvalues = []
	
	i=0

	# percorre os valores de data buscados para tratar e armazenar no eixo X
	for record2 in records2:
		dummy0, dummy, record2 = str(record2).split("(")

		# em alguns casos a data tem segundos, em outros não, por isso é necessario tentar ambas opções para cada caso
		try:
			record2a, record2m, record2d, record2h, record2min, record2s, dummy = record2.split(",")
		except:
			record2a, record2m, record2d, record2h, record2min, dummy = record2.split(",")

		record2a = record2a[2:]

		# cria uma string com a hora e a data com um indice no inicio para manter a ordem dos valores
		record2 = "%s - %s:%s - %s/%s/%s"%(i, record2h.strip(" "), record2min.strip(" )"), record2d.strip(" "), record2m.strip(" "), record2a.strip(" "))
		xlabel.append(record2)
		i+=1

	# percorre os valores da coluna pedida para tratar e armazenar no eixo Y
	for record in records:
		record = str(record).strip("(,)")
		yvalues.append(float(record))

	fig_est = plt.figure(figsize=(15, 5),num='Grafico do Histórico')

	plt_est = fig_est.add_subplot(1,1,1)
	plt_est.plot(yvalues)
	plt_est.set_xticklabels(xlabel)
	plt.xticks(rotation=90)
	fig_est.tight_layout(rect=[0.05, 0.35, 1, 1])

	plt.title(tabela)
	plt.ylabel(coluna)
	plt.xlabel('Data')

	fig_est.show()

	connection.commit()
	connection.close()

# Conexão do Banco -------------------------------------------------------------------------

import mysql.connector
from mysql.connector import Error

import subprocess

import time
from time import localtime, strftime
import datetime

def quary_bd():

	listbox0.delete(0, END)
	listbox1.delete(0, END)
	listbox2.delete(0, END)
	listbox3.delete(0, END)
	listbox4.delete(0, END)
	listbox5.delete(0, END)
	listbox6.delete(0, END)
	listbox7.delete(0, END)
	listbox8.delete(0, END)
	listbox9.delete(0, END)
	listbox10.delete(0, END)
	listbox11.delete(0, END)
	listbox12.delete(0, END)

	tabs = 0 # variavel usada para controlar quantas tabelas serão usadas na busca
	tabela = []

	# cria uma lista com quais tabelas vão ser usadas na busca
	if (cu.get() == 1 or gu.get() == 1 or gm.get() == 1 or rl.get() == 1 or ru.get() == 1):
		tabela.append("Ocupação")
		tabs+=1

	if (cf.get() == 1 or gf.get() == 1 or wu.get() == 1):
		tabela.append("Performance")
		tabs+=1

	if (ct.get() == 1 or gt.get() == 1 or ht.get() == 1 or st.get() == 1):
		tabela.append("Temperaturas")
		tabs+=1

	if tabs == 0:
		return

	connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='')

	# atribui 1 nos dados que foram escolhidos
	ct1 = ct.get()
	cf1 = cf.get()
	cu1 = cu.get()
	gt1 = gt.get()
	gf1 = gf.get()
	gu1 = gu.get()
	gm1 = gm.get()
	ru1 = ru.get()
	rl1 = rl.get()
	ht1 = ht.get()
	st1 = st.get()
	wu1 = wu.get()

	linha = ""

	# cria uma string com os valores a serem buscados
	if cu1 == 1:
		linha = linha + "CPU_Uso,"

	if gu1 == 1:
		linha = linha + "GPU_Uso,"

	if gm1 == 1:
		linha = linha + "GPU_MB,"

	if ru1 == 1:
		linha = linha + "RAM_Usada,"

	if rl1 == 1:
		linha = linha + "RAM_Livre,"

	if cf1 == 1:
		linha = linha + "CPU_Mhz,"

	if gf1 == 1:
		linha = linha + "GPU_Mhz,"

	if wu1 == 1:
		linha = linha + "Rede_Kbps,"

	if ct1 == 1:
		linha = linha + "CPU_ºC,"

	if gt1 == 1:
		linha = linha + "GPU_ºC,"

	if ht1 == 1:
		linha = linha + "HDD_ºC,"

	if st1 == 1:
		linha = linha + "SSD_ºC,"

	linha = linha + "%s.Data_Hora"%tabela[0]

	bd0,bd1,bd2,bd3,bd4,bd5,bd6,bd7,bd8,bd9,bd10,bd11 = "----","----","----","----","----","----","----","----","----","----","----","----"

	#linha = "CPU_Uso, GPU_Uso, GPU_MB, RAM_Usada, RAM_Livre, CPU_Mhz, GPU_Mhz, Rede_Kbps, CPU_ºC, GPU_ºC, HDD_ºC, SSD_ºC, Ocupação.Data_Hora"

	cursor = connection.cursor()

	# seleciona qual linha de busca vai ser usada de acordo com a quantidade de tabelas
	if tabs == 3:
		quary = ("SELECT %s from %s inner join  %s on %s.Data_Hora = %s.Data_Hora inner join %s on %s.Data_Hora = %s.Data_Hora"%(linha,tabela[0],tabela[1],tabela[1],tabela[0],tabela[2],tabela[2],tabela[1]))
	
	elif tabs == 2:
		quary = ("SELECT %s from %s inner join  %s on %s.Data_Hora = %s.Data_Hora"%(linha,tabela[0],tabela[1],tabela[1],tabela[0]))
	
	elif tabs == 1:
		quary = ("SELECT %s from %s"%(linha,tabela[0]))

	dat = 0
	# verifica se datas foram passadas na busca
	if (len(data1.get()) != 0 and len(data2.get()) != 0):
		hora1,datah1 = data1.get().split(" ")
		hora1,min1,seg1 = hora1.split(":")
		dia1,mes1,ano1 = datah1.split("/")
		datahora1 = "%s-%s-%s %s:%s:%s"%(ano1,mes1,dia1,hora1,min1,seg1)

		hora2,datah2 = data2.get().split(" ")
		hora2,min2,seg2 = hora2.split(":")
		dia2,mes2,ano2 = datah2.split("/")
		datahora2 = "%s-%s-%s %s:%s:%s"%(ano2,mes2,dia2,hora2,min2,seg2)

		quary = quary + " where (%s.Data_Hora between \"%s\" and \"%s\")"%(tabela[0], datahora1, datahora2)
		dat = 1

	elif (len(data1.get()) != 0):
		hora1,datah1 = data1.get().split(" ")
		hora1,min1,seg1 = hora1.split(":")
		dia1,mes1,ano1 = datah1.split("/")
		datahora1 = "%s-%s-%s %s:%s:%s"%(ano1,mes1,dia1,hora1,min1,seg1)

		quary = quary + " where (%s.Data_Hora > \"%s\")"%(tabela[0], datahora1)
		dat = 1

	elif (len(data2.get()) != 0):
		hora2,datah2 = data2.get().split(" ")
		hora2,min2,seg2 = hora2.split(":")
		dia2,mes2,ano2 = datah2.split("/")
		datahora2 = "%s-%s-%s %s:%s:%s"%(ano2,mes2,dia2,hora2,min2,seg2)

		quary = quary + " where (%s.Data_Hora < \"%s\")"%(tabela[0], datahora2)
		dat = 1

	# verifica se valores de minimo e/ou maximo foram passados na busca
	if (len(rangein.get()) != 0 and len(rangeend.get()) != 0):
		dmax = rangein.get()

		dmin = rangeend.get()

		if dat == 0:
			quary = quary + " where (%s between \"%s\" and \"%s\")"%(col.get(), dmax, dmin)
		else:
			quary = quary.strip(")") + " and %s between \"%s\" and \"%s\")"%(col.get(), dmax, dmin)

	elif (len(rangein.get()) != 0):
		dmax = rangein.get()

		if dat == 0:
			quary = quary + " where (%s >= \"%s\") order by %s desc "%(col.get(), dmax, col.get())
		else:
			quary = quary.strip(")") + " and %s >= \"%s\") order by %s desc "%(col.get(), dmax, col.get())

	elif (len(rangeend.get()) != 0):
		dmin = rangeend.get()

		if dat == 0:
			quary = quary + " where (%s <= \"%s\") order by %s "%(col.get(), dmin, col.get())
		else:
			quary = quary.strip(")") + " and %s <= \"%s\") order by %s "%(col.get(), dmin, col.get())

	print(quary)

	cursor.execute("%s"%quary)

	records = cursor.fetchall()
	
	for record in records:

		i=0

		if cu1 == 1:
			bd0 = str(record).split(",")[i]
			i+=1

		if gu1 == 1:
			bd1 = str(record).split(",")[i]
			i+=1

		if gm1 == 1:
			bd2 = str(record).split(",")[i]
			i+=1

		if ru1 == 1:
			bd3 = str(record).split(",")[i]
			i+=1

		if rl1 == 1:
			bd4 = str(record).split(",")[i]
			i+=1

		if cf1 == 1:
			bd5 = str(record).split(",")[i]
			i+=1

		if gf1 == 1:
			bd6 = str(record).split(",")[i]
			i+=1

		if wu1 == 1:
			bd7 = str(record).split(",")[i]
			i+=1

		if ct1 == 1:
			bd8 = str(record).split(",")[i]
			i+=1

		if gt1 == 1:
			bd9 = str(record).split(",")[i]
			i+=1

		if ht1 == 1:
			bd10 = str(record).split(",")[i]
			i+=1

		if st1 == 1:
			bd11 = str(record).split(",")[i]
		
		bd12 = str(record).split("(")[2]

		try:
			bd12a,bd12m,bd12d,bd12h,bd12min,bd12s = bd12.split(",")
	
		except:
			bd12a,bd12m,bd12d,bd12h,bd12min = bd12.split(",")

		bd12 = "%s:%s - %s/%s/%s"%(bd12h.strip(" "), bd12min.strip(" )"), bd12d.strip(" "), bd12m.strip(" "), bd12a.strip(" "))

		search = bd0.strip("(") + "," + bd1.strip("(") + "," + bd2.strip("(") + "," + bd3.strip("(") + "," + bd4.strip("(") + "," + bd5.strip("(") + "," + bd6.strip("(") + "," + bd7.strip("(") + "," + bd8.strip("(") + "," + bd9.strip("(") + "," + bd10.strip("(") + "," + bd11.strip("(") + "," + bd12

		list_insert(search)

	connection.commit()
	connection.close()

def run_bd():
	global proc_monit
	proc_monit = subprocess.Popen([sys.executable, 'hw_info_psutil_BD.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

	if rb.get() == "1":
		coluna = "CPU_ºC"
	elif rb.get() == "2":
		coluna = "CPU_Mhz"
	elif rb.get() == "3":
		coluna = "CPU_Uso"
	elif rb.get() == "4":
		coluna = "GPU_ºC"
	elif rb.get() == "5":
		coluna = "GPU_Mhz"
	elif rb.get() == "6":
		coluna = "GPU_Uso"
	elif rb.get() == "7":
		coluna = "GPU_MB"
	elif rb.get() == "8":
		coluna = "RAM_Usada"
	elif rb.get() == "9":
		coluna = "RAM_Livre"
	elif rb.get() == "10":
		coluna = "HDD_ºC"
	elif rb.get() == "11":
		coluna = "SSD_ºC"
	elif rb.get() == "12":
		coluna = "Rede_Kbps"
	else:
		return

	if (coluna == "CPU_Uso" or coluna == "GPU_Uso" or coluna == "GPU_MB" or coluna == "RAM_Livre" or coluna == "RAM_Usada"):
		tabela = "Ocupação"

	elif (coluna == "CPU_Mhz" or coluna == "GPU_Mhz" or coluna == "Rede_Kbps"):
		tabela = "Performance"

	elif (coluna == "CPU_ºC" or coluna == "GPU_ºC" or coluna == "HDD_ºC" or coluna == "SSD_ºC"):
		tabela = "Temperaturas"

	# inicia o grafico animado de monitoramento
	graf = FigureCanvasTkAgg(fig, frame_graf)
	#graf.show()
	graf.get_tk_widget().pack(side="left", padx=15, pady=15)
	#graf.get_tk_widget().grid()

	# inicia a barra de ferramentas do grafico
	toolbar = NavigationToolbar2TkAgg(graf, frame_graf)
	#toolbar.update()
	graf._tkcanvas.pack(side="top", fill="x")
	#graf._tkcanvas.grid()

	ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys, tabela, coluna), interval=intervalo)

	graf.show()

def stop_bd():
	try:
		subprocess.Popen.terminate(proc_monit)
	except:
		pass

# Interface Gráfica -------------------------------------------------------------------------

from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

# define a janela principal
root = Tk()
root.title("Sistema de Monitoramento - PIVI") # titulo da janela
#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
root.geometry("350x150") # tamanho da janela

# define novas janelas
def monit():

	global rb, aba_quadro1, frame_graf

	aba_quadro1 = Toplevel()

	aba_quadro1.title("Monitoramento em Tempo Real") # titulo da janela
	#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
	aba_quadro1.geometry("800x545") # tamanho da janela

	# cria quadros nas abas/janelas com para seus conteudos
	frame_radio = Frame(aba_quadro1)

	frame_graf = Frame(aba_quadro1)

	frame_radio.pack(side="right", padx=10, anchor="e")

	frame_graf.pack(side="left", padx=10, anchor="w")

	rb = StringVar()

	Radiobutton(frame_radio, text="CPU Temp."	, variable=rb, value=1).grid(column=0, row=0, sticky="w")
	Radiobutton(frame_radio, text="CPU Freq."	, variable=rb, value=2).grid(column=0, row=1, sticky="w")
	Radiobutton(frame_radio, text="CPU Uso"		, variable=rb, value=3).grid(column=0, row=2, sticky="w")
	Radiobutton(frame_radio, text="GPU Temp."	, variable=rb, value=4).grid(column=0, row=3, sticky="w")
	Radiobutton(frame_radio, text="GPU Freq."	, variable=rb, value=5).grid(column=0, row=4, sticky="w")
	Radiobutton(frame_radio, text="GPU Uso."	, variable=rb, value=6).grid(column=0, row=6, sticky="w")
	Radiobutton(frame_radio, text="GPU Mem."	, variable=rb, value=7).grid(column=0, row=7, sticky="w")
	Radiobutton(frame_radio, text="RAM Uso"		, variable=rb, value=8).grid(column=0, row=8, sticky="w")
	Radiobutton(frame_radio, text="RAM Livre"	, variable=rb, value=9).grid(column=0, row=9, sticky="w")
	Radiobutton(frame_radio, text="HDD Temp."	, variable=rb, value=10).grid(column=0, row=10, sticky="w")
	Radiobutton(frame_radio, text="SSD Temp."	, variable=rb, value=11).grid(column=0, row=11, sticky="w")
	Radiobutton(frame_radio, text="Rede Uso"	, variable=rb, value=12).grid(column=0, row=12, sticky="w")

	botao1 = Button(frame_radio, text="Iniciar", fg="#ffffff", bg="#404142", command=run_bd , width=5)
	#botao1.pack(side="right", padx=20, anchor="se")
	botao1.grid(column=0, row=13, sticky="s")

def tabel():
	global ct,cf,cu,gt,gf,gu,gm,ru,rl,ht,st,wu
	global listbox0,listbox1,listbox2,listbox3,listbox4,listbox5,listbox6,listbox7,listbox8,listbox9,listbox10,listbox11,listbox12
	global data1, data2, rangein, rangeend, col

	aba_quadro2 = Toplevel()

	aba_quadro2.title("Tabela de Busca no Banco de Dados") # titulo da janela
	#root.iconbitmap("~/sexto_semestre/PI6/test/test.ico")
	aba_quadro2.geometry("825x666") # tamanho da janela

	frame_lists = Frame(aba_quadro2)

	frame_lists.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="n")

	# adiciona barra de rolagem a lista
	scrolly = Scrollbar(frame_lists, orient="vertical")

	# cria os campos de titulo das colunas
	listt0 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt1 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt2 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt3 = Listbox(frame_lists, height=2, width=10, fg="#ffffff", bg="#404142")
	listt3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt4 = Listbox(frame_lists, height=2, width=10, fg="#ffffff", bg="#404142")
	listt4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt5 = Listbox(frame_lists, height=2, width=8, fg="#ffffff", bg="#404142")
	listt5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt6 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt7 = Listbox(frame_lists, height=2, width=9, fg="#ffffff", bg="#404142")
	listt7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt8 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt9 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt10 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt11 = Listbox(frame_lists, height=2, width=5, fg="#ffffff", bg="#404142")
	listt11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	listt12 = Listbox(frame_lists, height=2, width=15, fg="#ffffff", bg="#404142")
	listt12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=5, row=0, rowspan=1, sticky="s")

	# escreve os tutilos de coluna
	listt0.insert("end", "CPU");listt0.insert("end", "Uso")
	listt1.insert("end", "GPU");listt1.insert("end", "Uso")
	listt2.insert("end", "GPU");listt2.insert("end", "MB")
	listt3.insert("end", "RAM");listt3.insert("end", "Uso")
	listt4.insert("end", "RAM");listt4.insert("end", "Livre")
	listt5.insert("end", "CPU");listt5.insert("end", "MHz")
	listt6.insert("end", "GPU");listt6.insert("end", "MHz")
	listt7.insert("end", "Rede");listt7.insert("end", "kbps")
	listt8.insert("end", "CPU");listt8.insert("end", "°C")
	listt9.insert("end", "GPU");listt9.insert("end", "°C")
	listt10.insert("end", "HDD");listt10.insert("end", "°C")
	listt11.insert("end", "SSD");listt11.insert("end", "°C")
	listt12.insert("end", "Data");listt12.insert("end", "Hora")

	# cria as colunas de informaçoes
	listbox0 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox0.grid(column=0, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox1 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox1.grid(column=1, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox2 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox2.grid(column=2, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox3 = Listbox(frame_lists, height=25, width=10, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox3.grid(column=3, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox4 = Listbox(frame_lists, height=25, width=10, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox4.grid(column=4, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox5 = Listbox(frame_lists, height=25, width=8, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox5.grid(column=5, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox6 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox6.grid(column=6, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox7 = Listbox(frame_lists, height=25, width=9, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox7.grid(column=7, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox8 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox8.grid(column=8, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox9 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox9.grid(column=9, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox10 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox10.grid(column=10, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox11 = Listbox(frame_lists, height=25, width=5, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox11.grid(column=11, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	listbox12 = Listbox(frame_lists, height=25, width=15, fg="#ffffff", bg="#404142", yscrollcommand=scrolly.set)
	listbox12.grid(column=12, columnspan=1, ipadx=0, ipady=0, padx=0, pady=0, row=1, rowspan=1, sticky="n")

	scrolly.config(command=scrollall)
	scrolly.grid(column=13, padx=0, pady=0, row=1, rowspan=1, sticky="w")

	# variaveis para as caixas de seleção
	ct = IntVar()
	cf = IntVar()
	cu = IntVar()
	gt = IntVar()
	gf = IntVar()
	gu = IntVar()
	gm = IntVar()
	ru = IntVar()
	rl = IntVar()
	ht = IntVar()
	st = IntVar()
	wu = IntVar()

	# criação das caixas de seleção para busca no banco
	CT = Checkbutton(aba_quadro2, text="CPU Temp."	, variable=ct, onvalue="1")
	CT.deselect()
	CT.grid(column=0, row=1, padx=5, sticky="w")

	CF = Checkbutton(aba_quadro2, text="CPU Freq."	, variable=cf)
	CF.deselect()
	CF.grid(column=0, row=2, padx=5, sticky="w")

	CU = Checkbutton(aba_quadro2, text="CPU Uso"	, variable=cu)
	CU.deselect()
	CU.grid(column=0, row=3, padx=5, sticky="w")

	GT = Checkbutton(aba_quadro2, text="GPU Temp."	, variable=gt)
	GT.deselect()
	GT.grid(column=0, row=1, padx=105 , sticky="w")

	GF = Checkbutton(aba_quadro2, text="GPU Freq."	, variable=gf)
	GF.deselect()
	GF.grid(column=0, row=2, padx=105 , sticky="w")

	GU = Checkbutton(aba_quadro2, text="GPU Uso."	, variable=gu)
	GU.deselect()
	GU.grid(column=0, row=3, padx=105 , sticky="w")

	GM = Checkbutton(aba_quadro2, text="GPU Mem."	, variable=gm)
	GM.deselect()
	GM.grid(column=0, row=1, padx=205 , sticky="w")

	RU = Checkbutton(aba_quadro2, text="RAM Uso"	, variable=ru)
	RU.deselect()
	RU.grid(column=0, row=2, padx=205 , sticky="w")

	RL = Checkbutton(aba_quadro2, text="RAM Livre"	, variable=rl)
	RL.deselect()
	RL.grid(column=0, row=3, padx=205 , sticky="w")

	HT = Checkbutton(aba_quadro2, text="HDD Temp."	, variable=ht)
	HT.deselect()
	HT.grid(column=0, row=1, padx=305 , sticky="w")

	ST = Checkbutton(aba_quadro2, text="SSD Temp."	, variable=st)
	ST.deselect()
	ST.grid(column=0, row=2, padx=305 , sticky="w")

	WU = Checkbutton(aba_quadro2, text="Rede Uso"	, variable=wu)
	WU.deselect()
	WU.grid(column=0, row=3, padx=305 , sticky="w")

	data_label = Label(aba_quadro2, text="Ex. 03:14:07 19/01/2038").grid(column=0, row=1, pady=0, padx=115, sticky="e")

	data1 = Entry(aba_quadro2, width=20)
	data1.grid(column=0, row=2, pady=0, padx=100, sticky="e")

	data2 = Entry(aba_quadro2, width=20)
	data2.grid(column=0, row=3, pady=0, padx=100, sticky="e")

	data1_label = Label(aba_quadro2, text="Data de Inicio").grid(column=0, row=2, pady=0, padx=275, sticky="e")

	data2_label = Label(aba_quadro2, text="Data Final").grid(column=0, row=3, pady=0, padx=275, sticky="e")

	col = StringVar()

	cols = ["Escolha a Coluna",
	"CPU_Uso",
	"GPU_Uso",
	"GPU_MB",
	"RAM_Livre",
	"RAM_Usada",
	"CPU_Mhz",
	"GPU_Mhz",
	"Rede_Kbps",
	"CPU_ºC",
	"GPU_ºC",
	"HDD_ºC",
	"SSD_ºC"]

	col.set(cols[0])

	dado = ttk.OptionMenu(aba_quadro2, col, *cols)

	dado.grid(column=0, row=5, pady=0, padx=5, sticky="w")
	dado.config(width = 14)

	#colsel_label = Label(aba_quadro2, text=col.get()).grid(column=0, row=4, pady=0, padx=0, sticky="w")

	rangein, rangeend = 0,0

	rangein = Entry(aba_quadro2, width=20)
	rangein.grid(column=0, row=5, pady=0, padx=166, sticky="w")

	rangeend = Entry(aba_quadro2, width=20)
	rangeend.grid(column=0, row=5, pady=0, padx=336, sticky="w")

	rangein_label = Label(aba_quadro2, text="Dado Min.").grid(column=0, row=4, pady=0, padx=166, sticky="w")

	rangeend_label = Label(aba_quadro2, text="Dado Max").grid(column=0, row=4, pady=0, padx=336, sticky="w")

	botao2 = Button(aba_quadro2, text="Busca", fg="#ffffff", bg="#404142", command=quary_bd, width=5)
	botao2.grid(column=0, row=1, pady=0, padx=20, sticky="e")
	#botao.pack()

	botao3 = Button(aba_quadro2, text="Gráfico", fg="#ffffff", bg="#404142", command=select_graf, width=5)
	botao3.grid(column=0, row=3, pady=0, padx=20, sticky="e")
	#botao.pack()

def select_graf():

	list0,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11 = "","","","","","","","","","","",""

	# atribui o valor da coluna selecionada em variaveis
	list0 = listbox0.get("anchor")
	#listbox0 = Listbox(exportselection=0)
	list1 = listbox1.get("anchor")
	#listbox1 = Listbox(exportselection=0)
	list2 = listbox2.get("anchor")
	#listbox2 = Listbox(exportselection=0)
	list3 = listbox3.get("anchor")	

	list4 = listbox4.get("anchor")

	list5 = listbox5.get("anchor")

	list6 = listbox6.get("anchor")

	list7 = listbox7.get("anchor")

	list8 = listbox8.get("anchor")

	list9 = listbox9.get("anchor")

	list10 = listbox10.get("anchor")

	list11 = listbox11.get("anchor")

	# testa qual variavel não está nula e envia a coluna correspondente para a função do grafico
	if list0 != "":
		graf("CPU_Uso")

	elif list1 != "":
		graf("GPU_Uso")

	elif list2 != "":
		graf("GPU_MB")

	elif list3 != "":
		graf("RAM_Usada")

	elif list4 != "":
		graf("RAM_Livre")

	elif list5 != "":
		graf("CPU_Mhz")

	elif list6 != "":
		graf("GPU_Mhz")

	elif list7 != "":
		graf("Rede_Kbps")

	elif list8 != "":
		graf("CPU_ºC")

	elif list9 != "":
		graf("GPU_ºC")

	elif list10 != "":
		graf("HDD_ºC")

	elif list11 != "":
		graf("SSD_ºC")


# insere as informações nas colunas
def list_insert(nums):

	bd0,bd1,bd2,bd3,bd4,bd5,bd6,bd7,bd8,bd9,bd10,bd11,bd12 = nums.split(",")

	global listbox0,listbox1,listbox2,listbox3,listbox4,listbox5,listbox6,listbox7,listbox8,listbox9,listbox10,listbox11,listbox12

	# insere os valores recebidos em cada uma das listas, o parametro "0" faz com que os valores sejam inseridos no inicio
	listbox0.insert("0", bd0)
	listbox1.insert("0", bd1)
	listbox2.insert("0", bd2)
	listbox3.insert("0", bd3)
	listbox4.insert("0", bd4)
	listbox5.insert("0", bd5)
	listbox6.insert("0", bd6)
	listbox7.insert("0", bd7)
	listbox8.insert("0", bd8)
	listbox9.insert("0", bd9)
	listbox10.insert("0", bd10)
	listbox11.insert("0", bd11)
	listbox12.insert("0", bd12)

# função que permite rolar todas colunas ao mesmo tempo
def scrollall(*args): # envia o mesmo valor de scroll no eixo y para todas as listas
	listbox0.yview(*args)
	listbox1.yview(*args)
	listbox2.yview(*args)
	listbox3.yview(*args)
	listbox4.yview(*args)
	listbox5.yview(*args)
	listbox6.yview(*args)
	listbox7.yview(*args)
	listbox8.yview(*args)
	listbox9.yview(*args)
	listbox10.yview(*args)
	listbox11.yview(*args)
	listbox12.yview(*args)

# configura os botões
botao0root = Button(root, text="QUIT", fg="#ffffff", bg="#404142", command=lambda:[stop_bd(),quit()], width=190)
#botao0root.grid()
botao0root.pack(side="bottom", padx=5, pady=5, anchor="se")

botao1root = Button(root, text="Monitorar", fg="#ffffff", bg="#404142", command=monit, width=190)
#botao1root.grid()
botao1root.pack(side="top", padx=5, pady=5, anchor="se")

botao2root = Button(root, text="Buscar", fg="#ffffff", bg="#404142", command=tabel, width=190)
#botao2root.grid()
botao2root.pack(side="top", padx=5, pady=0, anchor="se")

root.mainloop()