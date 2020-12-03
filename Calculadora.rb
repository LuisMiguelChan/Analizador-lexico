class Calculadora
 
    # Se declaran las variables de la clase
    attr_accessor :x, :y
    
    def suma
     temp = x + y
     puts "La suma de es: #{temp}"
    end
    
    def resta
     temp = x - y
     puts "La resta es: #{temp}"
    end
    
    def multiplicacion
     temp = x * y
     puts "La multiplicacion es: #{temp}"
    end
    
    def division
     temp = x / y
     puts "La division es: #{temp}"
    end
    
    def modulo
     temp = x % y
     puts "El modulo es: #{temp}"
    end
    
    def potencia
     temp = x ** y
     puts "La potencia es: #{temp}"
    end

    def igual
        if x==y
            puts "los numeros son iguales"
        else
            puts"Los numeros no son iguales"
    end
    
   end
    
   # Hacemos un objeto y utilizamos sus atributos y metodos
   puts""
   puts "Con numeros decimales"
   calc = Calculadora.new
   calc.x = 3.157
   calc.y = 2.14
   calc.suma
   calc.resta
   calc.multiplicacion
   calc.division
   calc.modulo
   puts""
   puts "Con numeros enteros"
   calc2 = Calculadora.new
   calc2.x = 6
   calc2.y = 3
   calc2.suma
   calc2.resta
   calc2.multiplicacion
   calc2.division
   calc2.modulo
   puts""
   puts "comparacion"
   calc3 = Calculadora.new
   calc3.x = 5
   calc3.y = 7
   calc3.igual
end