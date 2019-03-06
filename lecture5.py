#!/usr/bin/python3


#pickle aka serialization
class A(object):
    def __init__(self, arg):
        self.a = arg

    def __repr__(self):
        return '<A(a={}) at 0x{:x}>'.format(self.a, id(self))
    
a = A(10)
print(a)
import pickle
pickle.dump(a,open("/tmp/save.pickle", "wb"))
b = pickle.load(open("/tmp/save.pickle", "rb"))
print(b)
c = pickle.dumps(a,protocol=pickle.HIGHEST_PROTOCOL)
print(c)
print(type(c))
d = pickle.loads(c)
print(d)

class B(object):
    def __init__(self, arg):
        self.a = arg
        self.my_temp_data = 'some data'

    def __repr__(self):
        return '<A(a={}) at 0x{:x}>'.format(self.a, id(self))

    def __getstate__(self):
        state = self.__dict__.copy()
        del state['my_temp_data']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        self.my_temp_data = ''

a = A(11)
print(a)
b = pickle.loads(pickle.dumps(a))
print(b)

#csv
import csv
row1 = ["1","one"]
row2 = ["2","two"]
row3 = ["3","three"]
rows = [row1, row2, row3]
with open("/tmp/some.csv","w", newline='') as csv_fh:
    writer = csv.writer(csv_fh, delimiter=",", quoting=csv.QUOTE_MINIMAL, quotechar='`', lineterminator='¯\_(ツ)_/¯ ')
    writer.writerows(rows)

reader = csv.reader(open("/tmp/some.csv","r"))
for row in reader:
    print(row)

#xml
import os
import xml.etree.cElementTree as ET


testXML = '''<TreeRoot>
    <Element1 value1="¯\_(ツ)_/¯">
       <SubElement1>¯\_(ツ)_/¯</SubElement1>
        <SubElement2>¯\_(ツ)_/¯</SubElement2>
   </Element1>
    <Element2 value2="ಠ_ಠ">
        <SubElement3>(╯°□°）╯︵ ┻━┻</SubElement3>
        <SubElement4>¯\_(ツ)_/¯</SubElement4>
    </Element2>
</TreeRoot>
'''

with open("/tmp/xmlfile.xml","w") as xmlfile:
    xmlfile.write(testXML)

XML_FILE = os.path.join(os.environ['HOME'], '/tmp/xmlfile.xml')
try:
    tree = ET.ElementTree(file=XML_FILE)
    root = tree.getroot()
    print(root)
    print(type(root))
    for child_of_root in root:
        print(child_of_root.tag)
        print(child_of_root.attrib)
        for child_of_child_of_root in child_of_root:
            print(child_of_child_of_root.tag)
            print(child_of_child_of_root.attrib)


except IOError as e:
    print("nError - can't find file {}".format(e) )
    
#JSON
import json
a = json.dumps(['foo',{"bar":["baz", None, 1.0, 2]}], sort_keys=True, indent=4)
print(a)
b = json.loads(a)
print(b)

#YAML
import yaml
b = yaml.safe_dump({'foo':{'bar':[1,2,3],
                            'baz':{'monty':[{'key':"value"},
                                            {'jey':"dalue"}]}}})
print(b)

#sqlite
import sqlite3
conn = sqlite3.connect('/tmp/sqlite.db')
print('Opened database successfully')

conn.execute('CREATE TABLE COMPANY'
            '(ID INT PRIMARY KEY NOT NULL,'
            'NAME TEXT NOT NULL,'
            'AGE INT NOT NULL,'
            'ADDRESS CHAR(50),'
            'SALARY REAL);')
print('Table created')
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS, SALARY)"
            "VALUES (1,'Abdulah', 33, 'Lahore', 20000)")
conn.commit()

cursor = conn.execute("SELECT id, name, age, address, salary from COMPANY")
for row in cursor:
    print(row)

conn.execute('UPDATE COMPANY set SALARY = 250000.1 where ID=1')
conn.commit()

cursor = conn.execute('SELECT id, name, address, salary from COMPANY where ID=1')
cursor.fetchone()

conn.execute("DELETE from COMPANY where ID=1;")
conn.commit()

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,?,?,?)",
            (4,"Gogi", 33, 'Detroit', -1))
conn.commit()

import os
os.remove("/tmp/sqlite.db")


#multiprocessing

def count(n):
    while n > 0:
        n -= 1
c = 8000000
import time
start = time.time()
count(c)
count(c)
print('no threads {0:03.2f} sec'.format(time.time() - start))

from threading import Thread
start = time.time()
t1 = Thread(target=count,args=(c,))
t1.start()
t2 = Thread(target=count,args=(c,))
t2.start()
t1.join()
t2.join()
print('threads(threading.Thread) {0:03.2f} sec'.format(time.time() - start))

#sudo pip3 install gevent
import gevent
start = time.time()
gevent.joinall([
    gevent.spawn(count,c),
    gevent.spawn(count,c),
])
print('threads(gevent) {0:03.2f} sec'.format(time.time() - start))

import multiprocessing
start = time.time()
p1 = multiprocessing.Process(target=count,args=(c,))
p2 = multiprocessing.Process(target=count,args=(c,))
p1.start()
p2.start()

p1.join()
p2.join()
print('threads(multiprocessing) {0:03.2f} sec'.format(time.time() - start))

#IPC
from multiprocessing import Process, Queue

def f(q):
    q.put([42,None,'hello'])
q = Queue()
p = Process(target=f, args=(q,))
p.start()
print(q.get())
p.join()

from multiprocessing import Pipe
def aaaa(conn):
    conn.send(['hello',11,None])
    print('client receives',conn.recv())
    conn.close()

parent_conn,child_conn = Pipe()
p = Process(target=aaaa, args=(child_conn,))
p.start()
print('server receives', parent_conn.recv())
parent_conn.send(['python',5])
p.join()



def bbb1(i):
    print('ya, ganstas',i)


processes = []
for num in range(5):
    p = Process(target=bbb1, args=(num,))
    p.start()
    processes.append(p)

    for p in processes:
        p.join()

from multiprocessing import Lock

def bbb(lock, i):
    with lock:
        print('ya, ganstas',i)

lock = Lock()

processes = []
for num in range(5):
    p = Process(target=bbb, args=(lock, num))
    p.start()
    processes.append(p)

    for p in processes:
        p.join()