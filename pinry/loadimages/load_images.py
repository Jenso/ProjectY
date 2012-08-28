from elementtree.ElementTree import parse
import os
import sys

sys.path.append('/home/jensohring/ProjectY/')
sys.path.append('/home/jensohring/ProjectY/pinry/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'pinry.settings.development'
from pins.models import Pin


tree = parse("feed_XML_UTF8_0_0_tab_singlequote_tab_0_462891022_778869190_productfeed.xml")
elem = tree.getroot()

i = 0
for el in elem:
    i += 1
    if i > 2:
        break
    #import pdb;pdb.set_trace()
    #print el.find("Name").text, el.find("ImageUrl").text#, el[2].text, el[3].text, el[4].text
    a = Pin(url=el.find("ImageUrl").text, submitter_id=1)
    a.save()


