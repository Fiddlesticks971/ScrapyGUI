import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import scrapy

class MainWindow(Gtk.Window):
    
    def __init__(self):
        Gtk.Window.__init__(self,title = "Scrapy Spiders")
        grid = Gtk.Grid()
        #setup basic Spider
        #self.spiders = scrapy.Spider()
        #self.spiders.name = "quotes"
        self.InputUrl = Gtk.Entry()
        self.GoSpiders = Gtk.Button(label = "Send Spiders")
        self.GoSpiders.connect("clicked", self.GoSpiders_Clicked)
        #show where spider has gone
        self.Status = Gtk.ListBox.new()
        
        grid.add(self.InputUrl)
        grid.attach_next_to(self.GoSpiders,self.InputUrl,Gtk.PositionType.RIGHT,1,1)
        grid.attach_next_to(self.Status,self.InputUrl,Gtk.PositionType.BOTTOM,2,1)
        self.add(grid)
        row = Gtk.ListBoxRow()
        testLabel = Gtk.Label("test")
        row.add(testLabel)
        self.Status.add(row)
        
    def GoSpiders_Clicked(self,widget):
        #self.spiders.Request( url = self.InputUrl.get_text(), callback = self.parse )
        print("go spider")
        
    def parse(self,response):
        page = response.url.split("/")[-2]
        row = Gtk.ListBoxRow()
        rowData = Gtk.Label(page + " : " + response.body)
        row.add(rowData)
        self.Status.add(row)
        
        

win = MainWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
