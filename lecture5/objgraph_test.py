x = []
y = [x, [x], dict(x=x)]
import objgraph
objgraph.show_refs([y], filename='/tmp/sample-graph.png')
objgraph.show_backrefs([y], filename='/tmp/sample-back-graph.png')

objgraph.show_most_common_types()