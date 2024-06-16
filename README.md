# Guberman OS Automation

Este projeto usa Selenium para automatizar a criação de Ordens de Serviço (OS) em massa em um sistema web chamado Guberman. O script lê dados de uma planilha, executa o processo de criação no sistema web e devolve uma nova planilha com os números das OS geradas.

## Configuração

1. Crie um ambiente virtual:
   ```sh
   python -m venv venv

2. Ative o ambiente virtual:
- Windows:
  ```sh
  Copiar código
  .\venv\Scripts\Activate.ps1
- No macOS/Linux:
  ```sh
  Copiar código
  source venv/bin/activate```

3. Instale as dependências
   ```sh
   pip install selenium python-dotenv

4. Configure suas variáveis de ambiente no arquivo .env:
   ```python
   SYSTEM_URL=http://example.com
   SYSTEM_USER=seu-usuario
   SYSTEM_FILIAL=sua-filial
   SYSTEM_PASSWORD=sua-senha

5. Execute o script:
   ```sh
   python app.py

## Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests.

## Uso
Coloque sua planilha de dados no mesmo diretório do script, por exemplo, dados.xlsx.
Execute o script
```sh
    python app.py
