create schema bd_teste2;

use bd_teste2;

create table  usuarios (
ID_Usuario int not null unique auto_increment primary key,
Nome varchar (150) not null,
Usuario varchar (150) not null unique,
permissao varchar(150) not null,
Email varchar (150) not null unique,
Senha varchar (150) not null,
CPF varchar (150) not null unique, 
BDAY varchar (150) not null
);

create table  clientes (
ID_Cliente int not null unique auto_increment primary key,
Nome varchar (150) not null,
CPF varchar(20) not null unique,
Email varchar (150) not null unique,
Telefone varchar (150) not null,
Endereco varchar (150) not null
);

create table quartos (
ID_Quartos int not null unique auto_increment primary key,
Numero int not null, 
Tipo varchar (150) not null, 
Status_Quarto varchar (150) not null,
Valor_Tipo float not null, 
Capacidade_Quarto varchar (150) not null, 
Descricao varchar (150) not null
);

create table reserva (
ID_Reserva int not null unique auto_increment primary key,
Data_Checkin date,
Data_Checkout date,
Valor_Reserva float not null,
Status_reserva varchar(150) not null,

ID_Cliente int,
foreign key (ID_Cliente) references clientes (ID_Cliente)
);

create table reserva_quartos (
ID_Reserva int,
ID_Quartos int,
foreign key (ID_Reserva) references reserva (ID_Reserva),
foreign key (ID_Quartos) references quartos (ID_Quartos)
);

create table financeiro (
ID_Pagamento int not null unique auto_increment primary key,
Data_Pagamento date not null,
Valor_Recebido float not null,
Valor_Devolvido float not null,
Tipo_Pagamento varchar (150) not null,
Quant_parcelas varchar (150) not null,
Bandeira_cartao varchar (150) not null,
codigo_pagamento varchar (150) not null,
Status_Pagamento varchar (150) not null,

ID_cliente int,
ID_Reserva int, 
foreign key (ID_Cliente) references clientes (ID_Cliente),
foreign key (ID_Reserva) references reserva (ID_Reserva)
);