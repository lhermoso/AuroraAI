# AuroraAI

Bem-vindo ao AuroraAI, um assistente pessoal revolucionário que redefine a maneira como interagimos com informações na internet. Utilizando tecnologias de ponta em inteligência artificial e conectado diretamente à OpenAI, o AuroraAI não se limita a apresentar resultados de buscas; ele compreende e atende as demandas dos usuários em tempo real, fornecendo respostas precisas e contextualizadas.

## Configuração do Projeto

Prepare seu ambiente para utilizar o AuroraAI seguindo estes passos simples.

### Pré-requisitos

- Python 3.8 ou superior.

### Configuração das Variáveis de Ambiente

1. **Clonar o Repositório**

   Faça o clone do repositório para sua máquina local.

2. **Arquivo de Variáveis de Ambiente**

   Duplique o arquivo `env-example` e renomeie a cópia para `.env`. Preencha as variáveis de ambiente conforme descrito:

   - `SERVER_API_DEV`: Obtenha gratuitamente em [Serper.dev](https://serper.dev/).
   - `OPEN_API_KEY`: Crie uma chave na [Plataforma OpenAI](https://platform.openai.com/api-keys) (custo aplicável).

3. **Instalação de Dependências**

   Execute o seguinte comando no terminal para instalar todas as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

### Execução do Projeto

Com as variáveis de ambiente configuradas e as dependências instaladas, navegue até o diretório do projeto e execute:

```bash
python main.py
```

## Como Usar o AuroraAI

Após iniciar o projeto, você será capaz de interagir com o AuroraAI através do terminal. Simplesmente digite sua pergunta e o AuroraAI buscará a melhor resposta para você. Para encerrar o programa, digite "sair".
