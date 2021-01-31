import random
import unittest
import MerklePatriciaTrie as MPT
import time
from hashlib import sha256
import string
import plyvel
import pickle

class TestingClass(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(TestingClass, self).__init__(*args, **kwargs)
		testdb = plyvel.DB("test", create_if_missing = True)
		self.test = MPT.MerklePatriciaTrie(testdb,"")
		self.db = plyvel.DB("rootDB", create_if_missing = True)
	
	def test_all(self):
		keys = ["a711355", "a77d337", "a7f9365", "a77d397"]
		values = ["aaaaaaaa", "bbbbbbbb", "cccccccc", "dddddddd"]
		for i in range(4):
			self.test.update(keys[i], values[i])

		print("Current root:", self.test.root_hash(),'')
		self.db.put(b"BlockTrie", self.test.root_hash())

		print self.test.iter_subtree('a7')

if __name__ == '__main__':
	unittest.main()
