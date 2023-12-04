open System.IO
open System.Text.RegularExpressions

let rx = Regex(@"one|two|three|four|six|seven|eight|nine")
let stream = new StreamReader @"..\input.txt"
let mutable valid = true
while(valid) do
    let line = stream.ReadLine()
    if(line = null) then
        valid <- false
    else
