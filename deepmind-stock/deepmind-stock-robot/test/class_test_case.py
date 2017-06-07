#!/usr/bin/env python
# -*- coding: utf-8 -*-
import types
from types import MethodType
__author__ = 'haipenge'


class Student(object):

	def __init__(self,name,age):
		self.name = name
		self.age = age
	def __str__(self):
		str = 'Name:' + self.name + ',age:'
		return str
	def __repr__(self):
		return 'Student'

	def print_info(self):
		print 'Name is,%s:age is:%s' % (self.name,self.age)


def get_all_properties_of_object(obj):
	properties=dir(obj)
	return properties

#给实例绑定一个方法
def set_age(self,age):
	self.age = age


if __name__ == '__main__':
	std = Student('a',19)
	print std.print_info()
	print 'Is std a instance of Student?',isinstance(std,Student)
	print 'type of student is:',type(std)
	print 'properties of ',Student,get_all_properties_of_object(Student)
	print '测试对像是否有某属性：Stuent is have age:',hasattr(std,'age')
	print '获取对像属性：',getattr(std,'age'),'如果属性不存在，返回默认值：',getattr(std,'age1','404')
	#为实例绑定新方法
	std.set_age = MethodType(set_age,std,Student)
	std.set_age(20)
	print std
	print 'Get new age of std:',std.age
	#给class 绑定方法
	#Student.set_age = MethodType(set_age,None,Student)
	print range[5:10]
