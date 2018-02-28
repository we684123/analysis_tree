import json
import re
import os
from ppint import pprint
main()
#------------------------------------------------------------------------------
def main():
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
		getlistdir = os.listdir(os.getcwd())
		gSFE = get_specified_Filename_Extension(getlistdir,'.settree')
		if gSFE == '':
			print("請創立新設定檔! 030...")
			creat_default()
		else:
			print('---可用的 .settree 檔如下---')
			for i in range(0,len(gSFE[0])) :
				print(str(gSFE[1][i])+ ". " + str(gSFE[0][i]))
			print('---------------------------\n')
			print("請問要套用哪個設定檔?")
			ans = input('請輸入檔案前方編號以選用，或輸入"N"創建新設定檔，或輸入"E"離開程式)')
			if ans == 'N' or ans == 'n':
				print("請創立新設定檔!")
				creat_default()
			elif ans == 'E' :
				exit
			elif type(int(ans)) == type(1):  #
				try:
					f = open(str(gSFE[0][int(ans)-1]),'r+',encoding = 'utf8')
					t = f.read()
					f.close()
					Default_settree = json.loads(t)
					print("讀取 " + str(gSFE[0][int(ans)-1]) +" 完成!")
				except Exception as e:
					print("	elif type(ans) == 'int': ERROR")
					print(e)
			else:
				print(ans)
				print('輸入錯誤!')
	else:
		e = input("無此選項，請按任一鍵離開")
		exit
	pass
#-------------------------------------------------------------------------------
def get_specified_Filename_Extension(array,specified_FE='null'):
	#顯示當前資料夾內容,如有指定副檔名會塞選
	#print("in get_specified_Filename_Extension")
	#print(array)
	#print(specified_FE)
	File_list = []
	File_id_list = []
	n = int(len(array))
	if specified_FE == 'null':
		for i in range(0,n):
			j = str(array[i])
			#print(j)
			File_list.append(j)
			File_id_list.append(int(i))
			#print(array[i])
	else:
		for i in range(0,n):
			if specified_FE in array[i]:
				#這裡有個bug 就是名子可以"123.gh.png" 中塞選條件 ".gh" 也過關
				#但我就不修了，目前對我來說夠用，為了先達成最小可行性。哪天有空再說
				j = str(array[i])
				#print(j)
				File_list.append(j)
				File_id_list.append(int(i))
	return [File_list,File_id_list]
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
			if e != '改寫成功':
				print('輸入錯誤 請查明後再撥')
			print(e)
		print("設定檔建立完成! Default.settree is Created!")
#------------------------------------------------------------------------------
def set_image_REformat(image_id,re):
	f = open('Default.settree','r+',encoding = 'utf8')
	t = f.read()
	f.close()
	Default_settree = json.loads(t)
	try:
		k = Default_settree['image_mod'][image_id]
		Default_settree['image_mod'][image_id] = str(re)
		f = open('Default.settree','w+',encoding = 'utf8')
		i = f.write(json.dumps(Default_settree))
		f.close()
		print("before re:")
		print(k)
		print("after re:")
		print(Default_settree['image_mod'][image_id])
		return("改寫成功")
	except Exception as e:
		return e
#-------------------------------------------------------------------------------
def find_get(txt,st,ed):
	try:
		txt = str(txt)
		a = txt.index(st)
		g = txt[a:]
		b = g.index(ed)
		c = len(st)
		ans = g[c:b]
		return ans
	except Exception as e:
		return e
#-------------------------------------------------------------------------------
