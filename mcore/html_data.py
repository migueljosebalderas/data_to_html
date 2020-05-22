
def data_to_html(list, query, output_file, sign="MB-HTML", title="Data Results"):
    with open(output_file, "w") as html:
        html.writelines(_render_template_html(list, query, sign, title))


def _render_template_html(list, query, sign, title="Data Results"):
    template = f"""
<!DOCTYPE html>
<html>

<head>
  <meta charset='UTF-8'>
  
  <title{title}</title>
  
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

"""

    template += """
  <style>
  * { 
    margin: 0; 
    padding: 0; 
  }
  body { 
    font: 14px/1.4 Palatino, Serif; 
  }
  
  /* 
  Generic Styling, for Desktops/Laptops 
  */
  table { 
    width: 100%; 
    border-collapse: collapse; 
  }
  /* Zebra striping */
  tr:nth-of-type(odd) { 
    background: #eee; 
  }
  th { 
    background: #333; 
    color: white; 
    font-weight: bold; 
  }
  td, th { 
    padding: 6px; 
    border: 1px solid #9B9B9B; 
    text-align: left; 
  }
  @media 
  only screen and (max-width: 760px),
  (min-device-width: 768px) and (max-device-width: 1024px)  {
    table, thead, tbody, th, td, tr { display: block; }
    thead tr { position: absolute;top: -9999px;left: -9999px;}
    tr { border: 1px solid #9B9B9B; }
    td { border: none;border-bottom: 1px solid #9B9B9B; position: relative;padding-left: 50%; }
    
    td:before { position: absolute;top: 6px;left: 6px;width: 45%; padding-right: 10px; white-space: nowrap;}
    
    /*
    Label the data
    */
    
    """

    for columname in list[0]:
        template += 'td:nth-of-type(0):before { content: "' + columname + '"; }\n'

    template += """
  }

  /* Smartphones (portrait and landscape) ----------- */
  @media only screen
  and (min-device-width : 320px)
  and (max-device-width : 480px) {
    body {
      padding: 0;
      margin: 0;
      width: 320px; }
    }

  /* iPads (portrait and landscape) ----------- */
  @media only screen and (min-device-width: 768px) and (max-device-width: 1024px) {
    body {
      width: 495px;
    }
  }

  </style>
  <!--<![endif]-->
<script type="text/javascript">

function search(){

  var s = document.getElementById('search').value;

  rows = document.getElementById('data').getElementsByTagName('TR');
  for(var i=0;i<rows.length;i++){
    if ( rows[i].textContent.indexOf(s)>0  || s.length==0 ) {
	  rows[i].style.display ='';
    } else {
      rows[i].style.display ='none';
    }
  }
}


var timer;
function delayedSearch() {
	clearTimeout(timer);
	console.log('delay-ing')
    timer = setTimeout(function () {
		console.log('delay-running')
		search();
    }, 500);
  }</script>
</head> 
"""

    template += f"""
<body>
	<code>
		SQL> {query}
	</code>
<div><input type="text" size="30" maxlength="1000" value="" id="search" onkeyup="delayedSearch();" /><input type="button" value="Go" onclick="lsearch();"/> </div>
<table><thead><tr> """

    for columname in list[0]:
        template += f"<th>{columname}</th>"

    template += """
</tr></thead>
<tbody id="data"> 
	"""

    for row in list[1:]:
        template += "<tr>\n"

        for value in row:
            template += f"<td>{value}</td>"

        template += "</tr>\n"

    template += f"""
</tbody></table>
<p><span>&#171;</span>{sign}<span>&#187;</span></p>
</body></html>
    """

    return template
