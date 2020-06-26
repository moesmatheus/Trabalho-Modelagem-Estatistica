import streamlit as st
from Fila import Fila
from matplotlib import pyplot as plt
import pandas as pd

def main():

    st.title('Simulação de Fila')


    t_chegada_media = 160
    t_chegada_minimo = 50
    t_chegada_maximo = 150
    t_chegada_dp = 30
    # Sidebar
    st.sidebar.header('Selecionar Variáveis')
    n_caixas = st.sidebar.slider('Número de Caixas', 1, 10, 3)
    t_simulacao = st.sidebar.slider('Tempo Simulação (h)', 0.0, 10.0, 3.0)
    p_preferencial = st.sidebar.slider('Proporção de clientes preferênciais', 0.0, 1.0, .1)
    st.sidebar.subheader('Chegada')
    dist_chegada = st.sidebar.selectbox('Distribuição Chegada', ['gauss-norm','uniforme discreta', 'uniforme continua', 'exponencial'])
    if dist_chegada == 'gauss-norm' or dist_chegada == 'exponencial':
        t_chegada_media = st.sidebar.slider('Tempo médio de chegada', 30, 300, 50)

    if dist_chegada == 'uniforme discreta' or dist_chegada == 'uniforme continua':
        t_chegada_minimo = st.sidebar.slider('Tempo mínimo de atendimento', 50, 300, 50)
        t_chegada_maximo = st.sidebar.slider('Tempo máximo de atendimento', t_chegada_minimo, 300, max(150, t_chegada_minimo))

    if dist_chegada == 'gauss-norm':
        t_chegada_dp = st.sidebar.slider('Desvio padrão do tempo de chegada', 0, 100, 10)


    st.sidebar.subheader('Atendimento')
    t_saida_media = st.sidebar.slider('Tempo médio de atendimento', 50, 300, 170)
    t_saida_dp = st.sidebar.slider('Desvio padrão tempo atendimento', 0, 50, 30)

    descricao = st.checkbox('Mostrar Descrição')
    if descricao:
        st.markdown(
'''
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
'''
        )

    f = Fila(
            n_caixas = n_caixas, 
            t_chegada_media = t_chegada_media, 
            t_chegada_dp = t_chegada_dp, 
            t_chegada_minimo = t_chegada_minimo, 
            t_chegada_maximo = t_chegada_maximo, 
            dist_chegada = dist_chegada, 
            t_saida_media = t_saida_media, 
            t_saida_dp = t_saida_dp, 
            p_preferencial = p_preferencial
        )

    f.simulacao(t_simulacao)

    st.subheader('Ao fim da simulação:')
    st.markdown(f"**Tamanho da fila:** {len(f.fila)}") # imprime tamanho da fila
    st.markdown(f"**Caixas:** {f.caixas}")             # imprime situação dos caixas
    st.markdown(f"**Duracao:** {f.horario/60/60:.2f} h")
    st.markdown(f"**Total de clientes:** {len(f.tempos_espera)}")
    st.markdown(f"**Tempo máximo de espera na fila:** {max(f.tempos_espera):.1f} min")
    st.markdown(f"**Tempo médio de espera na fila:** {sum(f.tempos_espera)/len(f.tempos_espera):.1f} min")

    # gera histograma dos tempos de espera na fila
    plt.hist(f.tempos_espera, 
                #bins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
            )
    plt.title('Histograma dos tempos de espera na fila')
    plt.xlabel("Tempo de espera na fila para ser atendido (minutos)")
    plt.ylabel("Contagem de clientes")
    plt.grid(True)
    st.pyplot()


    # gera line plot dos tempos de espera na fila
    plt.plot(f.tempos_espera, 'ro', markersize=3)
    plt.title('Timeplot dos tempos de espera na fila')
    plt.xlabel("Número de ordem de chegada dos clientes")
    plt.ylabel("Tempo de espera na fila para ser atendido (minutos)")
    plt.grid(True)
    plt.grid(True)
    st.pyplot()

    plt.title('Intervalo de chegadas (s)')
    plt.hist(f.log_tempo_chegada)
    plt.xlabel("Intervalo de chegadas (s)")
    plt.ylabel("Contagem de clientes")
    plt.grid(True)
    st.pyplot()

    plt.title('Tempo de atendimentos')
    plt.hist(f.log_tempo_atendimentos)
    plt.xlabel("Tempo de atendimento (s)")
    plt.ylabel("Contagem de clientes")
    plt.grid(True)
    st.pyplot()

    plt.plot(f.log_fila, 'ro', markersize=3)
    plt.title('Tamanho da Fila')
    plt.xlabel("Número de ordem de chegada dos clientes")
    plt.ylabel("Tamanho da Fila")
    plt.grid(True)
    plt.grid(True)
    st.pyplot()


if __name__ == '__main__':

    main()