{"changed":true,"filter":false,"title":"aStar.py","tooltip":"/aStar.py","value":"from environment import *\nev=Environment([1, 1], [5, 8])\nev.readEnvironment()\n\ndef actions(coord, L):\n    R=[]\n    x=coord[0]\n    y=coord[1]\n    if(L[x][y+1]!='#'):\n        R+=[[x, y+1]]\n    \n    if(L[x+1][y]!='#'):\n        R+=[[x+1, y]]\n    \n    if(L[x][y-1]!='#'):\n        R+=[[x, y-1]]\n    \n    if(L[x-1][y]!='#'):\n        R+=[[x-1, y]]\n        \n    return R\ndef A_Star(ev):\n    queue=[ev.start]\n    explored=[]\n    distList=\n    while(len(queue)!=0):\n        node=\n    ","undoManager":{"mark":-169,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":9,"column":9},"end":{"row":9,"column":12},"action":"insert","lines":["+[]"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":12},"end":{"row":9,"column":14},"action":"insert","lines":["[]"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":13},"end":{"row":9,"column":15},"action":"insert","lines":["xz"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["z"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":15},"end":{"row":9,"column":17},"action":"insert","lines":[" y"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":19},"action":"insert","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":21},"end":{"row":10,"column":8},"action":"insert","lines":["","        "]},{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":4},"end":{"row":12,"column":21},"action":"insert","lines":["if(L[x][y+1]!='#'):","        R+=[[x, y+1]]"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":13},"end":{"row":11,"column":15},"action":"remove","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":10},"end":{"row":11,"column":12},"action":"insert","lines":["$1"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":10},"end":{"row":11,"column":12},"action":"remove","lines":["$1"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":12},"action":"insert","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":14},"end":{"row":12,"column":16},"action":"insert","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":19},"end":{"row":12,"column":21},"action":"remove","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":15,"column":21},"action":"insert","lines":["","    if(L[x][y+1]!='#'):","        R+=[[x, y+1]]"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["+"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"remove","lines":["+"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["-"]}]}],[{"group":"doc","deltas":[{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]},{"start":{"row":16,"column":4},"end":{"row":17,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":4},"end":{"row":18,"column":21},"action":"insert","lines":["if(L[x][y+1]!='#'):","        R+=[[x, y+1]]"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":10},"end":{"row":17,"column":12},"action":"insert","lines":["-1"]}]}],[{"group":"doc","deltas":[{"start":{"row":17,"column":15},"end":{"row":17,"column":17},"action":"remove","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":17},"end":{"row":18,"column":19},"action":"remove","lines":["+1"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":14},"end":{"row":18,"column":16},"action":"insert","lines":["-1"]}]}],[{"group":"doc","deltas":[{"start":{"row":18,"column":21},"end":{"row":20,"column":4},"action":"insert","lines":["","        ","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":20,"column":4},"end":{"row":20,"column":12},"action":"insert","lines":["return R"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":12},"end":{"row":23,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":24,"column":0},"action":"remove","lines":["",""]},{"start":{"row":23,"column":4},"end":{"row":24,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":9},"action":"insert","lines":["while"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":9},"end":{"row":24,"column":11},"action":"insert","lines":["()"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"insert","lines":["temp"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["temp"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"insert","lines":["`"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":0},"end":{"row":23,"column":1},"action":"remove","lines":["`"]},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["    temp"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":8},"end":{"row":23,"column":11},"action":"insert","lines":["=ac"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":11},"end":{"row":23,"column":16},"action":"insert","lines":["tions"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":16},"end":{"row":23,"column":18},"action":"insert","lines":["()"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":18},"end":{"row":24,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":9},"action":"insert","lines":["clean"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":9},"end":{"row":24,"column":11},"action":"insert","lines":["Ma"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":15},"end":{"row":22,"column":4},"action":"insert","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":4},"end":{"row":22,"column":6},"action":"insert","lines":["gl"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":6},"end":{"row":22,"column":8},"action":"insert","lines":["ob"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":8},"end":{"row":22,"column":10},"action":"insert","lines":["al"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":10},"end":{"row":22,"column":13},"action":"insert","lines":[" ev"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":13},"end":{"row":25,"column":15},"action":"insert","lines":["ev"]}]}],[{"group":"doc","deltas":[{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":10},"end":{"row":22,"column":13},"action":"remove","lines":[" ev"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":8},"end":{"row":22,"column":10},"action":"remove","lines":["al"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":0},"end":{"row":22,"column":8},"action":"remove","lines":["    glob"]}]}],[{"group":"doc","deltas":[{"start":{"row":21,"column":15},"end":{"row":22,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":16},"action":"remove","lines":["cleanMap=ev."]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":12},"end":{"row":23,"column":5},"action":"insert","lines":["","    v"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":5},"action":"remove","lines":["v"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":16},"action":"insert","lines":["cleanMap=ev."]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":16},"end":{"row":23,"column":18},"action":"insert","lines":["gi"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":16},"end":{"row":23,"column":18},"action":"remove","lines":["gi"]},{"start":{"row":23,"column":16},"end":{"row":23,"column":37},"action":"insert","lines":["giveEnvironmentList()"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":17},"end":{"row":24,"column":20},"action":"insert","lines":["ev,"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":20},"end":{"row":24,"column":21},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":19},"end":{"row":24,"column":21},"action":"remove","lines":[",s"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":20},"end":{"row":24,"column":23},"action":"insert","lines":["sta"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":23},"end":{"row":24,"column":25},"action":"insert","lines":["rt"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":25},"end":{"row":24,"column":28},"action":"insert","lines":["., "]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":25},"end":{"row":24,"column":28},"action":"remove","lines":["., "]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":25},"end":{"row":24,"column":27},"action":"insert","lines":[", "]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":37},"end":{"row":24,"column":28},"action":"remove","lines":["","    temp=actions(ev.start, )"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":12},"end":{"row":23,"column":37},"action":"remove","lines":["","    cleanMap=ev.giveEnvironmentList()"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":11},"end":{"row":22,"column":14},"action":"insert","lines":["ev,"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":13},"end":{"row":22,"column":14},"action":"remove","lines":[","]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":13},"end":{"row":22,"column":15},"action":"insert","lines":[".s"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":15},"end":{"row":22,"column":19},"action":"insert","lines":["tart"]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":23,"column":4},"action":"remove","lines":["","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":10},"end":{"row":23,"column":14},"action":"insert","lines":["queu"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":14},"end":{"row":23,"column":15},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":10},"end":{"row":23,"column":13},"action":"insert","lines":["len"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":13},"end":{"row":23,"column":14},"action":"insert","lines":["("]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":19},"end":{"row":23,"column":20},"action":"insert","lines":[")"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":20},"end":{"row":23,"column":22},"action":"insert","lines":["!="]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":22},"end":{"row":23,"column":23},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":24},"end":{"row":24,"column":8},"action":"insert","lines":[":","        "]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":8},"end":{"row":24,"column":12},"action":"insert","lines":["node"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["-"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["-"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["0"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["-"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"remove","lines":["-"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":22,"column":20},"end":{"row":24,"column":4},"action":"insert","lines":["","    ","    "]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":6},"action":"insert","lines":["ex"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":6},"end":{"row":23,"column":11},"action":"insert","lines":["plate"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":8},"end":{"row":23,"column":11},"action":"remove","lines":["ate"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":7},"end":{"row":23,"column":8},"action":"insert","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["expl"]},{"start":{"row":23,"column":4},"end":{"row":23,"column":12},"action":"insert","lines":["explored"]}]}],[{"group":"doc","deltas":[{"start":{"row":23,"column":12},"end":{"row":23,"column":15},"action":"insert","lines":["=[]"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":7},"action":"insert","lines":["dis"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":7},"action":"remove","lines":["dis"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":4},"end":{"row":24,"column":7},"action":"insert","lines":["dis"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":7},"end":{"row":24,"column":9},"action":"insert","lines":["tL"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":10},"end":{"row":24,"column":12},"action":"insert","lines":["st"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":12},"end":{"row":24,"column":15},"action":"insert","lines":["=[]"]}]}],[{"group":"doc","deltas":[{"start":{"row":24,"column":13},"end":{"row":24,"column":15},"action":"remove","lines":["[]"]}]}]]},"ace":{"folds":[],"scrolltop":180,"scrollleft":0,"selection":{"start":{"row":22,"column":20},"end":{"row":22,"column":20},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":11,"state":"start","mode":"ace/mode/python"}},"timestamp":1427398714587}