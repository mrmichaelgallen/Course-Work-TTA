import wx, PythonDrill_PartFour_GUIprogramDB

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None,\
          title=title, size=(800,600))
        panel = wx.Panel(self)
    
        # Creating the menu bar
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")
        
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        
        self.CreateStatusBar()
        
        # Setup Add New Character UI
        # Text at the top
        wx.StaticBox(panel, label='Add a new character', pos=(20,40), size=(280, 190))
        
        # Text for name, gender etc
        wx.StaticText(panel, label='Name:', pos=(30,70))
        wx.StaticText(panel, label='Gender:', pos=(30,110))
        wx.StaticText(panel, label='Age:', pos=(30,150))
        wx.StaticText(panel, label='Occupation:', pos=(30,190))
        
        # Single line text boxes
        self.sName = wx.TextCtrl(panel, size=(150, -1), pos=(130,70))
        self.sGen = wx.TextCtrl(panel, size=(150, -1), pos=(130,110))
        self.sAge = wx.TextCtrl(panel, size=(150, -1), pos=(130,150))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130,190))

        # Save button
        save = wx.Button(panel, label="Add Character", pos=(100, 230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        # Adding character to database
        PythonDrill_PartFour_GUIprogramDB.newCharacter(name, gen, age, occ)
        print PythonDrill_PartFour_GUIprogramDB.viewAll()
        
    def exitProgram(self, event):
        self.Destroy()
    
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()