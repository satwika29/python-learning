emp = {"name":"abcd","id":1}
empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
for item in empList:
    print('name',item['name'],'id',item['id'])


def display_emp_list():
    emp = {"name":"abcd","id":1}
    empList = [{"name":"abcd","id":1},{"name":"xyz","id":2}]
    for item in empList:
        print('name',item['name'],'id',item['id'])
display_emp_list()