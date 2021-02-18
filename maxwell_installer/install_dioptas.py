#!/usr/bin/python3
import os
import sys
import subprocess
import re

class Installer(object):
    DESKTOP_FILE="""
[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Exec=/asap3/fs-sc/gpfs/common/scdd01/conda_env/integration_pipeline_stable/bin/dioptas
Name=Dioptas with Pipeline
Icon=/asap3/fs-sc/gpfs/common/scdd01/conda_env/integration_pipeline_stable/lib/python3.6/site-packages/dioptas/resources/icons/icon.png
Categories=Science;
    """
    
    LINK_NAME = "Dioptas.desktop"
    
    def __init__(self):
        object.__init__(self)
        self.user_id = None
        
        self.get_userid()
        self.create_dioptas_link()
        self.create_data_links()
        
    def get_userid(self):
        r = subprocess.run(["id"], stdout=subprocess.PIPE)
        d = r.stdout.decode()
        p = re.compile("uid=[0-9]+\(([^\)]+)\)")
        
        tl = p.findall(d)
        if len(tl)>0:
            self.user_id = tl[0]
        
    def create_dioptas_link(self):
        
        try:    
            fn = os.path.join("/home/{}/Desktop".format(self.user_id), self.LINK_NAME)
            print("Creating a desktop link ({})..".format(fn))
            with open(fn, "w") as fh:
                fh.write(self.DESKTOP_FILE)
                
        except IOError as e:
            print("Error: {}".format(e))
            
    def create_data_links(self):
        fn = "/home/{}/Desktop/data".format(self.user_id)
        start = "/asap3/petra3/gpfs/p02.2"
        print("Creating a data link ({} -> {})..".format(start,fn))
        subprocess.run(["ln", "-s", start, fn])
    
        

def main():
    i = Installer()

if __name__=="__main__":
    main()
