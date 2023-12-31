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

### Exemplos
- [Exemplos](./OCP/README.md)

## Liskov Substitution Principle
Este princípio tem como base a ideia de que a substituição de um objeto por um de seus herdeiros não deve quebrar a sua aplicação. O que isso quer dizer ? Isso no diz que embora maneira que as classes herdeiras implementa os métodos mudam, elas ainda devem respeitar o comportamento da classe pai, trazendo o mesmo tipo de retorno e implementando os mesmo métodos, para que assim, caso seja necessário uma substituição  de um objeto pelo outro, a implementação ocorra de forma simples e fácil.

"Uma classe derivada pode ser substituivel por sua classe base"
> "Let q(x) be a property provable about objects of x of type T. Then q(y) should be provable for objects y of type S where S is a subtype of T."

### Restrições e contratos
Para que as necessidades desse pilar sejam cumpridas, temos que ter em mente a ideia de regras e contratos das nossas classes abtratas/base, onde algum pontos são limitantes quanto ao escopo das subclasses, como por exemplo as assinaturas dos metodos e os comportamentos condicionais.

Quanto a assinatura dos metodos:
- Os argumentos das subclasses tem que ser iguais ou mais genericas do que as classes base
- Os valores retornados devem ser iguais ou mais restritivos do que as da classe base 
- Nenhuma exceção deve ser gerada pelas subclasses

Quanto ao comportamento condicional:
- pre condições não podem ser mais fortes em uma classe derivada
- pos condições não podem ser mais fracas em uma classe derivada
- Invariaveis da classe base devem ser preservadas nas subclasses
- O estado da classe base deve ser preservado se tal restrição existir nela

## Interface Segregation Principle
Neste princípio falamos sobre boas práticas ao criar contratos de interface, onde uma interface não deve implementar métodos que suas subclasses não irão utilizar.

> “Clients should not be forced to depend upon interfaces that they do not use.”

Sendo assim, interfaces devem ser muito bem planejadas, e caso em uma classe seja necessário implementar um método que não será utilizado, logo o código viola o princípio deve ser refatorado.



## Dependency Inversion Principle
Esse princípio diz respeito sobre a dependência entre módulos, ele nos diz que módulos de alto nível ( normalmente módulos de lógica ou que unificam os processos ) não devem depender de módulos de baixo nível ( Módulos que comprem tarrafas específicas ). E que ambos os módulos devem depender de abstrações ao invés disso.

>High-level modules should not depend on low-level modules. Both should depend on abstractions.
>Abstractions should not depend on details. Details should depend on abstractions.

Isso nos diz que, ao criarmos abstrações ( interfaces ) para intermediar a comunicação, nos tiramos da classe de alto nível a dependência que ela tem da classe de baixo nível, externalizando essa dependência em um contrato abstrato ( não detalhado )  que é a interface, assim a classe de baixo nível é obrigada a implementar as necessidades específicas da classe de alto nível de maneira desacoplada, viabilizando inclusive diferentes implementações dessa dependência.


## Fontes
- https://softwareengineering.stackexchange.com/questions/395419/how-can-a-class-have-multiple-methods-without-breaking-the-single-responsibility
- https://softwareengineering.stackexchange.com/questions/345018/when-using-the-single-responsibility-principle-what-constitutes-a-responsibili