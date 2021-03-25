# td module autocomplete 
# these imports are only needed for auto-complete in VSCode IDE, they have no impact on code execution

# read more here: https://medium.com/@tekt/improving-python-development-for-touchdesigner-5f60d6bafe31
# https://github.com/optexture/td-components/tree/master/lib/_stubs

try:
	TDF = op.TDModules.mod.TDFunctions
except NameError:
	from _stubs import TDFunctions as TDF
	pass

import json
import os.path

class KeyMaster:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		
		if not os.path.isfile(self.paramsDat.par.file.val):
			self.paramsDat.save(self.paramsDat.par.file.val)

	@property
	def CommandMapFile(self) -> str:
		'''
		the json file containing command map 
		'''
		return self.paramsDat['File', 1].val

	@CommandMapFile.setter
	def CommandMapFile(self, val: str) -> None:
		self.paramsDat['File', 1].val = val

	@property
	def Commands(self): #-> tableDAT
		return self.ownerComp.op('commands')

	@property
	def rawJSON(self) -> str:
		return self.ownerComp.op('json_file').text

	@property
	def TargetIP(self) -> str:
		return self.paramsDat['TargetIP', 1].val

	@TargetIP.setter
	def TargetIP(self, val) -> str:
		self.paramsDat['TargetIP', 1] = val

	@property
	def Port(self) -> int:
		return self.paramsDat['Port', 1].val

	@Port.setter
	def Port(self, val: int) -> None:
		self.paramsDat['Port', 1].val = val

	@property
	def udpDAT(self): # -> udpoutDAT
		return self.ownerComp.op('udp_out')

	@property
	def pagegenerator(self): #-> replicatorCOMP
		return op('/main/page_selector/selector_generator')

	@property
	def paramsDat(self): # -> tableDAT
		return self.ownerComp.op('params_file')

	@property
	def pageIndex(self): # -> tableDAT
		'''
		in unity, page definitions are enums
		which, under the hood, are ints. in order
		to send a properly serialized message, pages must
		be sent as int, not as string
		use this table to convert name to int

		pagenames include 'none' as 0, which is 
		accounted for in eval by adding 1 to rownum
		'''
		return self.ownerComp.op('pageindex')

	def SelectFile(self) -> None: 
		'''
		open os UI to select command map file
		'''
		self.CommandMapFile = ui.chooseFile(fileTypes=['json'], title=f'select CommandMap file')

	def ParseCommands(self, txt: str = None) -> None:
		'''
		handle loaded textfile as json
		extract pages and commands to populate both 
		page and command table dats for replicators
		'''
		if txt is None:
			txt = self.rawJSON
		
		obj = json.loads(txt)

		self.Commands.clear()
		for item in obj:
			entries = ','.join(obj[item])
			self.Commands.appendRow([item, entries])

		self.pagegenerator.par.recreateall.pulse()

	def SendCommand(self, page: str, label: str) -> None:
		'''
		individual buttons will send their label and key
		bundle it to json and send via UDP
		'''
		obj = {
			'pagename':page,
			'label':label
		}
		print('sending obj: ', obj)
		self.udpDAT.send(json.dumps(obj))