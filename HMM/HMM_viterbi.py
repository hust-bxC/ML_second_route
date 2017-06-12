# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 14:27:58 2017

@author: rogue
"""

from numpy import *

class HMM:

	def __init__(self):
		self.A=array([(0.4,0.3,0.3),(0.3,0.5,0.2),(0.2,0.4,0.2)])
		self.B=array([(0.5,0.5),(0.4,0.6),(0.7,0.3)])
		self.pi=array([(0.2),(0.4),(0.4)])
		self.o=[0,1,0]
		self.t=len(self.o)#观测序列长度
		self.m=len(self.A)#状态集合个数
		self.n=len(self.B[0])#观测集合个数

	def viterbi(self):
		#利用模型和观测序列找出最优的状态序列
		#时刻t时，很多路径可以到达状态i,且观测为self.o,
		#每个路径都有自己的概率，最大的概率用矩阵z记录,前一个状态用d矩阵记录
		self.z=array(zeros((self.t,self.m)))
		self.d=array(zeros((self.t,self.m)))
		for i in range(self.m):
			self.z[0][i]=self.pi[i]*self.B[i][self.o[0]]
			self.d[0][i]=0
		for j in range(1,self.t):
			for i in range(self.m):
				maxnum=self.z[j-1][0]*self.A[0][i]
				node=1
				for k in range(1,self.m):
					temp=self.z[j-1][k]*self.A[k][i]
					if(maxnum<temp):
						maxnum=temp
						node=k+1
				self.z[j][i]=maxnum*self.B[i][self.o[j]]
				self.d[j][i]=node
		#找到T时刻概率最大的路径
		max_probability=self.z[self.t-1][0]
		last_node=[1]
		temp=0
		for i in range(1,self.m):
			if(max_probability<self.z[self.t-1][i]):
				max_probability=self.z[self.t-1][i]
				last_node[0]=i+1
				temp=i
		i=self.t-1
		#self.d[t][p],t时刻状态为p的时候，t-1时刻的状态
		while(i>=1):
			last_node.append(self.d[i][temp])
			i=i-1
		temp=['o']
		temp[0]=int(last_node[len(last_node)-1])
		j=len(last_node)-2
		while j>=0:
			temp.append(int(last_node[j]))
			j=j-1
		print (u'路径节点分别为')
		print (temp)
		print (u'该路径概率为'+str(max_probability))


if __name__ == '__main__':
	test=HMM()
	test.viterbi()