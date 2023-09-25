# SOLID

## Single Responsibility Principle
Esse princípio diz respeito ao escopo de uma Classe, de maneira que cada Classe seja responsável apenas por uma responsabilidade. Se existe mais de uma responsabilidade em uma classe (ou motivo para ela ser alterada), a mesma já está violando o princípio e deve ser refatorada.


>"A module should be responsible to one, and only one, actor."
>"A class should have only one reason to change".


As duas frases acima dizem respeito ao como delimitar o escopo de uma classe. Importante não confundir, o Single Responsibility Principle não diz respeito a classes terem apenas um único método, esse princípio diz respeito a uma classe englobar métodos que digam respeito a um mesmo conceito, de maneira que toda vez que aquele conceito seja alterado, uma unica classe sera responsavel por esse conceito, sendo ela a unica afetada, e esta mesma classe sé será afetada pela alteração desse unico conceito.

Um bom exemplo é descrito em um tópico no site [softwareengineering](https://softwareengineering.stackexchange.com/questions/345018/when-using-the-single-responsibility-principle-what-constitutes-a-responsibili), caso seja requisitado que mudemos o banco de dados de Mysql para Oracle, quantas classes terão que ser alteradas ? Se respeitado o SRP, apenas uma. A ideia é que a classe que faça a conexão no padrão sql com o banco tenha sua responsabilidade encapsulada em apenas uma classe, sendo assim, a única afetada caso haja uma mudança. Outro bom exemplo é, aparece um requisito para alterar o cálculo de uma bonificação salarial de um funcionário junior, se essa alteração tiver um efeito cascada, onde mais de uma classe seja modificada, provavelmente não está de acordo com o SRP, porém se o principio for respeitado, muito provavelmente uma única classe responsável pela cálculo dessa bonificação tera que ser alterada.

### Exemplos
- [Exemplos](./SRP/README.md)

## Open/Close Principle

Este princípio, também conhecido como OCP, nos fala que, ao criarmos uma entidade, seja ela uma função, um módulo ou uma classe, a mesma deve ser aberta a extensão porém fechada a modificação. Isso quer dizer que, conforme sua aplicação vá escalando, suas entidades devem ser facilmente extensíveis, sem que isso modifique sua estrutura.

>"Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification"
>"You should be able to extend a classes behavior, without modifying it."

Existem muitas maneiras de respeitarmos esse princípio, embora não seja nem um pouco fácil implementá-lo na prática. Um dos exemplos mais comuns é o uso de interface e herança, para que quando novos modelos surgirem, elas herdem a classe/interface para assim não alterar a original e respeitar assim o código legado já existente. Outro exemplo é a utilização de diferentes versões de uma mesma funcionalidade, mantendo a original inalterada mas reaproveitando a estrutura que a compõem para uma nova versão. 
## Liskov Substitution Principle

## Interface Segregation Principle

## Dependecy Inversion Principle

## Fontes
- https://softwareengineering.stackexchange.com/questions/395419/how-can-a-class-have-multiple-methods-without-breaking-the-single-responsibility
- https://softwareengineering.stackexchange.com/questions/345018/when-using-the-single-responsibility-principle-what-constitutes-a-responsibili