from main import fizbuzz

def test_divisible_3():
    assert fizbuzz(3) == "Fizz"
    assert fizbuzz(9) == "Fizz"

def test_divisible_5():
    assert fizbuzz(5) == "Buzz"
    assert fizbuzz(10) == "Buzz"

def test_divisible_3y5():
    assert fizbuzz(15) == "FizzBuzz"
    assert fizbuzz(30) == "FizzBuzz"

def test_no_divisible():
    assert fizbuzz(2) == "2"
    assert fizbuzz(7) == "7"

def test_0():
    # 0 es divisible por cualquier número, debería devolver FizzBuzz
    assert fizbuzz(0) == "FizzBuzz"

def test_fizz():
    assert fizbuzz(6) == "Fizz"

def test_buzz():
    assert fizbuzz(20) == "Buzz"

def test_fizzbuzz():
    assert fizbuzz(45) == "FizzBuzz"

def test_respuestanumero():
    assert fizbuzz(1) == "1"
    assert fizbuzz(4) == "4"
    
def test_fizz_es_string():
    resultado = fizbuzz(3)
    assert isinstance(resultado, str)

def test_buzz_es_string():
    resultado = fizbuzz(5)
    assert isinstance(resultado, str)

def test_fizzbuzz_es_string():
    resultado = fizbuzz(15)
    assert isinstance(resultado, str)

def test_numero_es_string():
    resultado = fizbuzz(2)
    assert isinstance(resultado, str)