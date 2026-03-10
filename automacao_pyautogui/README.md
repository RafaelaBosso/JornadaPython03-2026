# RPA Job Posting Automation

Automação em Python para preenchimento automático de anúncios de vagas no site  
https://rpaexercise.aisingapore.org/.

Este projeto foi desenvolvido como exercício prático de **Robotic Process Automation (RPA)** utilizando Python e a biblioteca **PyAutoGUI**, automatizando a criação de anúncios de emprego a partir de dados armazenados em um arquivo CSV.

O projeto foi construído como parte da minha jornada de aprendizado em Python após concluir o mini curso **"Jornada Python" da Hashtag Treinamentos**, onde tive o primeiro contato com automação de tarefas. Neste projeto, fui além do conteúdo do curso, implementando **condicionais para lidar com dropdowns e checkboxes** no formulário web.

---

# Demonstração da Automação

A automação realiza as seguintes etapas:

1. Abre o navegador **Firefox**
2. Acessa a página de login do exercício
3. Realiza o login automaticamente
4. Lê os dados do arquivo `datatable.csv`
5. Preenche o formulário de criação de vagas
6. Seleciona dropdowns e checkboxes com base nos dados
7. Submete os anúncios automaticamente
8. Repete o processo para todas as linhas do CSV

---

# Tecnologias utilizadas

- Python
- PyAutoGUI
- Pandas
- Firefox

---

# Observações Importantes

- A automação depende da posição dos elementos na tela, portanto mudanças de resolução podem afetar o funcionamento.

- Recomenda-se executar com resolução Full HD (1920x1080).

- O navegador utilizado no desenvolvimento foi o Firefox.

- **Durante a execução não utilize o mouse ou teclado, pois isso pode interferir no fluxo da automação.**
