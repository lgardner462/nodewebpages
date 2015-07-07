<p> <b>Node vs Mac</b> <p>
% for i in sorted(nameMacZipped):
	%macstr= str(nameMacZipped[i])	
	%macstr = macstr.strip('[')
	%macstr = macstr.strip(']')
	%macstr = macstr.strip('"')
	%macstr2 = macstr.strip('[')
	%macstr2 = macstr2.strip(']')
	%macstr2= macstr2.strip('u')
	%macstr2 = macstr2.strip("'")
	{{i}},{{macstr2}}<br>
