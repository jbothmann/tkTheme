import tkinter as tk

#class Theme, which holds values for the colors and that the program should use for all widgets.  Default values approximate Tkinter defaults.
class Theme:
	#default values
	title = "default theme"
    bg = "#F0F0F0" #gray94%
    fg = "black"
    contrastbg = "white"
    contrastfg = "black"
    selectbg = "#0078D7" #default blue highlight
    selectfg = "white"
    contrastselectbg = "#0078D7" #default blue highlight
    contrastselectfg = "white"

    #static function that determines if the given string represents a valid color
    def Color(color):
    	return color


    def __init__(self, title="Default Gray", bg="gray95", fg="black", contrastbg="white", contrastfg="black", selectbg="#0078D7", selectfg="white", contrastselectbg="#00a2ed", contrastselectfg="white"):
        #inititalize theme title
        if isinstance(title, str):
        	self.title = title
        else:
        	self.title = Theme.title

        #inititalize values
        self.bg = bg #colors to be used for most elements
        self.fg = fg
        self.contrastbg = contrastbg #colors to be used for elements that need to stand out from the background
        self.contrastfg = contrastfg
        self.selectbg = selectbg #colors used when highlighting text
        self.selectfg = selectfg
        self.contrastselectbg = contrastselectbg #colors used when highlighting text on contrast element
        self.contrastselectfg = contrastselectfg

    #Theme.apply, passing this method a common widget will automatically reconfigure its color and font to fit the theme
    def apply(self, widget):
        if isinstance(widget, list):  #if passed a list of widgets, recursively handle all widgets
            for oo in widget:
                self.apply(oo)
        if isinstance(widget, tk.Tk) or isinstance(widget, tk.Toplevel):
            widget.config(bg=self.bg)
        elif isinstance(widget, tk.Frame):
            widget.config(bg=self.bg)
        elif isinstance(widget, tk.LabelFrame):
            widget.config(bg=self.bg, fg=self.fg, font=(self.font, self.fontSize+2))
        elif isinstance(widget, tk.Label):
            widget.config(bg=self.bg, fg=self.fg, font=(self.font, self.fontSize))
        elif isinstance(widget, tk.Button) or isinstance(widget, tk.Menubutton):
            widget.config(bg=self.bg, fg=self.fg, activebackground=self.bg, activeforeground=self.fg, font=(self.font, self.fontSize))
        elif isinstance(widget, tk.Entry):
            widget.config(bg=self.contrastbg, fg=self.contrastfg, selectbackground=self.contrastselectbg, selectforeground=self.contrastselectfg, font=(self.font, self.fontSize))
        elif isinstance(widget, SelectLabel): #This conditional must come before Text, because SelectLabel extends Text
            widget.config(bg=self.bg, fg=self.fg, selectbackground=self.selectbg, selectforeground=self.selectfg, font=(self.font, self.fontSize))
        elif isinstance(widget, tk.Text):
            widget.config(bg=self.contrastbg, fg=self.contrastfg, selectbackground=self.contrastselectbg, selectforeground=self.contrastselectfg, font=(self.font, self.fontSize))
        elif isinstance(widget, tk.Checkbutton) or isinstance(widget, Radiobutton):
            widget.config(bg=self.bg, fg='black', activebackground=self.bg, activeforeground=self.bg, font=(self.font, self.fontSize))
        elif isinstance (widget, tk.Menu):
            widget.config(bg=self.contrastbg, fg=self.contrastfg, activebackground=self.contrastselectbg, activeforeground=self.contrastselectfg, disabledforeground=None, font=(self.font, self.fontSize))
        return widget

class ThemeAndFont:
    __init__(self, theme = None, font = None):
    	if isinstance(theme, Theme):
    		self.theme = theme
    	else:
    		self.theme = Theme()

    	if isinstance(font, tk.font.Font):
    		self.font = font
    	else:
    		self.font = tk.font.Font()
