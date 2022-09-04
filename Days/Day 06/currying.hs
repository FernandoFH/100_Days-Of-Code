-- currying

sumarTresNumeros :: Int -> Int -> Int -> Int
sumarTresNumeros x y z = x + y + z

sumarYMostrarPrivate driver x y = driver (show (x + y))

sumarYMostrar = sumarYMostrarPrivate putStrLn
