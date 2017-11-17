# Original script and explanation taken from location below
# Labeling in arcmap with python, without creating any new data
# http://www.bgcarto.com/map-typography-a-python-label-expression/

def FindLabel ([PIN],[OWNER_NAME]):
  apn = [PIN]
  own = [OWNER_NAME]
  if own == None:
    L = apn +"\n"+"<fnt size='6'><ita><clr black='70'>"+"Unknown"+"</clr></ita></fnt>"
  elif own != None:
    ownT=own.title()
    L = apn +"\n"+"<fnt size='6'><ita><clr black='70'>"+ownT.replace("&","&amp;")+"</clr></ita></fnt>"
  return L
 
