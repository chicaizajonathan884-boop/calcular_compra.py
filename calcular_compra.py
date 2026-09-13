def calcularCompra(precio, cantidad):
    total = precio * cantidad
    return total 


if __name__ == "__main__":
    precio = 5
    cantidad = 3

    resultado = calcularCompra(precio, cantidad)

    print("El total de la compra es:", resultado, "dólares")
    