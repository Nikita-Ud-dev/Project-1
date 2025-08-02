from students import st1, st2, st3
from classes import Group

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
print(gr)
print(st1 == st1)
assert gr.find_student('Jobs') == st1 # 'Steve Jobs'
assert gr.find_student('Jobs2') is None
assert st1 == st1


gr.delete_student('Taylor')
print(gr) # Only one student