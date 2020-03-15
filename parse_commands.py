import json

raw_text = op('null_command_map').text

def parse_commands():
	obj = json.loads(raw_text)

	objs = obj['jsonTokens']
	kvp = {}
	pages = {}
	for item in objs:
		if item['page'] == 'PageSelection':
			pages = [p.replace('Control Page ', '') for p in item['labels']]
		else:
			kvp[item['page']] = item['labels']
	
	
	

	op('pages').clear()
	op('commands').clear()
	for p in pages:
		if p in kvp:
			op('pages').appendRow(p)
			op('commands').appendRow(kvp[p])

	op('page_selector/selector_generator').allowCooking = True
	op('page_selector/selector_generator').par.recreateall.pulse()
	
if len(raw_text) < 1:
	print('failed to load json command file')
	pass

else:
	parse_commands()





	