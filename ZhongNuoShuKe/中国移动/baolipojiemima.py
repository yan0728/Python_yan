# 由于MD5模块在python3中被移除
# 在python3中使用hashlib模块进行md5操作

import hashlib
import requests
import json

# 待加密信息
str = 'IUY9JiCa35ktBHKrJaS3s+Q49GRXtbaWchanneltest02channelcontentBB844B80F251FB56CA4AE5A68C56AF60FD8B63F672D73F429B4EE5CD24C4BE2CF5A8960C0DAA401E5B07FFFD1145CAA1262173BBBA688D394DFFB4CD652CC71996C664BC5E37CD11D44CB3B50FDA59F77C62C964370A1B2DFA256BFF2BB8BCECE1FC9F3188470FF0A4533A9963A3098638574388EF611560FF2F7BA64D8C061F76CE3B66A2AD130ACD1F8098A45AE23BF069B62A8303F8033F95767436BB2C53B432B0116E6AFBA069676808F886C9AF72399DA92F36BAE70AE83A310166798F4DD26F53DBE79DACB41B042EDA05B6F8contentflowNo201200002flowNomethodextend.yidong.contract.createmethodtime20210428165937timeversion1.0.1versionIUY9JiCa35ktBHKrJaS3s+Q49GRXtbaW'

# 创建md5对象
m = hashlib.md5()

# Tips
# 此处必须encode
# 若写法为m.update(str)  报错为： Unicode-objects must be encoded before hashing
# 因为python3里默认的str是unicode
# 或者 b = bytes(str, encoding='utf-8')，作用相同，都是encode为bytes
b = str.encode(encoding='utf-8')
m.update(b)
str_md5 = m.hexdigest()

print('MD5加密前为 ：' + str)
print('MD5加密后为小写 ：' + str_md5)

# 另一种写法：b‘’前缀代表的就是bytes
# str_md5 = hashlib.md5(b str).hexdigest()
print('MD5加密后为大写 ：' + str_md5.upper())
