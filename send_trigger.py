import json

payload = {}
# +2: 
# this is a super annoying inconsistency, but
# ControlPage enum in unity begins with 
# None = 0
# PageSelection = 1
# so those two get ignored from the count
# since the other two do not make it to the population table, 
# the 'page' index which ends up being translated in unity as 
# the control page enum value MUST be offset by 2 to account for this
# so, never remove None and PageSelection as the first two enum vals
payload['page'] = int(op('../page_index')[0] + 2) 
payload['label'] = parent().par.Widgetlabel.eval()


msg = {
	'topic' : 1,
	'payload' : json.dumps(payload)
}

print('sending: ', json.dumps(msg))
op('/main/udp_out').send(json.dumps(msg))