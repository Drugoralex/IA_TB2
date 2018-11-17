$(document).ready(()=>{
    $('#Enviar').click(async ()=>{
    	var lis = document.getElementById("div2").getElementsByTagName("li");
   		var Dinero = document.getElementById("Dinero");
   		var Procesador = document.getElementById("Procesador");
   		var Tarjeta = document.getElementById("Tarjeta");
   		var Ram = document.getElementById("Ram");

    	/*for (i = 0;	i < lis.length ; i++) {
    		console.log(lis[i].value);
		}*/
    	var auxDinero = Dinero.options[Dinero.selectedIndex].value;
    	var auxProcesador = Procesador.options[Procesador.selectedIndex].value;
    	var auxTarjeta = Tarjeta.options[Tarjeta.selectedIndex].value;
    	var auxRam = Ram.options[Ram.selectedIndex].value;
		
		let data = {
			lista_juegos: function() {
				let array = [];
				for(let i = 0;i<lis.length;i++){
					array.push(lis[i].value);
				}
				return array;
			}(),
			dinero: auxDinero
		};

		console.log(data);

		let res = await fetch('http://localhost:5000/logica', {
			method: 'POST',
			body: JSON.stringify(data),
			headers: {
				"Origin": "http://localhost:5000",
				"Access-Control-Request-Method": "POST",
				"Access-Control-Request-Headers": "Content-Type"
			}
		});

		console.log(await res.json());
    });
});