import os
import weasyprint
with open(os.path.join(os.path.dirname(__file__), 'test.html'), 'r+') as file:
    t = file.read()
weasyprint.HTML(string=t.encode('utf-8')).write_pdf('test.pdf')