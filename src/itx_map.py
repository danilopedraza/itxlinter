from my_io import write_to_file
from os import remove
from os.path import join
from subprocess import run
from tempfile import gettempdir
from uuid import uuid4
import xml.etree.ElementTree as ET

class ITXMap:
    def __init__(self, plain):
        self.plain = plain
        self.parsed = None
    
    def parse(self):
        if self.parsed is None:
            self.parsed = ET.fromstring(self.plain)
        
        return self.parsed

def get_itx_path():
    return "C:\IBM\TransformationExtender_10.1.1"

def get_mimport_path():
    return join(get_itx_path(), "mimport.exe")

def get_mexport_path():
    return join(get_itx_path(), "mexport.exe")

def mexport(filename):
    temp_file_name = join(gettempdir(), str(uuid4()))

    run(
        "{mexport_path} {filename} -O {temp_file_name}".format(
            mexport_path=get_mexport_path(),
            filename=filename,
            temp_file_name=temp_file_name,
        )
    )

    with open(temp_file_name, 'r') as f:
        content = f.read()
    
    remove(temp_file_name)
    return content

def mimport(filename):
    temp_file_name = join(gettempdir(), str(uuid4()))

    run(
        "{mimport_path} {filename} -O {temp_file_name}".format(
            mimport_path=get_mimport_path(),
            filename=filename,
            temp_file_name=temp_file_name,
        )
    )

    with open(temp_file_name, 'rb') as f:
        content = f.read()
    
    remove(temp_file_name)
    return content

def to_mms(itx_map):
    temp_file_name = join(gettempdir(), str(uuid4()))
    write_to_file(itx_map.plain.encode('utf-8'), temp_file_name)
    return mimport(temp_file_name)

def parse_binary(filename):
    itx_map = ITXMap(mexport(filename))
    itx_map.parse()
    return itx_map
