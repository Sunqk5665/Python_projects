#创建映射表
table=''.maketrans('abcdef123','uvwxyz@#$')
s="Python is a great programming language. I like it!"
print(s.translate(table))