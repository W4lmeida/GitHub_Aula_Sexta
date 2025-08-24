# 📘 Resumo de Comandos - CMD e Git/GitHub

Este guia reúne os principais comandos do **Prompt de Comando (CMD - Windows)** e do **Git/GitHub**, para uso em estudos e projetos.

### API's

* `endpoint` → O mesmo que o link da API que vamos consumir
* `api_key` → Algumas API's precisam de key, para poderem ser usadas

---

## 📌 Exemplos de endpoints:

* `Texto` → https://api.cohere.ai/v1/generate → geração de texto
* `Chat` → https://api.cohere.ai/v1/chat → chat estilo GPT
* `Resumo` → https://api.cohere.ai/v1/summarize → resumo de textos
* `Vetor` → https://api.cohere.ai/v1/embed → transformar texto em vetores
* `Classificar Texto` → https://api.cohere.ai/v1/classify → classificar texto
* `Rankear DOC's` → https://api.cohere.ai/v1/rerank → ranqueamento de documentos

---

## 🖥️ Comandos do CMD (Windows)

### 📂 Gerenciamento de pastas e arquivos

* `dir` → lista arquivos e pastas do diretório atual
* `cd nome_da_pasta` → entra em uma pasta
* `cd ..` → volta uma pasta
* `mkdir nome_da_pasta` → cria pasta
* `rmdir nome_da_pasta` → apaga pasta vazia
* `del arquivo.txt` → apaga um arquivo
* `ren antigo.txt novo.txt` → renomeia arquivo

### 📄 Criar arquivos

* `type nul > arquivo.txt` → cria arquivo vazio
* `echo texto > arquivo.txt` → cria arquivo com texto (sobrescreve)
* `echo texto >> arquivo.txt` → adiciona texto no final do arquivo
* `copy con arquivo.txt` → cria arquivo interativo (finaliza com **CTRL+Z** e Enter)

### ⚡ Outros úteis

* `cls` → limpa a tela
* `exit` → fecha o CMD
* `help` → mostra lista de comandos disponíveis
* `help nome_comando` → mostra ajuda de um comando

---

## 🐙 Comandos do Git/GitHub

### 🔧 Configuração inicial

* `git config --global user.name "Seu Nome"`
* `git config --global user.email "seuemail@example.com"`

### 📂 Criar/Clonar repositórios

* `git init` → inicia um repositório local
* `git clone URL` → clona um repositório do GitHub

### 📄 Controle de versões

* `git status` → mostra alterações no repositório
* `git add arquivo.txt` → adiciona arquivo para commit
* `git add .` → adiciona todos os arquivos
* `git commit -m "mensagem"` → salva alterações no histórico / confirma só o que já está na área de staging (git add)
* `git commit -a -m "msg"` → pula o git add e inclui automaticamente arquivos rastreados modificados/deletados / Funciona apenas quando atualizei um arquivo que já está no repositório, e quero atualizar ele no git também

### 🔄 Enviar e receber do GitHub

* `git remote add origin URL` → conecta repositório local ao GitHub
* `git push -u origin main` → envia commits para a branch *main* no GitHub
* `git pull origin main` → baixa últimas alterações do GitHub

### 🌱 Branches

* `git branch` → lista branches
* `git branch nome` → cria branch
* `git checkout nome` → troca para a branch
* `git merge nome` → mescla branch com a atual

### 🗑️ Desfazer alterações

* `git reset arquivo.txt` → remove arquivo da área de staging
* `git checkout -- arquivo.txt` → descarta alterações no arquivo
* `git reset --hard` → volta ao último commit (⚠️ perigoso, apaga mudanças)

---

📌 **Dica**: Use CMD para gerenciar arquivos/pastas e Git para versionar e sincronizar com o GitHub.
