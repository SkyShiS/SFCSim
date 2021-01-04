########################  
#nodes类测试
########################
#      add sfcsim path to sys path ##########
import sys     
import os
path=format(os.getcwd())
sys.path.append(path) 
# end    
from sfcsim import *
from network import *
print(nodes.__doc__)
##########################节点添加删除测试##########################################
print('*****************     测试添加删除节点    ******************')
node1=node(atts={'cpu':10,'memory':10,'storage':10,'access':False})
node2=node(uuid='node2',atts={'cpu':10,'memory':10,'storage':10,'access':False})
nodes=nodes()
nodes.add_node(node1)
nodes.add_node(node2)
nodes.add_node(node(uuid='node2',atts={'cpu':10,'memory':10,'storage':10,'access':False}))
nodes.add_node(node(uuid='node3',atts={'cpu':10,'memory':10,'storage':10,'access':False}))
nodes.add_node(node(uuid='node4',atts={'cpu':10,'memory':10,'storage':10,'access':False}))
nodes.add_node(node(uuid='node5',atts={'cpu':10,'memory':10,'storage':10,'access':False}))
nodes.add_node(node(uuid='node6',atts={'cpu':10,'memory':10,'storage':10,'access':False}))
nodes.add_vnf('node1',vnf_type(atts={'cpu':1,'memory':1,'storage':1}))
nodes.add_vnf('node1',vnf_type(name='type2',atts={'cpu':1,'memory':1,'storage':1}))
nodes.delete_node('node1')
nodes.delete_node('node6')
nodes.show_access()
nodes.show_server()
nodes.show()
##########################节点属性测试#################################################
print('*****************     测试修改节点属性    ******************')
nodes.set_access_nodes(['node1','node2'])
nodes.set_atts('node1',{'access':True})
nodes.set_atts('node2',{'access':True})
nodes.set_atts('node2',{'access':True}) #测试重复设置是否会影响数据
nodes.set_atts('node3',{'access':True})
nodes.show_access()
nodes.show_server()
nodes.show()
nodes.set_atts('node3',{'cpu':10,'access':False})
nodes.set_atts('node3',{'cpu':10,'access':False})
nodes.delete_node('node2')
nodes.show_access()
nodes.show_server()
nodes.show()
##########################vnf测试###############################################
print('*****************     测试节点添加移除vnf    ******************')
nodes.add_vnf('node1',vnf_type(atts={'cpu':1,'memory':1,'storage':1}))
nodes.show()
nodes.add_vnf('node2',vnf_type(atts={'cpu':1,'memory':1,'storage':1}))
nodes.show()
nodes.delete_vnf('node1','vnf_type2')
nodes.delete_vnf('node1','vnf_type1')
nodes.delete_vnf('node2','vnf_type1')
nodes.show_access()
nodes.show_server()
nodes.show()