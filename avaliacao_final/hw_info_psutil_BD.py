#importa biblioteca para rodar comandos bash diretamente do script python
import subprocess 

#importa biblioteca para gerenciamento de avisos
#import warnings
#warnings.filterwarnings("ignore") #ignora avisos 

#importa bibilhotecas de data e hora
import time
from time import localtime, strftime
import datetime

#importa biblioteca para comunicação com o banco de dados
import mysql.connector
from mysql.connector import Error

#importa bibliotecas de captura de informações do sistema
import psutil #sudo apt install python3-psutil
from pyspectator.computer import Computer

computer = Computer()
computer.os

sleep = 0 # Intervalo em segundos de cada postagem
monit_limit = 120

# Tenta iniciar conexão com o banco de dados
try:
	connection = mysql.connector.connect(host='localhost', database='pivi', user='icaro', password='')

	if connection.is_connected():
		db_Info = connection.get_server_info()
		print("Conectado ao Servidor MySQL versão ", db_Info)
		cursor = connection.cursor()
		cursor.execute("select database();")
		record = cursor.fetchone()
		print("Você está conectado ao banco de dados: ", record)

# Retorna mensagem de erro caso conexão falhe
except Error as e:
	print("Erro conectando ao MySQL", e)

finally:

	cont = 0
	while cont < monit_limit: # Numero de ciclos de leituda das informações
		cont = cont + 1

		########################### Leitura das informações ####################################

		#batt = psutil.sensors_battery()

		#chrg = subprocess.check_output(["sudo", "dmidecode", "-t", "22"])
		
		#NET

		old_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
		time.sleep(1)
		new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
		net_sts = new_value - old_value

		#CPU

		cpu_percent = psutil.cpu_percent(interval=1)
		cpu_freq = psutil.cpu_freq(percpu=False)
		cpu_temp = psutil.sensors_temperatures(fahrenheit=False)

		#RAM

		mem = psutil.virtual_memory()

		ram = subprocess.check_output(["sudo", "lshw", "-short", "-C", "memory"])
		
		#HDD
		
		hd_tmp = subprocess.check_output(["sudo", "smartctl", "-A", "/dev/sda"])
		
		hd = subprocess.check_output(["sudo", "smartctl", "-i", "/dev/sda"])
		
		#SSD

		ssd_tmp = subprocess.check_output(["sudo", "smartctl", "-A", "/dev/nvme0"])
		
		ssd = subprocess.check_output(["sudo", "smartctl", "-i", "/dev/nvme0"])
		
		#GPU

		gpu = subprocess.check_output(["nvidia-settings", "-q", "gpus", "-t"])

		gpu_temp = subprocess.check_output(["nvidia-settings", "-q", "gpucoretemp", "-t"])
		gpu_freq = subprocess.check_output(["nvidia-settings", "-q", "GPUCurrentClockFreqs", "-t"])
		gpu_mem = subprocess.check_output(["nvidia-settings", "-q", "UsedDedicatedGPUMemory", "-t"])
		gpu_percent = subprocess.check_output(["nvidia-settings", "-q", "GPUUtilization", "-t"])

		data = strftime("%Y-%m-%d", localtime())
		hora = strftime("%H:%M:%S", localtime())

		datahora = strftime("%Y-%m-%d %H:%M:%S", localtime())
		datahora = time.mktime(datetime.datetime.strptime(datahora,"%Y-%m-%d %H:%M:%S").timetuple())

		########################## Tratamento de valores ###################################

		#Bateria

		#chrg = chrg.decode("utf-8")
		#chrg = chrg.split("\n")
		#chrg1 = chrg[12]
		#chrg2 = chrg[13]
		#dummy, chrg1 = chrg1.split(":")
		#dummy, chrg2 = chrg2.split(":")
		#chrg = chrg1.strip(" ") + chrg2

		#NET

		net_sts = net_sts/1000

		#HDD

		hd_tmp = hd_tmp.decode("utf-8")
		hd_tmp = hd_tmp.split("\n")
		hd_tmp = hd_tmp[19]
		dummy, hd_tmp = hd_tmp.split("-")
		hd_tmp = hd_tmp.strip(" ")

		hd_tmp = int(hd_tmp)

		hd = hd.decode("utf-8")
		hd = hd.split("\n")
		hd1 = hd[4]
		hd2 = hd[8]
		dummy, hd1 = hd1.split(":")
		dummy, hd2 = hd2.split("[")
		hd = hd1.strip(" ") + " " + hd2.strip(" ]")

		#SSD

		ssd_tmp = ssd_tmp.decode("utf-8")
		ssd_tmp = ssd_tmp.split("\n")
		ssd_tmp = ssd_tmp[6]
		dummy, ssd_tmp = ssd_tmp.split(":")
		ssd_tmp = ssd_tmp.strip(" Celscius")

		ssd_tmp = int(ssd_tmp)

		ssd = ssd.decode("utf-8")
		ssd = ssd.split("\n")
		ssd = ssd[4]
		dummy, ssd = ssd.split(":")
		ssd = ssd.strip(" ")

		#RAM

		mem_free = float(round(mem.available/1000000,2))
		mem_used = float(round(mem.used/1000000,2))

		ram = ram.decode("utf-8")
		ram = ram.split("\n")
		ram1 = ram[5]
		ram2 = ram[4]
		dummy, ram1 = ram1.split("memory")
		dummy, ram2 = ram2.split("memory")
		ram = ram1.strip(" ") + " + " + ram2.strip(" ")

		#CPU

		cpu_percent = float(cpu_percent)

		cpu_freq = float(round(cpu_freq.current,2))

		names = list(cpu_temp.keys())
		if names[2] in cpu_temp:
			for entry in cpu_temp[names[2]]:
				#print("%s %s°C" % (entry.label, entry.current))
				break
		cpu_temp = entry.current

		cpu_temp = int(cpu_temp)

		#GPU

		gpu = gpu.decode("utf-8")
		gpu = gpu.split("\n")
		gpu = gpu[2].split("(")
		gpu = gpu[1].strip(")")

		gpu_temp = gpu_temp.decode("utf-8")
		gpu_temp = gpu_temp.split("\n")

		gpu_temp = int(gpu_temp[0])

		gpu_freq = gpu_freq.decode("utf-8")
		gpu_freq = gpu_freq.split("\n")
		gpu_freq = gpu_freq[0].split(",")

		gpu_freq = int(gpu_freq[0])

		gpu_mem = gpu_mem.decode("utf-8")
		gpu_mem = gpu_mem.split("\n")

		gpu_mem = int(gpu_mem[0])

		gpu_percent = gpu_percent.decode("utf-8") 
		gpu_percent = gpu_percent.split("\n")
		gpu_percent = gpu_percent[0].split(",")
		gpu_percent = gpu_percent[0].split("=")

		gpu_percent = int(gpu_percent[1])

		net_sts = round(net_sts,2)

		##################################### Printa os valores ################################
		print("\n##########################################################################")
		
		print("\n#", computer.processor.name)
		print("Uso da CPU:			", cpu_percent, "%")
		print("Freq. da CPU:		", cpu_freq, "Mhz")
		print("Temp. da CPU:		", cpu_temp, "°C")

		print("\n#", gpu)
		print("Uso da GPU:			", gpu_percent, "%")
		print("Freq. da GPU:		", gpu_freq, "Mhz")
		print("Temp. da GPU:		", gpu_temp, "°C")
		print("Uso da Mem. da GPU:	", gpu_mem, "MB")

		print("\n#", ram)
		print("RAM Livre:			", mem_free,"MB")
		print("RAM Usada:			", mem_used,"MB")

		print("\n#", hd)
		print("HDD Temp.:			", hd_tmp, "°C")

		print("\n#", ssd)
		print("SSD Temp.:			", ssd_tmp, "°C")

		print("\n# Rede")
		print("Uso de banda:		", net_sts, "Kbps")

		#print("\n# Bateria", chrg)
		#print("Nível de Carga:		", batt.percent, "%")

		print("\n", data, hora)

		#print("##########################################################################")

		##################################### Envia para o banco de dados ################################

		#cursor = connection.cursor(prepared=True)

		insert_uso = "insert into Ocupação(CPU_Uso, GPU_Uso, GPU_MB, RAM_Livre, RAM_Usada)values(%s,%s,%s,%s,%s);"%(cpu_percent,gpu_percent,gpu_mem,mem_free,mem_used)

		insert_velocidade = "insert into Performance(CPU_Mhz, GPU_Mhz, Rede_Kbps)values(%s,%s,%s);"%(cpu_freq,gpu_freq,net_sts)

		insert_temperatura = "insert into Temperaturas(CPU_ºC, GPU_ºC, HDD_ºC, SSD_ºC)values(%s,%s,%s,%s);"%(cpu_temp,gpu_temp,hd_tmp,ssd_tmp)

		cursor.execute(insert_uso)
		cursor.execute(insert_velocidade)
		cursor.execute(insert_temperatura)
		connection.commit()

		time.sleep(sleep)

	cursor.close()
	connection.close()
	print("MySQL connection is closed")