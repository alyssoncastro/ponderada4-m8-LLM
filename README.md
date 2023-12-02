# CHATBOT PARA NORMAS DE SEGURANÇAS EM AMBIENTES INDUSTRIAIS.

#### Autor: Alysson C. C. Cordeiro
##### ENGENHARIA DA COMPUTÇÃO - MÓDULO 8
###### Instituto de Tecnologia e liderança (INTELI).

### ESCOPO GERAL DO CHAT:

Um chatbot beseado em LLM usando a API  do ChatGPT, o qual foi desenvolvido para apenas responder sobre regras e normas da segurança do trabalho, além de utensílios e peças para manutenções.

### QUAIS FORAM AS TECNOLOGIAS?

1. Python 3.11
2. OpenAI
3. Gradio (Quickstart)
4. Miniconda
5. Langchain
6. Dotenv

### QUAIS AS FUNCIONALIDADES?

O chatbot está primeiramente com layout estilo de conversa de bots para o usuário ter uma experiência melhor. No campo "type a messager", o usuário digita uma saudação "oi!", "bom dia", entre outros.E existem 3 botões abaixo do campo: um para retrair, outro para pagar texto do campo digitado e outro para limpar as conversas. 

Ao enviar a mensagem, o usuário recebe em aproximadamente 5 segundos, uma resposta correspondente a que ele perguntou, que seria sobre segurança do trabalho. Caso contrário, será mostrado como resposta que é só possível responder se o assunto for relacionado ao ambiente de trabalho ou sistemas de manutenções.

### COMO DEVO INSTALAR?

1. Instale o Miniconda:

bach
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && bash Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

2. Faça a criação do seu ambiente Virtual e depois ative-o:

bash
conda create -n llm python=3.11
conda activate llm

3. Agora é só clonar meu repositório:

bash
git clone https://github.com/alyssoncastro/ponderada4-m8-LLM.git

cd ponderada4-m8-LLM/ponderada4-LLM


4. E rode com o comando:

bash
python3 interface.py


5. OBSERVAÇÃO:
bash
"Apenas rodará com eficácia se todas as bibliotecas, dependencias e importações estiverem já instaladas e configuradas!"

### VÍDEO:

https://drive.google.com/file/d/1-0C3jSxxFBOJ8Vjetj1ThYHk0iJMnqTs/view?usp=sharing


## NOTA

Agradecer ao professor Nicola pela paciencia de esperar essa atividade, na qual cumpri majoritariamente sozinho. Dando sempre feedback. E agradecê-lo pela compreensão do meu esforço. Mesmo projetinho ponderado não saindo perfeito.