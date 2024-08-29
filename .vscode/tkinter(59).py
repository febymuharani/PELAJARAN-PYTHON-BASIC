# GUI -> GRAPHICAL USER INTERFACE

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# INIT
window = tk.Tk()
window.configure(bg="pink")
window.geometry("300x200")
window.resizable(False,False)
window.title("EXAMPLE")

# VARIABLE dan FUNGSI
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
def tombol_click():
    #print(f"Sudah Selesai {NAMA_BELAKANG.get()}")
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Terimakasih {NAMA_DEPAN.get()} {NAMA_BELAKANG.get() }, Sampai Jumpa!!"
    showinfo(title="HALLLO!",message=pesan)

# Frame input
input_frame = ttk.Frame(window)

# penempatan grid, pack, place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen - kompenen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2. entry untuk nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Depan:")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4. entry untuk nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,fill="x",expand=True)
# 5. tombol untuk diklik
tombol_klik = tk.Button(input_frame,text="Selesai",command=tombol_click)
tombol_klik.pack(padx=10,pady=10,fill="x",expand=True)

# Main LOOP WINDOW
window.mainloop()
