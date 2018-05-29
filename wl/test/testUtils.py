from utils import *

if __name__ == '__main__':
    print(format_diff_string(123))
    print(format_diff_string(-1))
    print(format_diff_string(3600001))
    print(format_diff_string(1551232456233, max_string=20))
    print(format_diff_string(1551232456233))

    ret = []
    convert([1,2,3,4,5], ret)
    print(ret)

    ret = []
    convert({'a': { 'b':1, 'c':2 }}, ret)
    print(ret)

    ret = []
    convert({'a': {'b': [1,2,3,4,5], 'c': 2}}, ret)
    print(ret)
    
"""
123ms
0ms
1h1ms
17954d1h54m16s233ms
17954d1h
is list
['[0]=1', '[1]=2', '[2]=3', '[3]=4', '[4]=5']
['[a.b]=1', '[a.c]=2']
is list
['[a.b.0]=1', '[a.b.1]=2', '[a.b.2]=3', '[a.b.3]=4', '[a.b.4]=5', '[a.c]=2']
"""
