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
		c.name = op(template)[i,0].val
		c.allowCooking = True
		c.op('page_index').par.value0 = i
		print(f'{i} set page index to {c.op("page_index").par.value0}')
		c.par.clone = comp.par.master
		print('generating page container: ', c.name)
		
		i += 1
