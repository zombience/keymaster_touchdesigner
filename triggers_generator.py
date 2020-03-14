def onReplicate(comp, allOps, newOps, template, master):

	i = 0
	for c in newOps:

		c.allowCooking = True
		c.par.display = True

		triggername = op(template)[i,0].val
		if triggername is None or triggername is '' or triggername.startswith('_'):
			continue
			
		c.name = triggername.replace(' ', '_')
		c.par.Widgetlabel = triggername

		i += 1
