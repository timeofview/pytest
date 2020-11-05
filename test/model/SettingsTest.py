from model.setting import Setting

s0 = Setting(0, "version", "name", "path", "filename", "extension", "args", "stdin", 1, 1,
             True, 1, 1)
s1 = Setting(1, "version1", "name1", "path1", "filename", "extension", "args", "stdin")
s2 = Setting(2, "version2", "name2", "path2", "filename", "extension", "args", "stdin", 1, 1,
             True)
print(s0.to_string())
print(s1.to_string())
print(s2.to_string())