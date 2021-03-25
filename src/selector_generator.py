# me - this DAT
# 
# comp - the replicator component which is cooking
# allOps - a list of all replicants, created or existing
# newOps - the subset that were just created
# template - table DAT specifying the replicator attributes
# master - the master operator
#

def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps, newOps, template, master):

	i = 0
	for c in newOps:
		c.allowCooking = True
		c.par.display = True
		c.par.alignorder = i
		name = op(template)[i,0].val

		c.name = name.replace(' ', '_')
		c.par.Widgetlabel = name
		c.par.Index = i
		i += 1