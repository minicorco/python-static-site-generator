import shutil
from typing import List
from pathlib import Path

class Parser:
    extensions:List[str]=[]
    def valid_extension(self,extension):
        return extension in self.extensions
    def read(self,path)
        with open(path,"r") as file:
            return file.read()
    def write(self,path,dest,content,ext:".html"):
        full_path=self.dest / path.with_suffix(ext).name
        with open(full_path,'w') as file:
            file.write(content)
    def copy(self,path,source,dest):
        copy2(path,dest/path.relative_to(source))
    class ResourceParser(Parser):
        extensions=[".jpg",".png",".gif",".css",".html"]
         def parse(self, path, source, dest):
             self.copy(path, source, dest)




class parse(self,path:Path,source:Path,dest:Path):
    #els dos punts pareix que assignen tipus
    raise NotImplemented Error
