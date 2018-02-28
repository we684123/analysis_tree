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
Default_settree['image_mod']['image_id2'] = str(re)
re = '#'
str(re)
#------------------------------------------------------------------------------
ans = input('是否引入預設檔?(Y/N)\nimport Default.settree?')
if ans == 'y'or ans =='Y':
	print("!!!")
else:
	e = input("無此選項，請按任一鍵離開")
	exit
#-------------------------------------------------------------------------------
import os


getlistdir = os.listdir(os.getcwd())
os.getcwd()
type(getcwd)
#3333333
get_specified_Filename_Extension(getlistdir)
get_specified_Filename_Extension(getlistdir,'.settree')
yy = get_specified_Filename_Extension(getlistdir,'.settree')
yy



gSFE[0][0]
gSFE[1]
#-------------------------------------------------------------------------------
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
			#終於讀到了QWQ，接下來進入處理資料的部分
		except Exception as e:
			print("	elif type(ans) == 'int': ERROR")
			print(e)
	else:
		print(ans)
		print('輸入錯誤!')
