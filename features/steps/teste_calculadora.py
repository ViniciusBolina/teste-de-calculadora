from pyexpat import model
from behave import *

@given('os numeros {x} e {y}')
def step_impl(context, x, y):
    context.x = int(x)
    context.y = int(y)
    
@when('soma esses dois numeros')
def step_impl(context):
    context.soma = context.x + context.y
    
@then('é mostrado a soma desses dois numeros')
def step_impl(context):
    print(context.soma)

@given('os numeros {s} e {r}')
def step_impl(context, s, r):
    context.r = int(r)
    context.s = int(s)

@when('multiplicando os dois numeros')
def step_impl(context):
    context.multplica = context.r * context.s

@then('é mostrado a multplicão desses dois numeros')
def step_impl(context):
    print(context.multplica)

#para arrumar
@given('os numeros')
def step_impl(context):
    for row in context.table:
        context.t=int(row['t'])
        context.u=int(row['u'])
        
@when('o numero "u" subtrai de "t"')
def step_impl(context):
        context.subtracao = context.t - context.u
        
@then('é mostrado o valor da subtração')
def step_impl(context):
    print(context.subtracao)

@given('o numero {numeros}')
def step_impl(context, numeros):
    context.numeros = int(numeros)

@when('é divisivel por 2')
def step_impl(context):
    if context.numeros%2 == 0:
        context.resto = 0
    else:
        context.resto = context.numeros%2
    
@then('o resto da divisão é')
def step_impl(context):
    print(context.resto)
