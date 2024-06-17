# Padrões de commits 📜

De acordo com a documentação do **[Conventional Commits](https://www.conventionalcommits.org/pt-br)**, commits semânticos são uma convenção simples para ser utilizada nas mensagens de commit. Essa convenção define um conjunto de regras para criar um histórico de commit explícito, o que facilita a criação de ferramentas automatizadas.

## Tipo e descrição 

O commit semântico possui os elementos estruturais abaixo (tipos), que informam a intenção do seu commit ao utilizador(a) de seu código.

- `feat`- Commits do tipo feat indicam que seu trecho de código está incluindo um **novo recurso** (se relaciona com o MINOR do versionamento semântico).
- `fix` - Commits do tipo fix indicam que seu trecho de código commitado está **solucionando um problema** (bug fix), (se relaciona com o PATCH do versionamento semântico).
- `docs` - Commits do tipo docs indicam que houveram **mudanças na documentação**, como por exemplo no Readme do seu repositório. (Não inclui alterações em código).
- `test` - Commits do tipo test são utilizados quando são realizadas **alterações em testes**, seja criando, alterando ou excluindo testes unitários. (Não inclui alterações em código)
- `build` - Commits do tipo build são utilizados quando são realizadas modificações em **arquivos de build e dependências**.
- `perf` - Commits do tipo perf servem para identificar quaisquer alterações de código que estejam relacionadas a **performance**.
- `style` - Commits do tipo style indicam que houveram alterações referentes a **formatações de código**, semicolons, trailing spaces, lint... (Não inclui alterações em código).
- `refactor` - Commits do tipo refactor referem-se a mudanças devido a **refatorações que não alterem sua funcionalidade**, como por exemplo, uma alteração no formato como é processada determinada parte da tela, mas que manteve a mesma funcionalidade, ou melhorias de performance devido a um code review.
- `chore` - Commits do tipo chore indicam **atualizações de tarefas** de build, configurações de administrador, pacotes... como por exemplo adicionar um pacote no gitignore. (Não inclui alterações em código)
- `ci` - Commits do tipo ci indicam mudanças relacionadas a **integração contínua** (_continuous integration_).
- `raw` - Commits to tipo raw indicam mudanças relacionadas a arquivos de configurações, dados, features, parametros.
  
## Recomendações 🎉

- Adicione um tipo consistente com o título do conteúdo.
- Recomendamos que na primeira linha deve ter no máximo 4 palavras.
- Para descrever com detalhes, usar a descrição do commit.
- Usar um emoji no início da mensagem de commit representando sobre o commit.
- Os links precisam ser adicionados em sua forma mais autêntica, ou seja: sem encurtadores de link e links afiliados.

## Complementos de commits 💻

- **Rodapé:** informação sobre o revisor e número do card no Trello ou Jira. Exemplo: Reviewed-by: Elisandro Mello Refs #133
- **Corpo:** descrições mais precisas do que está contido no commit, apresentando impactos e os motivos pelos quais foram empregadas as alterações no código, como também instruções essenciais para intervenções futuras. Exemplo: see the issue for details on typos fixed.
- **Descrições:** uma descrição sucinta da mudança. Exemplo: correct minor typos in code

## Padrões Exeplificados💈

git commit -m ":tada: Commit inicial"	🎉 Commit inicial

git commit -m ":books: docs: Atualização do README"	   📚 docs: Atualização do README

git commit -m ":bug: fix: Loop infinito na linha 50"	🐛 fix: Loop infinito na linha 50

git commit -m ":sparkles: feat: Página de login"	✨ feat: Página de login

git commit -m ":bricks: ci: Modificação no Dockerfile"	   🧱 ci: Modificação no Dockerfile

git commit -m ":recycle: refactor: Passando para arrow functions"	♻️ refactor: Passando para arrow functions

git commit -m ":zap: perf: Melhoria no tempo de resposta"	⚡ perf: Melhoria no tempo de resposta

git commit -m ":boom: fix: Revertendo mudanças ineficientes"	  💥 fix: Revertendo mudanças ineficientes

git commit -m ":lipstick: feat: Estilização CSS do formulário"	  💄 feat: Estilização CSS do formulário

git commit -m ":test_tube: test: Criando novo teste"	🧪 test: Criando novo teste

git commit -m ":bulb: docs: Comentários sobre a função LoremIpsum( )"	  💡 docs: Comentários sobre a função LoremIpsum( )

git commit -m ":bulb: raw: RAW Data do ano aaaa"	 🗃️ raw: RAW Data do ano aaaa

# Templates de Pull Request
Podemos criar alguns templates para deixar padronizado os comentários que os desenvolvedores irão utilizar, dessa forma poderá aumentar a produtividade tanto da criação dos pull request, como também para facilitar a vida do responsável pela code review.

## Para bugs:
Resumo
Descrever rapidamente como ocorre o bug e qual foi a solução criada.

Checklist
- [ ] Eu adicionei|atualizei|corrigi os testes unitários do projeto (Se aplicável);
- [ ] Sem erros ou avisos no console após minha alteração;
- [ ] Tirei prints do antes e depois da correção do problema.[adicionar a screenshot]

## Para novas funcionalidades
Resumo
Escreva um breve resumo sobre o que foi alterado no sistema.

Checklist
- [ ] Eu adicionei|atualizei|corrigi os testes unitários do projeto (Se aplicável);
- [ ] Sem erros ou avisos no console após minha alteração;
- [ ] Tirei prints do antes e depois da correção do problema.[adicionar a screenshot]

# Padões de código

Para melhorar a organização dos arquivos, funções, performance e diminuir a chance de erros e conflitos, adotamos o Revealing Module Pattern do Christian Heilmann.

As vantagens desse pattern são: organização, clareza, performance, expõe publicamente apenas as funções e variáveis que se deseja e namespace único evitando sobrescrever métodos facilmente.

## Nomenclatura de pastas, arquivos, módulos e plugins

Um projeto pode ter muitos arquivos javascript, então é importante que estejam bem organizados desde o início, separados e bem nomeados.

A estrutura pode variar muito de projeto para projeto, mas as recomendações mínimas são:

Nomes dos arquivos na mesma língua em que são escritos;
Nomes sem camelCase;
Pastas separadas por tipos (bibliotecas/frameworks/plugins);
Plugins identificados por versão.
Exemplo:

	── javascripts
	   ├── libs
	   │   ├── jquery.min.js
	   │   └── underscore.min.js
	   │   └── highcharts.min.js
	   ├── plugins
	   │   ├── jquery.validate-1.2.js
	   │   ├── jquery.slider-3.1.js
	   │   └── jquery.validate.addicional-methods-0.8.js
	   ├── modules
	   │   ├── charts
	   │   |   ├── servers.js
	   │   |   └── transfer.js
	   │   ├── servers.js
	   │   └── servers.forms.js
	   ├── utils.js
	   └── main.js

## Seja compreensível
Use nomes de variáveis e funções auto explicativos e simples. Crie algum padrão e mantenha em todo o projeto.

Utilizamos variáveis e funções camelCase, pela facilidade de leitura, escrita e praticidade ao se trabalhar.

Exemplos:

Variáveis com nomes ruins:

// Curtos, posicionamento no código, abreviações e repetições de nome
var x1;
var campo1;
var campo2;
var latXY;

// Longos demais
var valorEixoXGraficoConsumo;
var campoTextoPrimeiroNome;
Funções com nomes ruins:

// Nomes que descrevem o código, nao o objetivo da função
function maiorDeDezoitoAnos(idade){
	return idade >= 18;
}
// É melhor descrever o objetivo
function possuiMaioridade(idade){
	return idade >= 18;
}

É uma boa ideia criar um padrão para suas variáveis e funções, como por exemplo:

// Variáveis com $ no início são elementos/objetos jQuery
var $header    = $('#header');
var $menuItens = $('#menu a');

// Maiúsculas para constantes
var PASTA_IMAGENS = '/assets/images/';
var NOME_CLIENTE = 'Fulano de Tal';

// _ no início para variáveis e funções privadas
var _contador = 0;

## Evite globais
No geral é uma péssima idéia, porque aumenta a chance de ter algo sobrescrito. Uma opção é utilizar closures e module pattern.

## Seja consistente no estilo de código
É possível escrever seu código de muitas maneiras, mas procure manter o mesmo estilo em todo seu projeto. Mantendo um padrão nos nomes, identacões, patterns, etc.

## Escreva os comentários necessários
É comum ouvir "Um bom código não precisa de explicação", mas na prática em projetos maiores, procure explicar a finalidade do seu código. Muitas pessoas, de diferentes níveis, podem ter que trabalhar no seu código e nem sempre elas tem experiência, tempo ou conhecimento do negócio para entender tudo. Facilite o desenvolvimento e manutenção comentando, mas não explicando o que ele faz, mas qual a regra de negócio.

Exemplo:

// Ruim: verifica se é maior de 18
// Bom: menores de idade sao redirecionados
if( idade >= 18 ){ ... }
Lembrando que comentários devem existir apenas na versão de desenvolvimento, devendo ser removidos no arquivo minificado que é entregue em produção.

## Use testes automatizados
Para criar e executar os testes unitários na linguagem Dart, precisamos instalar o pacote test. "flutter packages get". Referência: https://codelabs.developers.google.com/codelabs/flutter-app-testing?hl=pt-br#0
O Visual Studio dá suporte a duas estruturas de teste para Python, unittest e pytest (disponíveis no Visual Studio 2019 a partir da versão 16.3). Por padrão, nenhuma estrutura é selecionada quando você cria um projeto do Python. Referência: https://learn.microsoft.com/pt-br/visualstudio/python/unit-testing-python-in-visual-studio?view=vs-2022

## Configuração do ambiente

Para executar o projeto, será necessário instalar as dependências do requirements.txt, para isso, basta seguir os passos abaixo:

- Criar um ambiente virtual, digite o comando abaixo no terminal:
	- python -m venv venv
- Ativar o ambiente virtual:
	- venv\Scripts\activate   
- Instalar todas as dependências apenas no ambiente virtual:
	- pip install -r requirements.txt

## Configuração do arquivo .env

Será necessário criar um arquivo na raíz do projeto com o nome ".env", este arquivo será responsável por gerenciar todas informações de acesso ao banco de dados e SECRETS KEYS para funcionamento do JWT. Abaixo estão as variáveis que devem estar no arquivo:

DB_HOST
DB_NAME
DB_USER
DB_PASSWORD

Dependendo do e-mail de envio que vá usar, se é Gmail, Outlook, deverá preencher as seguintes váriaveis abaixo também:

EMAIL_GMAIL
PASSWORD_GMAIL (Esse password é um token que é gerado nas configurações do gmail para liberar o acesso)

EMAIL_OUTLOOK
PASSWORD_OUTLOOK (No caso do outlook é sua senha de acesso)

## Códigos de Retorno

    - 200 OK: A solicitação foi bem-sucedida.
    - 201 Created: A requisição foi bem sucedida e um novo recurso foi criado como resultado.
    - 400 Bad Request: O servidor não pode ou não irá processar a solicitação devido a algo que é percebido como um erro do cliente.
	- 500 Internal Server Error: O servidor encontrou uma situação com a qual não sabe lidar.

## Padronização de retorno

	- Erros:

		"erros": [
			{
			"coluna": "key",
			"message": "Este campo é obrigatório"
        	}
		]

	- Error:

		{
			"error":"error x"
		}

	- Success:

		{
			"success":"success y"
		}

## Routes

	- Login 
		- Endpoint: http://127.0.0.1:5000/login
		- Method: GET
		- Explanation: Nesse metódo, as informações de login e password devem ser passadas no body, conforme abaixo.
		- Return API: O retorno será apenas uma mensagem de "success" ou "error", caso tenha alguma key obrigatória faltando, será retornado um array de "erros". 
		- JSON format:
		{
  			"login": "teste",
  			"password": "123456"
		}

	- User
		- Endpoint 1: http://127.0.0.1:5000/user
		- Methods: POST
		- Explanation: Nesse método, as informações obrigatórias no json devem ser passadas conforme abaixo.
		- Return API: O retorno será o objeto completo que foi salvo no banco, incluindo o ID.
		- Endpoint 2: http://127.0.0.1:5000/user/<int:id>
		- Methods: GET, UPDATE, DELETE
		- Explanation: No método GET é necessário passar apenas o ID do objeto que deseja, no UPDATE é necessário passar o ID na URL e a key que quer alterar no body, no DELETE é necessário passar apenas o ID que será excluído.
		- Return API: No método GET será retornado apenas o objeto completo do ID específico, no UPDATE será retornado o usuário com a nova alteração ou uma mensagem de "error" ou um array de "erros" caso esteja faltando alguma key, já no DELETE apenas uma mensagem de "error" ou "success".
		- JSON format required fields:
		{
			"name": "Teste",
			"login": "teste",
			"password": "123456",
			"email": "teste@gmail.com",
			"phone": "12345678910",
			"id_profile": 1
		}

	- Recover Password
		- Endpoint: http://127.0.0.1:5000/recoverPassword/<string:email>
		- Method: GET, PUT
		- Explanation: No método GET será enviado o e-mail e devolvido o token, já no PUT, deve ser enviado o e-mail na URL e o novo password no body, conforme abaixo.
		- Return API: O retorno do método GET será uma key com "token" e um value com o token enviado para o e-mail do usuário ou uma mensagem de "error", já no UPDATE será retornado uma mensagem de "success" ou de "error". 
		- JSON format to PUT:
		{
  			"password": "123456"
		}

