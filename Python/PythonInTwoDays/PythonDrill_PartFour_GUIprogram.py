import wx, PythonDrill_PartFour_GUIprogramDB

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(800,600))
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
        self.sAge = wx.SpinCtrl(panel, value='0', pos=(130, 150), size=(70,25))
        self.sOcc = wx.TextCtrl(panel, size=(150, -1), pos=(130,190))

        # Save button
        save = wx.Button(panel, label="Add Character", pos=(100, 230))
        save.Bind(wx.EVT_BUTTON, self.addCharacter)

        # Setup the Table UI
        # Setup table as listCtrl
        self.listCtrl = wx.ListCtrl(panel, size=(400,400), pos=(350, 40), style=wx.LC_REPORT | wx.BORDER_SUNKEN)

        # Add columns to listCtrl
        self.listCtrl.InsertColumn(0, "ID")
        self.listCtrl.InsertColumn(1, "Name")
        self.listCtrl.InsertColumn(2, "Gender")
        self.listCtrl.InsertColumn(3, "Age")
        self.listCtrl.InsertColumn(4, "Occupation")


    def addCharacter(self, event):
        name = self.sName.GetValue()
        gen = self.sGen.GetValue()
        age = self.sAge.GetValue()
        occ = self.sOcc.GetValue()

        # Checking if variables have a value
        if (name == '') or (gen == '') or (age == '') or (occ == ''):
            # Alert user that a variable is empty
            dlg = wx.MessageDialog(None, 'Some character details are missing. Enter values in each text box.', 'Missing Details', wx.OK)
            dlg.ShowModal()
            dlg.Destroy
            return False

        # Adding character to database
        PythonDrill_PartFour_GUIprogramDB.newCharacter(name, gen, age, occ)
        print PythonDrill_PartFour_GUIprogramDB.viewAll()

        # Empty text boxes when finished
        self.sName.Clear()
        self.sGen.Clear()
        self.sOcc.Clear()
        self.sAge.SetValue(0)

        # Update list control
        self.fillListCtrl()

        
    def exitProgram(self, event):
        self.Destroy()

    def fillListCtrl(self):
        # Get data from the database
        allData = PythonDrill_PartFour_GUIprogramDB.viewAll()

        # Append data to the table
        for row in allData:
            # Loop through and append data
            self.listCtrl.Append(row)
    
app = wx.App()
frame = Frame("Python GUI")
frame.Show()
app.MainLoop()