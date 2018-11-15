$(document).ready(()=>{
    $('#Enviar').click(()=>{
    	var lis = document.getElementById("div2").getElementsByTagName("li");
    	for (i = 0;	i < lis.length ; i++) {
    		console.log(lis[i].id);
    	}
    });
});