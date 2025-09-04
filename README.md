
# Análise de Sentimentos com Azure AI Language Studio

### Objetivos do Projeto 

- Desenvolvido como parte do _bootcamp_ **Randstand - Análise de Dados/DIO** para o uso de ferramentas _Azure Speech Studio_ e
   _Azure Language Studio_ para análise de fala e linguagem natural. 

- Aplicaremos técnicas no Processamento de linguagem natural (PLN) para identificar e classificar sentimentos em textos com recursos de inteligência artificial na nuvem através da plataforma MS Azure.

### Tecnologias e Ferramentas Utilizadas

 
- Microsoft Azure AI Language Studio
- Microsoft Azure Speech Studio
- Git & GitHub
- Markdown
- VS Code

--- 

### Estudo de Caso: Duo Gourmet Delivery

```

Para tornar o projeto mais próximo de um cenário real, utilizei um conjunto de 303 avaliações reais coletadas no Duo Gourmet Delivery. Essas avaliações foram extraídas da base de dados do dashboard (dados devidamente anonimizados) e representam feedbacks genuínos de clientes sobre qualidade, atendimento e tempo de entrega.

```
 
---

### Etapas do Processo   

1. **Coleta**: As páginas de avaliações foram salvas manualmente no formato `.html` e armazenadas em `data/html_paginas`.  
      
      ``` Para garantir que os comentários estivessem presentes no HTML, o conteúdo foi copiado diretamente do elemento <article> no DevTools (HTML renderizado). ```    

2. **Extração**: O script `extrair_avaliacoes_v4.py` percorre todos os arquivos HTML e extrai:
   - Nome do cliente (anonimizado para `[cliente1]`, `[cliente2]`…)
   - Nota (estrelas)
   - Comentário (somente se houver texto)
   - Data da avaliação
3. **Limpeza**:
   - Remoção de avaliações sem comentário
   - Remoção de caracteres inválidos (`?` no lugar de emojis)
   - Padronização de espaços e quebras de linha
4. **Geração do dataset**: O resultado é salvo em `data/avaliacoes_duo_gourmet.csv`, pronto para análise no Azure Language Studio.

<br>
  
   >⚠️ Os arquivos HTML originais não foram incluídos no repositório por questões de **privacidade** e para manter o **projeto leve**. O script pode ser reutilizado com qualquer conjunto de páginas salvas em `.html`.

</br>

---

### Dependências

1. `pandas` — _manipulação de dados_
2. `beautifulsoup4` — _extração de conteúdo HTML_
3. `lxml` — _parser rápido para HTML/XML_

<br>

---

### Referências

1. [Guia de Markdown no GitHub](https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
2. [Documentação do Azure AI Language Studio](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/)
3. [Documentação do Azure Speech Studio](https://learn.microsoft.com/pt-br/azure/ai-services/speech-service/)