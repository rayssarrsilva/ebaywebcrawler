# eBay Web Crawler

## 📌 Descrição
O **eBay Web Crawler** é um **robô de raspagem de dados (web scraping)** desenvolvido em Python para coletar informações de produtos no eBay. Ele permite a extração de detalhes como nome do produto, preço, link e outras informações relevantes, facilitando análises e monitoramento de preços.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Selenium** (Automação de navegador)
- **BeautifulSoup** (Extração de dados HTML)
- **Requests** (Requisições HTTP)

## ⚙️ Funcionalidades
- 🔍 **Coleta automática de dados** de produtos no eBay.
- 📄 **Extração de detalhes**: nome, preço, link e outras informações.
- 📊 **Armazenamento estruturado** em CSV ou banco de dados.
- ⏳ **Execução programada** para monitoramento contínuo de preços.

## 📂 Estrutura do Projeto
```
ebaywebcrawler/
│── crawler/         # Código principal do web crawler
│── data/            # Armazenamento de dados extraídos
│── logs/            # Logs de execução
│── requirements.txt # Dependências do projeto
│── main.py          # Arquivo principal para execução
```

## 🚀 Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/rayssarrsilva/ebaywebcrawler.git
cd ebaywebcrawler
```

### 2️⃣ Criar e Ativar Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o Web Crawler
```bash
python main.py
```

## 🛠️ Melhorias Futuras
- Implementação de **proxy rotation** para evitar bloqueios.
- Suporte a múltiplas categorias de produtos.
- Exportação direta para **banco de dados SQL**.
- Interface gráfica para facilitar o uso.

## ⚠️ Aviso Legal
Este projeto é apenas para fins educacionais. O uso inadequado pode violar os **termos de serviço do eBay**. Sempre consulte as diretrizes do site antes de realizar raspagem de dados.

## 📄 Licença
Este projeto está sob a licença **MIT**. Contribuições são bem-vindas! 🚀

---
🔹 **Desenvolvido por Rayssa** | [GitHub](https://github.com/rayssarrsilva)
