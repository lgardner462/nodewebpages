<a href="http://localhost:8080/download/txe1_node_hwtab.csv">download csv</a>
<p></p>
<pre><a href="http://localhost:8080/showmac">Show Mac Addresses</a></pre>
<p></p>
<pre><a href="http://localhost:8080/showrack">Show Rack Locations</a></pre>

<table border="1">
%for row in csvFull[:]:
  <tr>
  <td><a href="http://localhost:8080/{{row[0]}}">{{row[0]}}</a></td>
  <td>{{row[1:]}}</td></tr>
%end
</table>

