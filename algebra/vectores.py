"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos: Oriol Jiménez Garrich
    
    # Pruebas unitarias:

    >>> v1 = Vector([1, 2, 3])
    >>> v2 = Vector([4, 5, 6])

    >>> print(v1 * 2)
    [2, 4, 6]
    >>> print(v1 * v2)
    [4, 10, 18]

    >>> print(v1 @ v2)
    32
    >>> print(v2 @ v1)
    32

    >>> v1 = Vector([2, 1, 2])
    >>> v2 = Vector([0.5, 1, 0.5])
    >>> print(v1 // v2)
    [1.0, 2.0, 1.0]
    >>> print(v1 % v2)
    [1.0, -1.0, 1.0]
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other

    def __mul__(self, other):
        """
        Método para multiplicar el vector por un escalar o realizar el producto de Hadamard con otro vector.
        """
        if isinstance(other, (int, float)):
            return Vector(num * other for num in self)
        elif isinstance(other, Vector):
            return Vector(uno * otro for uno, otro in zip(self, other))# Hadmard
        # La funcio zip convina els elements de self i other en parells i després els multipliquem retornant el nou vector 

    __rmul__ = __mul__

    def __matmul__(self, other):
        """
        Calcula el producte escalar entre dos vectors
        """
        suma = 0

        if isinstance(other, Vector):
            for uno, otro in zip(self, other):
                suma += uno * otro
        return suma
    
    __rmatmul__ = __matmul__


    def __floordiv__(self, other):
        """
        Devuelve la componente de v1 (self) paralela a v2 (other)
        """
        if isinstance(other, Vector):
            return ((self @ other) / (other @ other)) * other
        # Primero con self @ other hacemos el producto escalar (numerador de la formula)
        # Luego con other @ other hacemos el módulo al quadrado (denominador)
        # Por último, multiplicamos por el vector other (multiplicación de Hadmard para tener un vector)
        
    def __mod__(self, other):
        """
        Devuelve la componente de v1 (self) perpendicular a v2 (other)
        """
        if isinstance(other, Vector):
            return self - (self // other)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

