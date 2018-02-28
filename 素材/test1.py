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
	'image_mod':{
		'flowchart.start1':'null',
		'flowchart.start2':'null',
		'flowchart.terminator':'null',
		'flowchart.process':'null',
		'flowchart.predefinedProcess':'null',
		'flowchart.decision':'null',
		'flowchart.loopLimit':'null',
		'flowchart.loopLimitEnd':'null',
		'flowchart.document':'null',
		'flowchart.data':'null',
		'flowchart.directData':'null',
		'flowchart.storedData':'null',
		'flowchart.sequentialData':'null',
		'flowchart.dataBase':'null',
		'flowchart.internalStorage':'null',
		'flowchart.manualInput':'null',
		'flowchart.card':'null',
		'flowchart.paperType':'null',
		'flowchart.cloud':'null',
		'flowchart.delay':'null',
		'flowchart.display':'null',
		'flowchart.manualOperation':'null',
		'flowchart.preparation':'null',
		'flowchart.onPageReference':'null',
		'flowchart.offPageReference':'null',
		'flowchart.userMessage':'null',
		'flowchart.networkMessage':'null',
		'flowchart.annotation':'null'
	}
}
f = open('Default.settree','w+',encoding = 'utf8')
i = f.write(json.dumps(Default_settree))
i

f.close()
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
Default_settree['image_mod']['flowchart.userMessage']
image_id = 'flowchart.userMessage'
Default_settree['image_mod'][image_id] = str(re)
re = '#'
str(re)
#------------------------------------------------------------------------------
