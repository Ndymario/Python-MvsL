



# unused for now, just keeping these things here for later

if (string == "bind"){

}


stringimworkingwith = "player.y:100"
split_string = stringimworkingwith.split(":")
print(stringimworkingwith)
print(split_string)
exec("%s = %d" % (split_string[0],eval(split_string[1])))