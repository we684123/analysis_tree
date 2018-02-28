import json
print("定義分離字元")
slice_chat = input("set slice chat")
print("定義標籤格式")
label_format = input("set label format")
print("定義引數區域")
argument_area = input("set argument area")
print("定義引數分離字元")
argument_slice_chat = input("set argument slice chat")
Default_settree = {
	'analysis_mod':{
		'slice_chat':slice_chat,
		'label_format':label_format,
		'argument_area':argument_area,
		'argument_slice_chat':argument_slice_chat
	},
	'iagme_mod':{}
}
f = open('Default.settree','w')
i = f.write(json.dumps(Default_settree))
i
#------------------------------------------------------------------------------
f = open('Default.settree','r+',encoding = 'utf8')
t = f.read()
e = json.dumps(t)
type(t)
path(t)
e
j = json.loads(t)
j
Default_settree = json.loads(t)
t
Default_settree['']
