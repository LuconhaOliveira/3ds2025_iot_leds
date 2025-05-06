#include<WiFi.h>
#include<WiFiMulti.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
const char* rede_wifi = "AAPM"; //O nome da rede Wifi
const char* senha_wifi = ""; //A senha da rede
unsigned long zero = 0;
char led = 21;
char ldr = 35;

WiFiMulti rede;

void conectarWiFi() {
  rede.addAP(rede_wifi, senha_wifi); //Inicia a conexão com a rede
  Serial.print("Conectando ao WiFi");

  while (rede.run() != WL_CONNECTED) { //Aguarda uma resposta
    delay(1000);
    Serial.print(".");
  }
  
  Serial.println("\nWiFi Conectado!");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
  Serial.print("MAC: ");
  Serial.println(WiFi.macAddress());
}

String requisitarDados() {
  HTTPClient http;
  http.begin("https://threeds2025-iot-leds.onrender.com/request");
  int httpResponCode = http.GET();
  if (httpResponCode == 200) {
    String respostaJson = http.getString();
    return respostaJson;
  } else {
    Serial.print("Erro HTTP: ");
    Serial.println(httpResponCode);
    return "";
  }
}

void enviarDados(bool luzAcesa) {
  HTTPClient http;
  if(luzAcesa){
    http.begin("https://threeds2025-iot-leds.onrender.com/luzSala/ligar");
  }else{
    http.begin("https://threeds2025-iot-leds.onrender.com/luzSala/desligar");
  }
  int httpResponCode = http.GET();
  if (httpResponCode == 200) {
    Serial.println("Deu certo! (LDR)");
  } else {
    Serial.print("Erro HTTP: ");
    Serial.println(httpResponCode);
  }
}

bool processarJSON(String json, DynamicJsonDocument& resultado) {
  DeserializationError error = deserializeJson(resultado, json);
  if (error) {
    Serial.print("Erro no JSON: ");
    Serial.println(error.c_str());
    return false;
  }
    return true;
}
void setup(){
  Serial.begin(115200); //Iniciando o serial para imprimir no monitor
  conectarWiFi();
  pinMode(led, OUTPUT);
  pinMode(ldr, INPUT);
}
void loop(){
  
  if (millis() - zero > 1000) {
    Serial.println(analogRead(ldr));
    if(analogRead(ldr)<=1000){
      enviarDados(true);
    }else{
      enviarDados(false);
    }
    String jsonRecebido = requisitarDados();
    
    DynamicJsonDocument resultado(256);

    if (processarJSON(jsonRecebido, resultado)) {
      String pedido = resultado["pedido"];
      if(pedido == "1"){
        digitalWrite(led,1);
      }else if(pedido=="0"){
        digitalWrite(led,0);
      }
    }

    zero = millis();
  }
}