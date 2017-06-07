# -*- coding: utf-8 -*-
# hello.py
import sys
import math
import os
print 'hello world!'
print 'The quick brown fox', 'jumps over', 'the lazy dog'
print 100 + 200
#交互式输入
name = raw_input('please enter your name:')
print 'hello,',name
#编写打印标签
def line(desc='学习'):
	type = sys.getfilesystemencoding()
	i = 0
	print i
	str = ''
	while i < 30:
	    str += '-'
	    i = i + 1
	    if i == 15:
	        str += desc
	print i,str.decode('utf-8').encode(type)
###########################################
#Start to lean use list
line('Data Struct:List')
test_list = ['a','b','c']
print 'print list element :', test_list
print 'list length is:',len(test_list)
#切片
test_list_sub=test_list[0:2]
print 'test list sub is:',test_list_sub,test_list[:2]
print 'To got first ele of list by index:',test_list[0]
test_list[1] = 'x'
print 'Reset ele of list:'
print test_list
test_list_range = range(1,10)
print 'range list:',test_list_range
test_list_range_compute = [x*x for x in range(1,10) if x%2 == 0]
print 'comput range :',test_list_range_compute
#生成两个字母的全排列
test_list_range_char = [m + n for m in 'ABC' for n in 'XYZ']
print test_list_range_char
#列出目录下的所有文件和目录
test_file_list = [d for d in os.listdir('.')]
print 'file list is :',test_file_list


############################################
#元组tupple
line('Data Struct:tuple')
test_tupple = ('1','2','3')
#不能改变
print 'tupple ele is:',test_tupple
print 'Get first ele:',test_tupple[0]
#只有1个元素的tuple定义时必须加一个逗号\',\',来消除歧义
###########################################
#Dic,字典
line('Data Struct:dic')
dic = {'name':'haipenge','age':36}
print dic,'name is:',dic['name']
#对Dic的循环处理
def dic_loop(dic):
	for k,v in dic.iteritems():
		print k,'=',v

print 'dic loop booth key and v:\n',dic_loop(dic)

#添加新数据 
dic['sex'] = '男'
print dic
#判断key是否存在
print 'Key name is Exist:','name' in dic
#返回value
print 'get value of age key:',dic.get('age')
#删除一个KEY
dic.pop('sex')
print 'after remove sex from dic:',dic
########################################
#Set
line('Data Struct:set')
#无重复元素
test_set=set([1,2,3])
print 'set elements is:',test_set
test_set.add(4)
print 'after use .add(),set is:',test_set
test_set.remove(2)
print 'after remove key:',test_set
test_new_set=set([9,1,2])
set_togg = test_set & test_new_set
print 'set togg:',set_togg
set_union = test_set | test_new_set
print 'set union：',set_union
#
print {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}['1']
line('Use abs')
print 'abs(-100) = ',abs(-1000)
line('Use cmp,compare max or min')
print 'cmp(1,2) = ',cmp(1,2),'cmp(2,1) = ',cmp(2,1),'cmp(1,1) = ',cmp(1,1)
#line('数据类型转换')
#print 'int(\'1\') = ' ,int('1'),'int(12.1) = ',int(12.1),'str(12.3) = ',str(12.3),'bool(1) = ',bool(1),'bool(\'\') = ',bool('')

#匿名函数
line('lambada functoin')
print map(lambda x:x+1,[1,2,3,4,5])
#把匿名函数作为返回值返回
def build_lambda_as_return_func(x,y):
    return lambda:x*x + y*y

func_b = build_lambda_as_return_func(2,3)
print func_b()

#空函数
def pop():
    pass

#Pass use
def age(x):
	if x > 18:
		pass

print 'exec pop() :',pop(),'exec age(1):',age(1),'exec age(20):',age(20)

#函数参数检查， isinstance
def my_abs(x):
	if not isinstance(x,(int,float)):
		raise TypeError('bad operand type.only allow int ,float.')
	if x > 0:
		return x
	else:
		return -x

print 'my_abs(1):',my_abs(1),'my_abs(-1):',my_abs(-1),'my_abs(\'a\'):',my_abs(100)

#返回多个值,注：原来返回值是一个tuple
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx,ny

print 'move(1,2,1,10):',move(1,2,1,10)
#map
line('map(fn,[])')
def map_fun(x):
	return x * x

print 'int list 2 squar:',map(map_fun,range(10))
print 'str int list 2 str list :', map(str,range(10))

#reduce:reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#函数f必须接收两个参数
#exam:
def reduce_fun(x,y):
	if x % 2 == 0:
	    return x * 10 +y
	else:
		return 0

print 'reduce(f,[]):',reduce(reduce_fun,range(10))
print 'map and reduce:',reduce(reduce_fun,map(map_fun,range(10)))
#===================filter() 函数======================
line('learn function of \'filter()\'')
def is_feature(x):
	if x % 2 == 1:
		return x
print 'User filter:',filter(is_feature,range(10))

def not_empty(s):
	return s and s.strip()
print 'Use filer check string is empty:',filter(not_empty,['a','','b','C'])
#===================Use sorted=========================
line('sorted')
need_2_sort_list = [5,4,3,0,8,9,11,23,44,24,33]
print 'Before sort :',need_2_sort_list
print 'After sort :',sorted(need_2_sort_list)
def reversed_cmp(x,y):
	if x > y:
		return -1
	if x < y:
		return 1
	if x == y:
		return 0
print 'Use reversed_cmp func,after sorted is:',sorted(need_2_sort_list,reversed_cmp)
neet_2_sort_str_list = ['c','C','A','anc','xY','XYi']
print 'Before str sort:',neet_2_sort_str_list
print 'After str sort:',sorted(neet_2_sort_str_list)
def cmp_ignore_case(s1,s2):
	u1 = s1.upper()
	u2 = s2.upper()
	if u1 < u2:
		return -1
	if u1 > u2:
		return 1
	if u1 == u2:
		return 0
print 'Use cmp_ignore_case sort str list:',sorted(neet_2_sort_str_list,cmp_ignore_case)

#============匿名函数
print (map(lambda x:x * x,range(10)))
lambda_fun = lambda x:x*x
print '将匿名函数赋值给一个变量：',lambda_fun(5)
