def find_page_name(command):
	for row in op('/main/pages').rows():
		if row[0].val in command:
			#print('matched command ', command, ' with name: ', row[0].val)
			return row[0].val
	return 'Disable_All'

def onReplicate(comp, allOps, newOps, template, master):

	i = 0
	for c in newOps:
		c.allowCooking = True
		c.par.display = True
		c.par.alignorder = i
		name = op(template)[i,0].val

		#lookup = find_page_name(name)
		#print('returned page name: ', lookup, 'for command: ', name)
		c.name = name.replace(' ', '_')
		c.par.Widgetlabel = name
		i += 1
