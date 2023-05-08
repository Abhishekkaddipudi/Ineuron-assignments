import docx2txt
import os
class readdoc:
    def __init__(self,filePath=''):
        self.filePath=filePath
        if not os.path.exists(filePath):
            raise FileNotFoundError
    
    def read_with_h2(self):      
        my_text = docx2txt.process(self.filePath)
        list1=my_text.split("\n\n")
        print("<h2>"+"</h2>\n<h2>".join(list1)+"</h2>")