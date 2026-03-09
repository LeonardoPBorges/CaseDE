# CaseDE
Criação de Projeto Case, referente a API do COINCAP.

------------------------------------------------
##CABEÇALHO  
#Criado por: Leonardo Borges  
#Data Criação: 09/03/2026  
#Version: Versão 01 -- criação do processo  
------------------------------------------------

------------------------------------------------
Atualização do Processo
------------------------------------------------

  A atualizaçao do processo deverá acontecer de segunda a sexta para não comprometer o saldo Total de Créditos disponiveis por/mês, que são 4.000 créditos.  
  Cada processamento irá utilizar me média de 60 créditos.  
  
------------------------------------------------
 Passos para a extração de Dados:
 ------------------------------------------------
   1°. Criar uma conta em: https://pro.coincap.io/dashboard  
   Após criar a conta crie a sua chave API em minha chaves API:    
   <img width="1407" height="157" alt="image" src="https://github.com/user-attachments/assets/70a1ad16-8c53-41f4-921a-676d3a0ac2c5" />  

   Após criar sua chave, entre em API coin CAP: https://pro.coincap.io/api-docs/   
   Para este projeto foi selecionado duas tabelas:  PREÇO e ATIVOS 
   
     Preço: Pontos de extremidade mínimos para obter um preço em USD por endereço + rede ou por símbolo.  
     Ativos: O preço do ativo é uma média ponderada pelo volume, calculada a partir da coleta de dados de negociação das bolsas. Cada bolsa contribui para esse preço proporcionalmente ao seu volume de negociação. Todos os valores são convertidos para USD e podem ser convertidos através do endpoint /rates.  

------------------------------------------------
Para a criação da API
------------------------------------------------
  Para a criação de API foi utilizado a Linguagem python, e o processo criado em VS Code.  
  
      -- Para os dados de Ativos foram utilizadas as seguintes regras disponiveis no arquivo: teste_api_coin_ativos.py  
      -- Para os dados de Preço foram utilizadas as seguintes regras disponiveis no arquivo: tete_api_coin_preço.py  

------------------------------------------------
Tratamento Dos Dados - Big Query
------------------------------------------------
  Para tratamento dos dados Foi utilizados os critérios referente as camadas Stage, Raw, e Trusted  
  
      -- Stage: Os dados forma levados de forma bruta, conforme os dados extraidos na API, sem transformações.  
      -- Raw: nesta camada os dados são replicados da Stage para a Raw, mantendo seu formato Original.  
      -- Trusted: Nesta camada foi realizado o tratamento de nome das colunas para o padrão, tipagem dos Dados, definido as Strings em NUMERIC, FLOAT, INT, DATE  
 
------------------------------------------------
Valização dos Dados em DataViz
------------------------------------------------
  Foi utilizado o Looker para a visualização dos dados em formatos acessiveis, e com visuais rápidos e de fácil entendimento.   
  Gerando alguns dados consolidados referentes as Criptomoedas e alguns Insghts relevante para os dados obtidos  
  Link do Dashboard: https://lookerstudio.google.com/u/1/reporting/27168d6a-71c8-4418-9fe5-c0633fddf858/page/UuTrF  
  
------------------------------------------------
END
------------------------------------------------
