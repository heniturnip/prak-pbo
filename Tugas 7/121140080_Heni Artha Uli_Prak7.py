import tkinter as tk
from tkinter import filedialog

class PengolahTeks:
    def __init__(self, master):
        self.master = master
        self.master.title("Text Editor")
        self.text = tk.Text(self.master)
        self.text.pack(expand=True, fill='both')
        self.menu()
        
    #membuat menu bar pada window aplikasi
    def menu(self):
        menu_bar = tk.Menu(self.master)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        menu_bar.add_cascade(label="Menu", menu=file_menu)
        self.master.config(menu=menu_bar)
        
    #membuka file teks 
    def open_file(self):
        #membuka dialog box untuk memilih file yang akan dibuka
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    self.text.delete('1.0', 'end')
                    self.text.insert('1.0', file.read())
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))
                
    #menyimpan isi teks ke dalam file yang telah dibuka sebelumnya
    def save_file(self):
        #menyimpan isi teks yang sudah diedit
        if hasattr(self, 'file_path'):
            try:
                with open(self.file_path, 'w') as file:
                    file.write(self.text.get('1.0', 'end'))
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))
        else:
            self.save_file_as()
            
    #menyimpan isi teks ke dalam file baru
    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.txt')
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(self.text.get('1.0', 'end'))
                    self.file_path = file_path
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

if __name__ == '__main__':
    root = tk.Tk()
    PengolahTeks(root)
    root.mainloop()
