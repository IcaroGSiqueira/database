INSERT into pivi.Temperaturas (CPU_ºC ,GPU_ºC ,HDD_ºC , SSD_ºC ,Data_Hora) 
select CPU_ºC ,GPU_ºC ,HDD_ºC , SSD_ºC ,Data_Hora FROM pivi.projeto;