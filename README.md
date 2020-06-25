# Trabalho Modelagem Estatística Avançada 
[Interface da simulação](https://modelagem-estatistica.herokuapp.com/)
## Introdução
Este programa simula a chegada de clientes a um banco, que possui alguns postos de atendimento (caixas). A fila é única para todos os caixas.
Os tempos entre chegadas de clientes segue uma distribuição normal, continua discreta, contínua ou exponencial.
A duração do atendimento a um cliente no caixa segue uma distribuição normal. 

Ao final, você encontra algumas sugestões de melhorias neste programa, que você pode fazer como exercício.

**eventos** 

É uma lista de eventos programados, sendo que cada evento
pode ser:


*   -1 é o evento da chegada de um cliente ao banco
*   0, 1, 2 ... é o evento do término do atendimento de um cliente
no caixa 0, 1, 2, ...




**horario_eventos**

É a lista dos horários em que ocorrerão os eventos programados na lista **eventos**. 

**caixas**

É uma lista dos caixas (postos de atendimentos). Cada caixa pode estar em um dos seguintes estados:
*   "livre"
*   "ocupado"
*   "fechado"

**fila**

É uma lista que contém os horários de chegada nos clientes que comporão a fila de atendimento. Serve para podermos medir o tempo de espera em fila. 

**horario**

Variável inteira com o horário atual. O tempo é medido em segundos, contados a partir do instante 0 (instante em que a simulação começou a ser executada).

**tempos_espera**

Lista que registra o tempo de espera na fila de cada cliente que vem ao banco. Se o cliente não encontrou nenhuma fila, registra zero. Unidade é minutos (e não segundos!). 

## Executar Aplicação Streamlit
> streamlit run stream.py