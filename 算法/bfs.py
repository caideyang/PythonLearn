#encoding:utf-8

"""
广度优先算法

本例主要实现从"you"的朋友关系里找到一位芒果供应商（名字最后一位是m)

"""
from collections import deque
import time
#假设person最后一位字母是m，就认为他是mongo供应商，返回True
def is_mongo_seller(person):
    return person[-1] == "m"

graph = { "you":["alex","bob","jeck"],
          "alex":["you","jeck","lessy","frank"],
          "bob":["you","frank","bipper"],
          "jeck":["you","alex","jarry"],
          "lessy":["alex","qiu"],
          "frank":["alex","bob","qiu"],
          "bipper":["bob","jim"],
          "jarry":["jeck"],
          "qiu":["lessy","frank"],
          "jim":["bipper","alvom"],
          "alvom":["jim"]
          }

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = [name]
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if is_mongo_seller(person):
                print("Person %s is a mongo seller ." % person)
            else:
                search_queue += graph[person]
                searched.append(person)
                print(searched)
    return False

search("you")
