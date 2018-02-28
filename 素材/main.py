import json
ans = input('是否引入預設檔?(Y/N)\nimport Default.settree?')
if ans == 'y'or ans =='Y':
	try:
		f = open('Default.settree','r+',encoding = 'utf8')
		t = f.read()
		f.close()
		Default_settree = json.loads(t)
		print("讀取 Default.settree 完成!")
	except Exception as e:
		print('預設檔遺失')
		print('Default.settree is miss')
		print('是否建立新設定檔?(Y/N)\n"N"則離開\n')
		print('creat a new Default.settree?(Y/N)\n"N" is exit')
		ans2 = input()
		if ans2 == ('y'or'Y'):
			creat_default()
		else:
			e = input("無此選項，請按任一鍵離開")
			exit
elif ans == 'n'or ans =='N':
	print("請創立新設定檔! 030...")
	creat_default()
else:
	e = input("無此選項，請按任一鍵離開")
	exit
#------------------------------------------------------------------------------
def creat_default():
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
	f.close()
	if i == 0 :
		print("opss... analysis_mod資料沒有寫入，請關掉程式後檢查bug")
	else:
		print("====================")
		print("定義圖示設定(image_mod)，預設皆'null'(不匹配)，請看圖後輸入圖形'群組及名稱'和'正則式'")
		print("set image format(image_mod),Default all is 'null',plz look '流程圖.png' ")
		print("after that, input image Group name and image name and Regular Expression")
		print("-----")
		while 1:
			print("請輸入圖形群組及名稱(EX: flowchart.start1)，或輸入'E'離開")
			image_id = input("input image Group and name(EX: flowchart.start1) or 'E' to exit")
			if image_id == 'E':
				e = input("所有動作停止，請按任一鍵離開")
				exit
				break
			print("請輸入正則式")
			re = input("input re")
			e = set_image_REformat(image_id,re)
			print(e)
		print("設定檔建立完成!")
		print("Default.settree is Created!")
	#rectangle = input("矩形(rectangle)對應正則(re)")
#------------------------------------------------------------------------------
def set_image_REformat(image_id,re):
	f = open('Default.settree','r+',encoding = 'utf8')
	t = f.read()
	f.close()
	Default_settree = json.loads(t)
	try:
		Default_settree['image_mod'][image_id] = str(re)
		return("改寫成功")
	except Exception as e:
		return e
