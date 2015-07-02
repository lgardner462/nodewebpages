<table border="1">
%for row in nodeNameAndLoc:
  <tr>
  %for col in row:
    <td><a href="http://localhost:8080/shownode/{{row[0]}}">{{col}}</a></td>
  %end
  </tr>
%end
</table>
