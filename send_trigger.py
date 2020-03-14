import json

payload = {}
payload['page'] = parent().parent().digits 
payload['label'] = parent().par.Widgetlabel.eval()


msg = {
	'topic' : 2,
	'payload' : json.dumps(payload)
}

print('sending: ', json.dumps(msg))
op('/main/udp_out').send(json.dumps(msg))