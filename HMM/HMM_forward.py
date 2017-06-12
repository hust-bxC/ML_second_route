# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:44:38 2017

@author: rogue
"""

from numpy import *

class HMM:

	def __init__(self):
		self.A=array([(0.5,0.2,0.3),(0.3,0.5,0.2),(0.2,0.4,0.2)])
		self.B=array([(0.1,0.9),(0.4,0.6),(0.7,0.3)])
		self.pi=array([(0.2),(0.4),(0.4)])
		self.o=[0,1,0]
		self.t=len(self.o)#观测序列长度
		self.m=len(self.A)#状态集合个数
		self.n=len(self.B[0])#观测集合个数

	def forward_algorithm(self):
		#t时刻部分观测序列为o1,o2,ot,状态为qi的概率用矩阵x表示，
		#则矩阵大小行数为观测序列数，列数为状态个数
		self.x=array(zeros((self.t,self.m)))
		#先计算出时刻1时，观测为o1,状态为qi的概率
		for i in range(self.m):
			self.x[0][i]=self.pi[i]*self.B[i][self.o[0]]
		for j in range(1,self.t):
			for i in range(self.m):
				#前一时刻所有状态的概率乘以转移概率得到i状态概率
				#i状态的概率*i状态到j观测的概率
				temp=0
				for k in range(self.m):
					temp=temp+self.x[j-1][k]*self.A[k][i]
				self.x[j][i]=temp*self.B[i][self.o[j]]
		result=0
		for i in range(self.m):
			result=result+self.x[self.t-1][i]
		print ("前向概率矩阵及当前观测序列概率如下：",'\n',self.x,'\n',result)
		

		
if __name__ == '__main__':
	test=HMM()
	test.forward_algorithm()
	