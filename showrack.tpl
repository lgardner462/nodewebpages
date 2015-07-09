<p> <b>Node vs Rack</b> <p>
% for i in sorted(nameLocZipped):
	%rackstr= str(nameLocZipped[i])	
	%rackstr = rackstr.strip('[')
	%rackstr = rackstr.strip(']')
	%rackstr = rackstr.strip('"')
	%rackstr2 = rackstr.strip('[')
	%rackstr2 = rackstr2.strip(']')
	%rackstr2= rackstr2.strip('u')
	%rackstr2 = rackstr2.strip("'")
	<p><a href="http://localhost:8080/{{i}}">{{i}}</a>,{{rackstr2}}</p>
