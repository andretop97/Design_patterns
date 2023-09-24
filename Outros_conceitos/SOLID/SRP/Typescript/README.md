# Exemplo em Typescript
Neste exemplo Simples criamos duas classes, uma responsável pelo escopo de cliente e outra responsável pelo escopo de notificação, como podemos ver, os métodos relacionadas ao CRUD do client estão com sua responsabilidade encapsuladas na classe Client, sendo assim, toda vez que for preciso alterar o conceito de cliente é nessa classe que atuamos. O mesmo se aplica a classe de Notify, neste exemplo ela encapsula a responsabilidade por enviar a notificação através de diferentes métodos, seria interessante neste exemplo também encapsular em uma classe diferente o conector entre a aplicação e o serviço de envio de notificação, para que assim, quando for preciso alterar a conexão que envia o SMS por exemplo, a única classe afetada seja o conector, sem afetar a classe notify.
