immutable_var = (16, True, "string", 115.5)
print('Immutable tuple: ', immutable_var)
# immutable_var[0] = 15 ,нельзя изменить
mutable_list = [16, True, "string", 115.5]
mutable_list.append("Russia")
mutable_list.extend([152, "Urban"])
mutable_list.remove(16)
print('Mutable list: ', mutable_list)