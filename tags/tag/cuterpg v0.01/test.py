from table import table
from db import Database

DB=Database()

DB.create_new_table('tabla_comun',['al','b','s'])

table=DB['tabla_comun']

#table=table(['al','b','s'])

table.add('gs','dsg','90avo8a0987sdgsdg')
table.add('s','yrmry','908afsfas0987sdgsdgsd')
table.add('tgwg','5','908afa0f987gyglglhuho87gl')
table.add('s','3agsndtsrh4wse','908a0sfsaa987')
table.add('s',5,'ee')
table.add('s','asgasgag52','ee')
table.add('ssdgssafsavasbafawge',5,'ee')
table.add('s',5,'eeqasgfa')
table.add('s',table,__import__('coloreado'))

print table

print "-"

print table.get_row(2)



print "_-------_"
print '\nresultado de la consulta: \n' + str(table.get('al','s','s','ee'))
print '\nresultado de la consulta: \n' + str(table.get())

table.get('al','s','s','ee')[0][1]='t'#la tabla ha cambiando
print '\nresultado de la consulta: \n' + str(table.get('al','s','s','ee'))

#a = raw_input('\npresione enter para salir')
