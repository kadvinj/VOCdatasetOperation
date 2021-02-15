#----------------------------------------------------------------------#
#   验证集的划分在train.py代码里面进行
#   test.txt和val.txt里面没有内容是正常的。训练不会使用到。
#----------------------------------------------------------------------#
import os
import random 
random.seed(0)

xmlfilepath=r'./Annotations'
saveBasePath=r"./ImageSets/Main/"
 
#----------------------------------------------------------------------#
#   想要增加测试集修改trainval_percent
#   
#   trainval是train+val。一般我们会将val全部用于训练，就相当于用trainval来训练,然后用val调整。 train_percent = 1
#   另一种方式是用train来训练，val是用于训练过程中的验证，test用于训练结束后的模型评估 train_percent = 0.6
#   方式2： 比例： trainval_persent =  train_percent = 0.8，则train:val:test = 0.64:0.16:0.2 
#   trainval_persent决定测试集数量，train_percent决定验证集数量，因为train_percent是占trainval的比例，0.8*0.8=0.64train占总数据的0.64
#----------------------------------------------------------------------#
trainval_percent=1
train_percent=0.8

temp_xml = os.listdir(xmlfilepath)
total_xml = []
for xml in temp_xml:
    if xml.endswith(".xml"):
        total_xml.append(xml)

num=len(total_xml)  
list=range(num)  
tv=int(num*trainval_percent)  
tr=int(tv*train_percent)  
trainval= random.sample(list,tv)  
train=random.sample(trainval,tr)  
 
print("train and val size",tv)
print("train size",tr)
ftrainval = open(os.path.join(saveBasePath,'trainval.txt'), 'w')  
ftest = open(os.path.join(saveBasePath,'test.txt'), 'w')  
ftrain = open(os.path.join(saveBasePath,'train.txt'), 'w')  
fval = open(os.path.join(saveBasePath,'val.txt'), 'w')  
 
for i  in list:  
    name=total_xml[i][:-4]+'\n'  
    if i in trainval:  
        ftrainval.write(name)  
        if i in train:  
            ftrain.write(name)  
        else:  
            fval.write(name)  
    else:  
        ftest.write(name)  
  
ftrainval.close()  
ftrain.close()  
fval.close()  
ftest .close()
