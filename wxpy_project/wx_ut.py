
import sys

sys.path.append('/Users/zhangxian/program/python/python test/pygame/')
#from pygame import pygameInterface
import common
import pygameInterface
import alphabet
#from pygame import common

common.GetCurrectDir()
alphabetInformation = pygameInterface.GetCurrentBallRect()
print("call.", alphabetInformation['alphabet'])
print("hello world.", sys.path)

alphabet.StartAlphabetGame()



