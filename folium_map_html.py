def popup_html(row,df):
    i = row
    print(i)
    cliente = df['cliente'].iloc[i] 
    endereco = df['endereco'].iloc[i]
    ordem_de_servico = df['ordem_de_servico'].iloc[i] 
    encarregado = df['encarregado'].iloc[i] 
    oficial = df['oficial'].iloc[i]                   
    ajudante = df['ajudante'].iloc[i]
    
    double_quotes = '"'
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<style>

table {{
  border:10px solid black;
  border-color:#D5D5D5;
  text-align:center;
  background-color:#D5D5D5;
  width:300px;
}}

tr{{
  border:1px solid #D5D5D5;
  text-align:center;
  background-color:#B8F3B8;
  width:80%;
}}

th{{
  border:1px solid black tranparent;
  text-align:center;
  border-radius:10px;
  background-color:#D5D5D5;
  border-color:grey;
  font-family: Arial, sans-serif;
}}

td{{
  border:1px solid black;
  text-align:center;
  background-color:white;
  border-color:#F1F1F1;
  font-family: Arial, sans-serif;
  font-size:12px;
}}

p{{
  text-align:left;
  height: 20px;
  width: 200px;
  padding-top: 1px;
  padding-left: 10px;
}}

#space {{
  height:2px;
  background-color:#D5D5D5;
  border:none;
}}

#space2 {{
  height:10px;
  background-color:#D5D5D5;
  border:solid #D5D5D5 1px;
}}

</style>
</head> 
  
<body>
  <div style={double_quotes}width:auto; overflow:hidden;{double_quotes}>
     <div style={double_quotes}width:300px; float:left;{double_quotes}>
        <table>
      <tr> 
         <th>Cliente</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr> 
      <tr>
         <td style={double_quotes}width:200px; height:20px; text-align:center;{double_quotes}>{cliente}</td>
      </tr> 
     <tr>
       <td id=space2></td>
      </tr>
     <tr>
         <th >Ordem de Serviço</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
     <tr>
         <td style={double_quotes}width:200px; height:20px; text-align:center;{double_quotes}>{ordem_de_servico}</td>
      </tr>
     <tr>
       <td id=space2></td>
      </tr>
     <tr>
         <th >Serviço</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
        <td style={double_quotes}width:300px; height:70px;{double_quotes}>ADEQUAÇÃO DO CENTRO DE MEDIÇÃO</td>
      </tr>
     <tr>
       <td id=space2></td>
      </tr>
     <tr>
         <th >Endereço</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
         <td style={double_quotes}width:300px; height:57px;{double_quotes}>{endereco}</td>
      </tr>
     <tr>
       <td id=space2></td>
      </tr>
   </table>
     </div>
     <div style={double_quotes}margin-left:302px;{double_quotes}>
        <table>
     <tr>
         <th >Encarregado</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
         <td style={double_quotes}width:300px; height:20px;{double_quotes}>{encarregado}</td>
      </tr>
     <tr>
       <td id=space2></td>
      </tr>
     <tr>
         <th >Oficial</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
         <td style={double_quotes}width:300px; height:20px;{double_quotes}>{oficial}</td>
      </tr>
     <tr>
       <td id=space2></td>
      </tr>
     <tr>
         <th >Ajudante</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
         <td style={double_quotes}width:300px; height:20px;{double_quotes}>{ajudante}</td>
      </tr>
   </table>
       <table style={double_quotes}margin-top:2px;{double_quotes}>
         <tr>
         <th >Situação</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
         <td style={double_quotes}width:300px; height:20px; color:green;{double_quotes}>Em Execução</td>
      </tr>
      <tr>
       <td id=space2></td>
      </tr>
         <tr>
         <th >Observação</th>
      </tr>
     <tr>
       <td id=space></td>
      </tr>
      <tr>
        <td style={double_quotes}width:300px; height:40px; overflow:scroll;{double_quotes}><p>Falta a ligação com a revisão \n Atualizado em: 31/12/2022</p></td>
      </tr>
       </table>
     </div>
</div>
  
</body>
</html>
"""
    return html