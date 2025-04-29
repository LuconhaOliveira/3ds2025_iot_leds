const obterDados = async ()=>{
    const url = "https://threeds2025-iot-leds.onrender.com/request"
    const response = await fetch(url)
    const data = response.json()
    console.log(data)
    const led = document.getElementById('estado_led')
    if (data.pedido == 1){
        led.innerHTML = "Ligado"
    }
    if (data.pedido == 0){
        led.innerHTML = "Desligado"
    }
}

setInterval(obterDados, 1000)