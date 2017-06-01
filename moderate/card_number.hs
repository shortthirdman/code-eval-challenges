import System.Environment (getArgs)
import Data.Char (isDigit)

toDigits  :: Integer -> [Integer]
toDigits x | x < 0     = [-1]
           | x < 10    = [x]
           | otherwise = toDigits (div x 10) ++ [mod x 10]

toDigitsRev  :: Integer -> [Integer]
toDigitsRev x | x < 0  = [-1]
              | otherwise = reverse (toDigits x)

dobSec          :: [Integer] -> [Integer] -> [Integer]
dobSec xs []     = xs
dobSec xs [x]    = xs ++ [x]
dobSec xs (y:ys) = dobSec (xs ++ [y, 2 * head ys]) (tail ys)

sumDigits :: [Integer] -> Integer
sumDigits = foldr (\ x -> (+) (div x 10 + mod x 10)) 0

isValid  :: Integer -> String
isValid x | mod (sumDigits (dobSec [] (toDigitsRev x))) 10 == 0 = "1"
          | otherwise                                           = "0"

main :: IO ()
main = do
    [inpFile] <- getArgs
    input <- readFile inpFile
    putStr . unlines . map (isValid . read . filter isDigit) $ lines input
