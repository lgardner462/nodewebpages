<pre><a href="dl link goes here">download csv</a><pre>

%for row in csvFull[2:]:
	<a href="http://localhost:8080/{{row[0]}}">{{row[0]}}</a>	
	<pre>{{row}}</pre>
