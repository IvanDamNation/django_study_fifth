from django import template

register = template.Library()


@register.filter(name='censor')
def censor(value):
    value1 = (str(value)).split()
    with open('censor_list.txt') as f:
        censor_list = f.read().split(",\n")

    for i, word in enumerate(censor_list):
        for j, word1 in enumerate(value1):
            if word1 == word:
                value1[j] = "*****"

    value = ' '.join(value1)
    return str(value)
