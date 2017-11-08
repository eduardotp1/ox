#include "sw_uart.h"
#pragma GCC optimize ("-O3")

void sw_uart_setup(due_sw_uart *uart, int rx, int tx, int stopbits, int databits, int paritybit) {
	uart->pin_tx     = tx;
	uart->pin_rx     = rx;
	uart->stopbits   = stopbits;
	uart->paritybit  = paritybit;
  uart->databits   = databits;
  pinMode(rx, INPUT);
  pinMode(tx, OUTPUT);
  digitalWrite(tx, HIGH);
}

void sw_uart_write_data(due_sw_uart *uart, char* bufferData, int writeN) {
  for(int i = 0; i < writeN; i++) {
    sw_uart_write_byte(uart, bufferData[i]);
  }
}

void sw_uart_write_string(due_sw_uart *uart, char* stringData) {
  sw_uart_write_data(uart, stringData, strlen(stringData));
}

// Funcao para calcular paridade impar
// retorna paridade
int calc_odd_parity(char data) {
  int soma;
  for(int i = 0; i < 8; i++) {
    soma += data >> i & 0X01;
  }
  if(soma % 2 == 0) {
    return 1;
  }
  else {
    return 0;
  }
}

// Funcao para enviar um char (data 8 bits) via uart
void sw_uart_write_byte(due_sw_uart *uart, char data) {
  
  // variável para armazenar paridade
  int parity = 0;

  // atualiza valor da paridade
  if(uart->paritybit == SW_UART_ODD_PARITY) {
     parity = calc_odd_parity(data);
  } else if(uart->paritybit == SW_UART_EVEN_PARITY) {
     parity = !calc_odd_parity(data);
  }
  
  // envia start bit
  digitalWrite(uart -> pin_tx, LOW);
  _sw_uart_wait_T(uart);
  
  // envia payload
  for(int i = 0; i < uart->databits; i++) {
    int pay = data >> i & 0X01;
    digitalWrite(uart -> pin_tx, pay);
    _sw_uart_wait_T(uart);
  }

  // envia paridade, se existir
  if(uart->paritybit != SW_UART_NO_PARITY) {
    digitalWrite(uart -> pin_tx, parity);
  }
  
  // envia stop bit, se existir
  for(int i = 0; i < uart->stopbits; i++) {
    digitalWrite(uart -> pin_tx, HIGH);
  } 
}

// MCK 21MHz
// 1093 para baudrate 9600/2
void _sw_uart_wait_half_T(due_sw_uart *uart) {
  for(int i = 0; i < 1093; i++){
    asm("NOP");
  }
}

void _sw_uart_wait_T(due_sw_uart *uart) {
  _sw_uart_wait_half_T(uart);
  _sw_uart_wait_half_T(uart);
}

