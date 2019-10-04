import objgraph

class MyMemoryObject(object):
    pass

def compute_smth(_cache={}):
    _cache[42] = dict(foo=MyMemoryObject(), bar = MyMemoryObject())

    x = MyMemoryObject()
    print('done')

objgraph.show_growth(limit=3)
compute_smth()
objgraph.show_growth()

#inspect object
print(objgraph.by_type('MyMemoryObject'))
objgraph.show_chain(objgraph.find_backref_chain(objgraph.by_type(MyMemoryObject)[0],objgraph.is_proper_module),filename = 'chain.png')