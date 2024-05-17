# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:43:51 2024

@author: ocanh
"""

import datetime
import pytz

def ocan_decorator(inner):
    def inner_decorator():
        # Mendapatkan waktu UTC
        utc_now = datetime.datetime.now(pytz.utc)

        # Mengubah waktu UTC menjadi UTC+7
        jakarta_tz = pytz.timezone('Asia/Jakarta')
        jakarta_now = utc_now.astimezone(jakarta_tz)
        print("\nTanggal:", jakarta_now.strftime("%Y-%m-%d"))
        print("Waktu:", jakarta_now.strftime("%H:%M:%S"))

    return inner_decorator

@ocan_decorator
def decorated():
    print("berubah menjadi")

# Menampilkan informasi awal
print("Nama: Hasanul Bashori")
print("NIM: 064002300041")
print("Timezone: Asia/Jakarta")

# Membuat loop untuk menunggu input Enter dari pengguna
while True:
    # Memanggil fungsi decorated
    decorated()
    input_value = input("\nKetuk Enter untuk melanjutkan, atau ketik 'exit' untuk keluar: ")
    if input_value.lower() == 'exit':
        break  
