import schedule
import time
import speedtest
from datetime import datetime
import pandas as pd
import numpy as np
from threading import Timer

def speedTest():
    data = pd.read_excel('dados.xlsx', sheet_nome = 'base')
    speed = speedtest.SpeedTest()
    data_atual = datetime.now().strftime('%d%m%Y')
    hora_atual = datetime.now().strftime('%H:%M')
    vel = speed.download(threads = None) * (10**-6)
    data.loc[len(data)] = [data_atual, hora_atual, vel]
    data.to_excel('dados.xlsx', sheet_name = 'base', index = False)
    Timer(1800, speedTest).start()
    
speedTest()