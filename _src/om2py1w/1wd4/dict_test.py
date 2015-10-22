# -*- coding: utf-8 -*-
# dicts are index by keys,
# are not like sequence indexed by numbers
# what
# - keys in dict are immutable
# - 字符和数字都可使是keys
# - 包括字符or数字ortuple的tuple也可使是keys
# - 但是若tuple包含mutable object 则不可以用作 keys
# - 所以 list 是不能用作 key的
# - 配对的 男：女
# - 如果后面添加keys 存在了 则会覆盖掉（遗忘以前的）
# ....
# keys()
# sorted() 排序

tel = {'jack':137, "sape":9801}
tel['guido'] = 9366
print tel
print tel["jack"]

del tel['sape']
print tel
print tel.keys()

dict([('jeremy', 13798019366), ('jesus', 5201314)])
print dict
print {x:x**2 for x in (2, 4, 6)}
dict(jeremy=13798019366, jesus=5201314)