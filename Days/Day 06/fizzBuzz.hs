-- FizzBuzz rules:
-- print numbers from 1 to 100
-- if number is divisible by 3, print Fizz
-- if number is divisible by 5, print Buzz
-- if number is divisible by 3 and 5, print FizzBuzz
-- otherwise, print the number

fizzBuzz :: Int -> String
fizzBuzz n | n `mod` 15 == 0   = "FizzBuzz"
        | n `mod` 3  == 0      = "Fizz"
        | n `mod` 5  == 0      = "Buzz"
        | otherwise            = show n

main :: IO()
-- main = mapM_ putStrLn $ map fizzBuzz [1..100]
main = do putStrLn $ unlines (map fizzBuzz [1..100]) 
