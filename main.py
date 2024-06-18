def func_1(obj):
  obj['one'] = 'one'
  return obj

new_obj = {
  'name': 'name',
  'aaa': 'aaa',
}

res = func_1(new_obj)

print(res)
print(new_obj)
