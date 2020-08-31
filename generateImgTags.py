import os

basePath = "../blakesanie.com/cs/techUsed"

for filename in os.listdir(basePath):
    print('<img height="20" style="margin-bottom: 10px;" src="https://blakesanie.com/cs/techUsed/{}" />&nbsp;&nbsp;'.format(filename))
