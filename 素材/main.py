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
			pass

def creat_default():
	print("定義分離字元")
	slice_chat = input("set slice chat")
	print("定義標籤格式")
	slice_chat = input("set slice chat")
	print("定義引數區域")
	slice_chat = input("set slice chat")
	print("定義引數分離字元")
	slice_chat = input("set slice chat")
	print("定義分離字元")
	slice_chat = input("set slice chat")
