-- pipe operation para componer funciones 

duplicarLista :: [Int] -> [Int]
duplicarLista = map (* 2)

filtarParesLista :: [Int] -> [Int]
filtarParesLista = filter (\x -> (mod x 2) == 0)

incremetarLista :: [Int] -> [Int]
incremetarLista = map succ 


