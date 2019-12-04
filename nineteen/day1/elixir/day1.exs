defmodule AocDay1 do
    def int_list do
        "day1_data.txt" 
        |> File.read! 
        |> String.split 
        |> Enum.map(fn (x) -> String.to_integer(x) end)
    end

    def fuel_adder_upper do
        int_list()
        |> Enum.map(fn x -> div(x, 3) - 2 end) 
        |> Enum.sum
    end
end
