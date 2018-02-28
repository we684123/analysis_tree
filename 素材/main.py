import json
ans = input('是否引入預設檔?(Y/N)\nimport Default.settree?')
if ans == ('y'or'Y'):
	try:
		import 'Default.settree'
	except Exception as e:
		print('預設檔遺失')
		print('Default.settree is miss')
		print('是否建立新設定檔?(Y/N)\n"N"則離開\n')
		print('creat a new Default.settree?(Y/N)\n"N" is exit')
		ans2 = input()
		if ans2 == ('y'or'Y'):
			creat_default()
		else:
			e = input("無此選項，請按任一件離開")
			exit
elif ans == ('n' or 'N'):
	print("請創立新設定檔! 030...")
	creat_default()
else:
	e = input("無此選項，請按任一件離開")
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
		'slice_chat':slice_chat,
		'label_format':label_format,
		'argument_area':argument_area,
		'argument_slice_chat':argument_slice_chat
	}
	f = open('Default.settree','w')
	i = f.write(json.dumps(Default_settree))
	if i == 0 :
		print("opss... 資料沒有寫入，請關掉程式後檢查bug")
	else:
		print("====================")
		print("定義圖示設定，預設皆'null'(不匹配)，請看圖後輸入圖示編號和正則式")
		print("set image format,Default all is 'null',plz look '流程圖.png' ")
		print("after that, input image id and key in Regular Expression")
		print("-----")
		while 1:
			print("請輸入圖形id，或輸入'E'離開")
			image_id = input("input image_id or 'E' to exit")
			if image_id == 'E':
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
