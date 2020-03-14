import json

raw_text = op('null_command_map').text

def parse_commands():
	obj = json.loads(raw_text)

	objs = obj['jsonTokens']
	kvp = {}
	pages = {}
	for item in objs:
		if item['page'] == 'PageSelection':
			pages = item['labels']
		else:
			kvp[item['page']] = item['labels']
	
	#print(kvp)
	
			
	op('pages').clear()
	op('pages').appendRows(sorted(kvp))

	op('commands').clear()
	[op('commands').appendRow(kvp[key]) for key in sorted(kvp)]
	
	op('page_selector/page_commands').clear()
	
	pages.sort()
		
	op('page_selector/page_commands').appendRows(pages)
	op('page_selector/selector_generator').allowCooking = True
	op('page_selector/selector_generator').par.recreateall.pulse()

if len(raw_text) < 1:
	print('failed to load json command file')
	pass

else:
	parse_commands()





	