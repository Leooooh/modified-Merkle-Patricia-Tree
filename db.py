import plyvel
import time

class DB:
    def get(self, key):
        value = self.get(key)
        if value == None:
            value = ""
        return value
    
    def put(self, key, value):
        self.put(key, value)
            
    def delete(self, key):
        self.delete(key)

    def close(self):
        self.close()
        assert self.close
