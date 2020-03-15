def onReplicate(comp, allOps, newOps, template, master):
	i = 0
	for c in newOps:
		c.name = op(template)[i,0].val
		c.allowCooking = True
		c.op('page_index').par.value0 = i
		print('generating page container: ', c.name)
		c.op('populate_triggers').run()
		i += 1
