import re

def contacts(container, info, operation):
    email_pattern = r'^[^@]+@[^@]+[.][^@]+$'
    name_pattern = r'^[a-zA-Z0-9-_ ]*$'
    oper_check = ('add', 'update', 'delete')
    if operation not in oper_check:  # check operation
        return False
    if 'email' not in info or 'name' not in info:   # check info
        return False
    if re.search(email_pattern, info['email']) and re.search(name_pattern, info['name']):  # check pattern
        email = info.pop('email')
        if operation == 'add':
            container.update({email: info})
            return True
        elif operation == 'update':
            if email in container:
                container.update({email: {**container.get(email), **info}})
                return True
            else:
                return False
        elif operation == 'delete':
            if email in container:
                container.pop(email, "none")
                return True
            else:
                return False
        return False
    else:
        return False
    return True
