let flag = [85; 77; 68; 67; 84; 70; 123; 126; 126; 126; 116; 102; 118; 51; 99; 48; 64; 33; 64; 36; 38; 42; 40; 94; 116; 98; 53; 51; 43; 95; 43; 51; 114; 51; 50; 98; 52; 98; 121; 41; 40; 38; 35; 41; 82; 37; 64; 95; 95; 95; 95; 95; 115; 51; 82; 49; 48; 85; 115; 49; 89; 95; 119; 104; 79; 95; 64; 99; 116; 117; 64; 49; 49; 121; 95; 117; 115; 69; 115; 95; 48; 99; 64; 109; 49; 63; 63; 63; 95; 95; 95; 95; 95; 78; 78; 73; 94; 38; 79; 78; 38; 88; 37; 94; 94; 38; 81; 42; 84; 116; 102; 56; 57; 55; 56; 118; 119; 111; 56; 126; 126; 126; 125];;
let flag_len = 123;;

Printf.printf "===============================================\n";;
Printf.printf "OCaml Flag Checker (v 1.0.0)\n";;
Printf.printf "===============================================\n";;

Printf.printf "Make a guess: \n";;
flush stdout;;

let user_input = input_line stdin;;

let rec check_input s i =
  if (i < flag_len) then
    let chr = s.[i] in
    let user_ascii = Char.code chr in
    let correct_ascii = List.nth flag i in

    Printf.printf "Checking: %c" chr;

    if (user_ascii != correct_ascii) then begin
      Printf.printf " - Incorrect Match!\n";
    end
    else begin
      Printf.printf " - Match!\n";
    end;
    flush stdout;

    check_input s (i + 1);  (* Recursive call for the next character *)
in

if (String.length user_input != flag_len) then begin
  Printf.printf "Incorrect length!\n";
  flush stdout;
  exit 1;
end
else
  check_input user_input 0;
  Printf.printf "Checking completed.\n";
  flush stdout;
  exit 0;
