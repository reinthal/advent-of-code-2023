import Data.List

computeNumberAuxLeft :: String -> String
computeNumberAuxLeft [] = "0"
computeNumberAuxLeft xs
            | [head xs] `elem` map show [0..9] = [head xs]
            | "one" `isPrefixOf` xs = "1"
            | "two" `isPrefixOf` xs = "2"
            | "three" `isPrefixOf` xs = "3"
            | "four" `isPrefixOf` xs = "4"
            | "five" `isPrefixOf` xs = "5"
            | "six" `isPrefixOf` xs = "6"
            | "seven" `isPrefixOf` xs = "7"
            | "eight" `isPrefixOf` xs = "8"
            | "nine" `isPrefixOf` xs = "9"
            | "zero" `isPrefixOf` xs = "0"
            | otherwise = computeNumberAuxLeft $ tail xs

computeNumberAuxRight :: String -> String
computeNumberAuxRight [] = "0"
computeNumberAuxRight xs 
            | [last xs] `elem` map show [0..9] = [last xs]
            | "one" `isSuffixOf` xs = "1"
            | "two" `isSuffixOf` xs = "2"
            | "three" `isSuffixOf` xs = "3"
            | "four" `isSuffixOf` xs = "4"
            | "five" `isSuffixOf` xs = "5"
            | "six" `isSuffixOf` xs = "6"
            | "seven" `isSuffixOf` xs = "7"
            | "eight" `isSuffixOf` xs = "8"
            | "nine" `isSuffixOf` xs = "9"
            | "zero" `isSuffixOf` xs = "0"
            | otherwise = computeNumberAuxRight $ init xs

computeNumber :: String -> Int
computeNumber [] = 0
computeNumber s = read (computeNumberAuxLeft s ++ computeNumberAuxRight s)::Int


main :: IO ()
main = interact $ \input -> 
  let output = sum $ map computeNumber (lines input)
  in show output