from gestor import gestor

import pysqlite2

print dir(pysqlite2)

a=pysqlite2.__init__('a')

print a

gestordb=gestor('db.txt')

raw=""
while raw!='exit':
    print "\n\ncomands: [add:groupname] [del:groupname] [save] [exit] [sort] [natural sort] [show db] [reload] [delete duplicates] [delete natural duplicates]  [search:text]"
    raw=raw_input('> ')    
    print gestordb.command(raw)
    
if gestordb.need_save:
    raw=raw_input("do you want save? [Yes/no] ")
    if not raw in ['no','n']:
        gestordb.save()
    