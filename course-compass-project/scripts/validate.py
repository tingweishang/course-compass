import json,re
from pathlib import Path
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'dist/data/courses.json').read_text())
assert isinstance(data,list) and data
ids=set()
for c in data:
    for k in ['id','title','subtitle','category','icon','level','source','pitfall','exercise']:
        assert isinstance(c[k],str) and c[k].strip(), (c.get('id'),k)
    assert re.fullmatch('[a-z][a-z0-9]*(?:-[a-z0-9]+)*',c['id'])
    assert c['id'] not in ids; ids.add(c['id'])
    assert type(c['minutes']) is int and c['minutes']>0
    assert len(c['goals'])==3 and all(isinstance(g,str) and g.strip() for g in c['goals'])
    assert len(c['concepts'])==3
    for x in c['concepts']:
        assert all(isinstance(x[k],str) and x[k].strip() for k in ['title','body','example'])
    assert len(c['quiz'])==2
    for q in c['quiz']:
        assert len(q['options'])==3 and len(set(q['options']))==3
        assert all(isinstance(o,str) and o.strip() for o in q['options'])
        assert type(q['answer']) is int and 0<=q['answer']<3
        assert q['question'].strip() and q['explanation'].strip()
for name in ['index.html','style.css','app.js']:
    assert (root/'dist'/name).is_file()
print(f'PASS: {len(data)} courses, {sum(len(c["concepts"]) for c in data)} concepts, {sum(len(c["quiz"]) for c in data)} quiz questions; unique routes and required files verified.')
