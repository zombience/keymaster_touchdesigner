def onReplicate(comp, allOps, newOps, template, master):
	i = 0
	for c in newOps:
		c.name = op(template)[i,0].val + '_' + str(i)
		c.allowCooking = True
		print('generating page container: ', c.name)
		c.op('populate_triggers').run()
		i += 1
