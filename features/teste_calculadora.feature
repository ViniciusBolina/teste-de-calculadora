Feature: Teste de calculos

        Scenario: testanto soma
                Given os numeros 8 e 5
                When soma esses dois numeros
                Then é mostrado a soma desses dois numeros

        Scenario Outline: teste de multiplicação
                Given os numeros <s> e <r>
                When multiplicando os dois numeros
                Then é mostrado a multplicão desses dois numeros
        Examples: numeros
                | s | r |
                | 3 | 4 |
                | 6 | 1 |
                | 5 | 5 |
                | 1 | 2 |
    
        Scenario: teste de subtração
                Given os numeros
                | t  | u  |
                | 4  | 3  |
                | 10 | 2  |
                | 55 | 23 |
                | 9  | 2  |
                When o numero "u" subtrai de "t"
                Then é mostrado o valor da subtração

        Scenario Outline: teste de divisão
                Given o numero <numeros>
                When é divisivel por 2 
                Then o resto da divisão é
      
        Examples: tabela de numeros
                | numeros |
                |     2   |
                |     4   |
                |     7   |
                |    10   |
                |    11   |
                |    15   |
                |    22   |
