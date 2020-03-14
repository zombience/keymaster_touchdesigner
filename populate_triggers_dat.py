import json

target = op('commands')
target.clear()
[target.appendRow(t[0].val) for t in op('null_commands').rows() if len(t[0].val) > 0]

op('create_buttons').allowCooking = True
op('create_buttons').par.recreateall.pulse()	