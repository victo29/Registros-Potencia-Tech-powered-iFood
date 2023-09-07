select now() as Timestamp;

create database if not exists manipulation;
use manipulation;

create table bankAccounts(
	id_account int auto_increment primary key,
    Ag_num int not null,
    Ac_num int  not null,
    Saldo float,
    constraint identification_account_constraint unique (Ag_num, Ac_num)
);
alter  table bankAccounts add LimiteCredito float not null default 500.00;

-- insert into bankAccounts(Ag_num,Ac_num,Saldo) values (156,264358,0);

create table bankClient(
	id_client int auto_increment,
    ClientAccount int,
    CPF char(11) not null,
    RG char(9) not null,
    Nome varchar(50),
    Endereco varchar(100),
    Renda_mensal float,
    primary key(id_client,ClientAccount),
    constraint fk_account_client foreign key (ClientAccount) references bankAccounts(id_account) on update cascade
    );
    alter table bankClient add UFF char(2) not null;
    
    -- insert into bankClient (ClientAccount,CPF, RG, Nome, 
    -- endereco, Renda_mensal, UFF) values (1,12345678913,123456789,'Roger Guedes', 'rua de baixo', 6500.5,'BA');
    
    
    
    CREATE TABLE bankTransactions(
	Id_transcation INT auto_increment PRIMARY KEY,
	Ocorrencia datetime,
	Status_transaction VARCHAR(20),
	Valor_transferido FLOAT,
	Source_account INT,
	Destination_account INT,
	CONSTRAINT fk_source_transaction foreign key (Source_account) REFERENCES
	bankAccounts(id_Account),
	CONSTRAINT fk_destionation_transaction foreign key (destination_account) REFERENCES
	bankAccounts(id_Account)
);
    

