computeNumberAux :: String -> String
computeNumberAux [] = "0"
computeNumberAux (x:xs) 
            | [x] `elem` map show [0..9] = [x]
            | otherwise = computeNumberAux xs


computeNumber :: String -> Int
computeNumber [] = 0
computeNumber s = read (computeNumberAux s ++ computeNumberAux (reverse s))::Int

main :: IO ()
main = interact $ \input -> 
  let output = sum $ map computeNumber (lines input)
  in show output
    
