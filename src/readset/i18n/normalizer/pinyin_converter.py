def pinyin_dict():
    """Generated map"""
    pinyin_out = file('pinyin.py', 'w')
    pinyin_out.write("# Chinese character mapping\n\n")
    pinyin_out.write("mapping = {\n\t")
    i = 0    

    for line in open('pinyin.db'):
        key, value = line.split('\t')
        i += 1
        delimiter = '\n\t' if i%4 == 0 else ' '
        char = value.split()[0][:-1].lower()

        if char == '"':
            char = r'\"'
        elif char == '\\':
            char = r'\\'

        pinyin_out.write(r'%s : "%s",%s' % (int(key, base=16), char, delimiter))

    pinyin_out.write("\n}\n")
    pinyin_out.close()


if __name__ == '__main__':
    pinyin_dict()
    from pinyin import mapping
    print("The number of items of mapping is %s" % len(mapping))
