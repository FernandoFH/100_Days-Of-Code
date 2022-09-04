-- pattern matching 

imprimirNumeroDeLaSuerte :: Int -> String
imprimirNumeroDeLaSuerte 7 = "Numero de la suerte"
imprimirNumeroDeLaSuerte x = "No es el numero de la suerte"

sumaTotalOps :: Int -> Int -> Int 
sumaTotalOps 0 y = y 
sumaTotalOps x y = sumaTotalOps (x-1) (y+x)

--  deconstructores
data Peso = PesoEnKg Float | PesoEng Float 

mostrarPesoKg :: Peso -> IO ()
mostrarPesoKg (PesoEnKg x) = putStrLn (show x)
mostrarPesoKg (PesoEng x) = putStrLn (show (x/1000))



