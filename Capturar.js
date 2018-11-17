$(document).ready(()=>{
    $('#Enviar').click(()=>{
    	var lis = document.getElementById("div2").getElementsByTagName("li");
   		var Dinero = document.getElementById("Dinero");
   		var Procesador = document.getElementById("Procesador");
   		var Tarjeta = document.getElementById("Tarjeta");
   		var Ram = document.getElementById("Ram");

    	for (i = 0;	i < lis.length ; i++) {
    		console.log(lis[i].value);
    	}
    	var auxDinero = Dinero.options[Dinero.selectedIndex].value;
    	var auxProcesador = Procesador.options[Procesador.selectedIndex].value;
    	var auxTarjeta = Tarjeta.options[Tarjeta.selectedIndex].value;
    	var auxRam = Ram.options[Ram.selectedIndex].value;
    	
    //	fetch("http://localhost:5000/bayesian/pepe",{headers: {Accept: "application/json",Content-Type:"application/json"}}).then(data => console.log(data.json())).catch(error => console.log(error))
    });
});