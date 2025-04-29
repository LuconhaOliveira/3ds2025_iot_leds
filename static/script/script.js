const obterDados = async () => {
    try {
        const url = "https://threeds2025-iot-leds.onrender.com/request";
        const response = await fetch(url);
        const data = await response.json(); // ✅ await aqui
        console.log(data); // ✅ agora mostra os dados reais

        const led = document.getElementById('estado_led');
        if (data.pedido === '1') {
            led.textContent = "Ligado";
        } else if (data.pedido === '0') {
            led.textContent = "Desligado";
        } else {
            led.textContent = "Valor desconhecido";
        }
    } catch (erro) {
        console.error("Erro ao obter dados:", erro);
    }
};

const alterarLampada = async () =>{
    const url = "https://threeds2025-iot-leds.onrender.com/get/estadoLuz"
    const response = await fetch(url)
    const data = await response.json()
    const luz = document.getElementById('luz')
    if (data.estado_luz == "ligadas"){
        luz.textContent = "Ligada!"
    }
    if (data.estado_luz == "desligadas"){
        luz.textContent = "Desligada!"
    }
}

setInterval(obterDados, 1000);