def preco_por_categoria(categoria):
    if categoria == 1:
        preco = 10
    else:
        if categoria == 2:
            preco = 18
        else:
         raise ValueError(f'categoria invaálida: (categoria)')
    return preco