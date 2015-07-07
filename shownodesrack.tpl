<table border="1">
<a href="dl link goes here">download csv</a>
%for row in nodeNames[2:]:
  <tr>
  <td><a href="http://localhost:8080/shownode/{{row}}">{{row}}</a></td>
  </tr>
%end
</table>
