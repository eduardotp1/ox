# Modulacao Digital
#### Eduardo Tirta, Gulherme Graicer
### Protocolo Uart
O protocolo tem um estado inicial de sinal 1, constante, para enviar um dado, ele envia um bit start de sinal 0, para indicar ao receptor que uma mensagem sera enviada, entao, logo apos, envia o payload, que sao uma sequencia de bits que formam um caracter, de acordo com a tabela ASCII, depois do evnio do payload, um bit de paridade eh enviado para poder identificar algum erro que pode ter ocorrido no processo de envio, deixando a informacao mais precisa e com menos erros, finalmente, um stop bit de sinal 1 eh enviado, o que faz retornar ao modo inicial
### Onda

### Descricao do codigo
