import tkinter as tk
from tkinter.constants import *
from tkinter import ttk
from tkinter import filedialog
import yaml

def LOL_LangChanger():

    def loadFile():
        folder_path = filedialog.askdirectory()
        loadFile_en.delete(0, 'end')
        if not folder_path:
            loadFile_en.insert(END, "C:\ProgramData\Riot Games\Metadata\league_of_legends.live\league_of_legends.live.product_settings.yaml")
        else:
            loadFile_en.insert(0, folder_path)

    def update_locale_settings(file_path, new_locale):

        locale_mapping = {
            'zh_TW': '繁體中文',
            'ja_JP': '日文',
            'ko_KR': '韓文',
            'zh_CN': '簡體中文',
            'fr_FR': '法文',
            'de_DE': '德文',
            'vi_VN': '越語',
        }

        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
                if 'settings' in data and 'locale' in data['settings']:
                    data['settings']['locale'] = new_locale

            with open(file_path, 'w') as file:
                yaml.dump(data, file)

            print(f'Successfully updated locale to "{new_locale}"')
            lb3_2 = tk.Label(text=f"成功更改語言: {locale_mapping.get(new_locale)}"+" "*50, bg="grey50", fg="white", height=1)
            lb3_2.place(x=75, y=111)
            

        except Exception as e:
            print(f'Error updating locale: {e}')
            lb3_2 = tk.Label(text="")
            lb3_2 = tk.Label(text="發生錯誤"+" "*50, bg="grey50", fg="white", height=1)
            lb3_2.place(x=75, y=111)

            

    def saveLocale():

        locale_mapping = {
            '繁體中文': 'zh_TW',
            '日文': 'ja_JP',
            '韓文': 'ko_KR',
            '簡體中文': 'zh_CN',
            '法文': 'fr_FR',
            '德文': 'de_DE',
            '越語': 'vi_VN',
        }

        file_path = loadFile_en.get()
        new_locale_value = locale_mapping.get(locale_option_menu.get())

        if file_path and new_locale_value:
            update_locale_settings(file_path, new_locale_value)

    # initialize window
    window = tk.Tk()
    window.title('LOL_Language Changer')
    window.geometry('450x300')
    window.configure(bg='grey50')
    window.resizable(False, False)
    window.iconbitmap('icon.ico')

    # labels
    lb1 = tk.Label(text="檔案路徑", bg="grey25", fg="white", height=1)
    lb1.place(x=15, y=51)

    lb2 = tk.Label(text="選擇語言", bg="grey25", fg="white", height=1)
    lb2.place(x=15, y=81)

    lb3_1 = tk.Label(text="提示訊息", bg="grey25", fg="white", height=1)
    lb3_1.place(x=15, y=111)

    lb3_2 = tk.Label(text=" ", bg="grey50", fg="white", height=1)
    lb3_2.place(x=75, y=111)


    # entry
    loadFile_en = tk.Entry(width=37, font=('Arial 13'))
    loadFile_en.insert(END, "C:\ProgramData\Riot Games\Metadata\league_of_legends.live\league_of_legends.live.product_settings.yaml")
    loadFile_en.place(x=75, y=50)

    # button
    loadFile_btn = tk.Button(text="…", height=1, command=loadFile)
    loadFile_btn.place(x=417, y=50)

    # optionmenu
    locales = [ 
        '繁體中文',
        '日文',
        '韓文',
        '簡體中文',
        '法文',
        '德文',
        '越語'
    ]
    locale_option_menu = ttk.Combobox(
        values = locales,  
        width=8
    )
    locale_option_menu.current(0)
    locale_option_menu.place(x=75, y=81)

    # Save button
    save_btn = tk.Button(text="儲存", height=1, width=5, command=saveLocale)
    save_btn.place(x=200, y=200)

    window.mainloop()

if __name__ == "__main__":
    LOL_LangChanger()
