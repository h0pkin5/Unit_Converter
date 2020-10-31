from converter import Converter, MASS_UNITS, LENGTH_UNITS, SQUARED_UNITS
import tkinter as tk
from tkinter import ttk, messagebox


class MainWindow(tk.Frame):
    
    def __init__(self, master):
        tk.Frame.__init__(self, master=master)

        self.mass_converter = Converter('gramm', MASS_UNITS)
        self.length_converter = Converter('meter', LENGTH_UNITS)
        self.square_converter = Converter('square meter', SQUARED_UNITS)

        self.active_converter = self.mass_converter

        self.conversion_mode_label = tk.Label(self, text='Converter', font='Verdana 14 bold')
        self.conversion_mode_combo = ttk.Combobox(self, values=['Mass', 'Length', 'Squared'])
        self.conversion_mode_combo.current(0)
        self.conversion_mode_combo.bind('<<ComboboxSelected>>', self.selectConversionMode)

        
        self.unit_to_convert_from_label = tk.Label(self, text='From:', font='Verdana 14 bold')
        self.unit_to_convert_from_combo = ttk.Combobox(self, values=self.active_converter.unit_list)
        self.unit_to_convert_from_combo.current(0)
        
        self.input_label = tk.Label(self, text='Input:', font='Verdana 14 bold')
        self.value_entry = tk.Entry(self)
        
        self.unit_to_convert_to_label = tk.Label(self, text='To:', font='Verdana 14 bold')
        self.unit_to_convert_to_combo = ttk.Combobox(self, values=self.active_converter.unit_list)
        self.convert_btn = tk.Button(self, text='Convert', command=self.convert)
        self.result_label_label = tk.Label(self, text='Result: ', font='Verdana 14 bold')
        self.result_label = tk.Label(self, text='0.00')

        self.conversion_mode_label.grid(row=0,column=0)
        self.unit_to_convert_from_label.grid(row=1, column=0)
        self.unit_to_convert_to_label.grid(row=2, column=0)
        self.input_label.grid(row=3, column=0)
        self.result_label_label.grid(row=4, column=0)
        self.result_label.grid(row=4, column=1)

        self.value_entry.grid(row=3, column=1)
        self.convert_btn.grid(row=4, column=2)

        self.conversion_mode_combo.grid(row=0, column=1)
        self.unit_to_convert_from_combo.grid(row=1, column=1)
        self.unit_to_convert_to_combo.grid(row=2, column=1)

    def selectConversionMode(self, event):
        if self.conversion_mode_combo.get() == 'Mass':
            self.active_converter = self.mass_converter
            self.unit_to_convert_to_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo.current(0)
            self.unit_to_convert_from_combo.current(0)
        
        elif self.conversion_mode_combo.get() == 'Length':
            self.active_converter = self.length_converter
            self.unit_to_convert_to_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo.current(0)
            self.unit_to_convert_from_combo.current(0)
        
        elif self.conversion_mode_combo.get() == 'Squared':
            self.active_converter = self.square_converter
            self.unit_to_convert_to_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo['values'] = self.active_converter.unit_list
            self.unit_to_convert_from_combo.current(0)
            self.unit_to_convert_from_combo.current(0)

    def convert(self):
        try:
            value = float(self.value_entry.get())
        except:
            tk.messagebox.showerror(title='Value Error', message='You entered a value that is not a number')
        
        if self.unit_to_convert_from_combo.get() == self.active_converter.base_unit:
            result = self.active_converter.convertFromBase(value, self.unit_to_convert_to_combo.get())
        
        elif self.unit_to_convert_from_combo.get != self.active_converter.base_unit and self.unit_to_convert_to_combo.get() == self.active_converter.base_unit:
            result = self.active_converter.convertToBase(value, self.unit_to_convert_from_combo.get())
        
        elif self.unit_to_convert_from_combo.get() != self.active_converter.base_unit and self.unit_to_convert_to_combo.get() != self.active_converter.base_unit:
            result = self.active_converter.convertNoneBase(value, self.unit_to_convert_from_combo.get(), self.unit_to_convert_to_combo.get())

        self.result_label['text'] = str(result)


def main():
    root = tk.Tk()
    MainWindow(master=root).pack()
    root.title('Unit Converter')
    root.mainloop()


if __name__ == '__main__':
    main()



