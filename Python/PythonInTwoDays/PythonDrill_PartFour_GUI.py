##########
########## Testing GUI
##########

# import wx
#
# appVar = wx.App()
# frameVar = wx.Frame(None, title="Python GUI", size=(300,200))
# frameVar.Show()
# appVar.MainLoop()

##########
########## Testing GUI
##########

# import wx
#
# class Frame(wx.Frame):
#     def __init__(self, title):
#         wx.Frame.__init__(self, None, title=title, size=(300,200))
#         panel = wx.Panel(self)
#
#         button = wx.Button(panel,label="Exit",size=(100,40),pos=(100,30))
#         # Bind button event to the function self.exit
#         button.Bind(wx.EVT_BUTTON, self.exit)
#
#         # Create menu bar
#         menuBar = wx.MenuBar()
#
#         # Create the menus
#         fileMenu = wx.Menu()
#         editMenu = wx.Menu()
#
#         menuBar.Append(fileMenu, "File")
#         menuBar.Append(editMenu, "Edit")
#
#         #Add items to fileMenu
#         fileMenu.Append(wx.NewId(), "New File", "Create a new file")
#         fileMenu.Append(wx.NewId(), "Open", "Open")
#         exitItem = fileMenu.Append(wx.NewId(), "Exit", "Exit"
#
#         self.SetMenuBar(menuBar)
#         self.CreateStatusBar()
#
#         # Bind exit menu item to exit function
#         self.Bind(wx.EVT_MENU, self.exit, exitItem)
#
#     def exit(self, event):
#         self.Destroy()
#
# app = wx.App()
# frame = Frame("Python GUI")
# frame.Show()
# app.MainLoop()

##########
########## Testing GUI
##########

# import wx
#
# class Frame(wx.Frame):
#     def __init__(self, title):
#         wx.Frame.__init__(self, None,\
#           title=title, size=(300,250))
#         panel = wx.Panel(self)

        ## Static Text
        # wx.StaticText(panel, label='Single line', pos=(100,100))

        # # Static Box
        # wx.StaticBox(panel, label="Static Box Title", pos=(10,10), size=(265,190))
        # wx.StaticText(panel, label='Single line', pos=(100,100))

        # ## Combo Box
        # simpsons=['Bart', 'Lisa', 'Maggie', 'Marge', 'Homer']
        # CB = wx.ComboBox(panel, pos=(100, 50), choices=simpsons, style = wx.CB_READONLY)

        # ## Check Box
        # wx.CheckBox(panel, label='Male', pos=(100,50))
        # wx.CheckBox(panel, label='Female', pos=(100,80))

        # ## Radio Button
        # wx.RadioButton(panel, label='Male', pos=(100,50))
        # wx.RadioButton(panel, label='Female', pos=(100,80))

        # ## Text Control
        # wx.TextCtrl(panel, size=(200, -1), pos=(50,30))
        # wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(200, 100), pos=(50, 80))

        # ## Spin Control
        # wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70,25))

    #     ## Spin Control
    #     sc = wx.SpinCtrl(panel, value='0', pos=(130, 50), size=(70,25))
    #     self.valueText = wx.StaticText(panel, label='', pos=(130, 80))
    #
    #     sc.Bind(wx.EVT_SPINCTRL, self.spinControl)
    #
    # def spinControl(self, event):
    #     # Get spin control value
    #     value = event.GetInt()
    #     # Update static text
    #     self.valueText.SetLabel(str(value))

# app = wx.App()
# frame = Frame("wxPython Widgets!")
# frame.Show()
# app.MainLoop()




