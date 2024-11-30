from datetime import date


def formatar_data_entrada(data: date):
    return '{:04}/{:02}/{:02}'.format(data.year, data.month, data.day)


def formatar_data_saida(data: date):
    return '{:02}/{:02}/{:04}'.format(data.day, data.month, data.year)
