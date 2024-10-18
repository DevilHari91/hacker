import time

def print_ascii_art():
    art = r"""
    
                 :::::::::::::::::::::::::::::::::::::::::::::::::-===--::::::::::::::::::::...................:::::. 
                 :::::::::::::::::::::::::::::::::::::::::--+*#############+-:::::::::::::.....................:::::. 
                 :::::::::::::::::::::::::::::::::::::::=#%%%%%%%%%%#%#%%####*+::::::::::......................:::::. 
                 ::::::::::::::::::::::::::::::::::::-*%%%%%%%%%%%%%%%%%%%%####*+-:::::::......................:::::. 
                 ::::::::::::::::::::::::::::::::::-*%%%%%%%%%%%%%%%%%%%%%%######*+::::::......................:::::. 
                 :::::::::::::::::::::::::::::::::-#%%%%%%%%%%%@@%%%%%%%%%%%#######*:::::......................:::::: 
                 :::::::::::::::::::::::::::::::::#%%%@@@%@@@%%@@%@%%%%%%@%%%%%%%####-:::......................:::::: 
                 ::::::::::::::::::::::::::::::::+%%@@@@%%######%%%%%%%%%%%%%%%%%#%%#+:::......................:::::: 
                 :::::::::::::::::::::::::::::::-%%%@@@%#*********###**+++===+*%%%%%#*:::......................:::::: 
                 :::::::::::::::::::::::::::::::-%%%%@%%**+++++++++++++===----=#%%%%%#-::......................:::::: 
                 :::::::::::::::::::::::::::::::=%%@@%%#*++++++++++++++===-----*%%%%##=:.......................:::::: 
                 :::::::::::::::::::::::::::::::=%%%@%**++++++++====++===------=#%%###-::......................:::::: 
                 :::::::::::::::::::::::::::::::=%%%%*++*####***+++++++++=------+%%%%+::....................::::::::: 
                 :::::::::::::::::::::::::::::::+%%%****####################***==#%##-::...................:::::::::: 
                 :::::::::::::::::::::::::::::::+#%#*****#**%####*##***#####**+++***::::..................::::::::::: 
                 :::::::::::::::::::::::::::::::****+++++*****#***##*+=**##*++==-=+-::::................::::::::::::: 
                 :::::::::::::::::::::::::::::::++#*+++++++*+++++*+=-=--=+++=--:-=*=::::..............::::::::::::::: 
                 :::::::::::::::::::::::::::::::-+**++++++++*****+==-:=======-::-=+:::::............::::::::::::::::: 
                 ::::::::::::::::::::::::::::::::+**+++++++****#+====-:=++==-::-==+:::::..........::::::::::::::::::: 
                 ::::::::::::::::::::::::::::::::=+**++++++****##%#**#*==+++=---=+=.::::..........::::::::::::::::::: 
                 ::::::::::::::::::::::::::::::::.-***++++++****#####*+==-===---=+-..:::.........:::::::::::::::::::: 
                 ::::::::::::::::::::::::::::::.....*******##%%###***+*****=======:.::::.........:::::::::::::::::::: 
                 ::::::::::::::::::::::::::::.......*******#%%%##***+==+*##+====+=.:-===-::.......::::::::::::::::::: 
                 ::::::::::::::::::::::::::.....:--+%################**+==**++++**::--==+++=-==::::::::::::....:::::: 
                 ::::::::::::::::::::::::..:-------#%%%#######****###*++==++++*###+:--:==--=-=::::::..::::::::::::::: 
                 :::::::::::::::::::::::-------==-+%@%##############**+++++****###*---==-:==+=:.........::::::::::::: 
                 ::::::::::::::::::::::------=++--*%%%#*####%%%%%%%%%###**###*+**#+--==--=+++-.....:.....:::::::::::: 
                 ::::::::::::::::::---====---=*--=#%%%#***#%%%%%%%%%%%%%%%%+::-**#*+----=++++:...::........:::::::::: 
                 :::::::::::::::---=======--=++--=*%%%##****##%%%%%%%%%%*=##=::-+*#+---=++++=...:--.....:...::::::::: 
                 ::::::::::::.:-----======-==+=-*#+#%%###########%%%%%*+++*#####***+--=+++++-....--:...::....:::::::: 
                 :::::::::::.:::------==+===+++#**++*############%#*===--=+++++***++===+++++-....-=:..:::.....::::::: 
                 ::::::::::..:::---------===++++++===+==+*######+--++=---=====+**+==++=++++=-..::-=:.:--:......:::::: 
                 :::::::::..:::-------=========-----====+++##+--:=+=-----=====++++=+++++++==:.-::-=:.:--........::::: 
                 ::::::::..:::----------==============---==+-:.:-=--------=--==+====++++++=-:.--:-+-.--:.........:::: 
                 ::::::..:::::--------------------------=++=:::::------------========+++==-::.--:-+-::::..........::: 
                 ::::::::::--------------------------==+++=::::::--:-------===========+==-:::.-=:-+=:::............:: 
                 :::::::-:-----------------------===+++====:::::::-:-----===---------===-:::::-+-=+=:::.............: 
                 ::::.::----------------------=============-:::-::-----==----------:-==-:::::-:++=+--:::::..........: 
                 ::::::---====-----==+==---=======-===-===------:------------------------:::::--++==-::::::.......... 
                 ::::---==+++==-=+++=---====-------==--===-----=------=----======++===-----::::-*++===--:::::........   


                                       ______  __ __   ____  ____   __  _      __ __   ___   __ __ 
                                      |      ||  |  | /    ||    \ |  |/ ]    |  |  | /   \ |  |  |
                                      |      ||  |  ||  o  ||  _  ||  ' /     |  |  ||     ||  |  |
                                      |_|  |_||  _  ||     ||  |  ||    \     |  ~  ||  O  ||  |  |
                                        |  |  |  |  ||  _  ||  |  ||     \    |___, ||     ||  :  |
                                        |  |  |  |  ||  |  ||  |  ||  .  |    |     ||     ||     |
                                        |__|  |__|__||__|__||__|__||__|\_|    |____/  \___/  \__,_|
                                                 _____  ____  ____      _____ ____  ____           
                                               / ___/ /    ||    |    / ___/|    ||    \          
                                              (   \_ |  o  | |  |    (   \_  |  | |  D  )         
                                               \__  ||     | |  |     \__  | |  | |    /          
                                               /  \ ||  _  | |  |     /  \ | |  | |    \          
                                               \    ||  |  | |  |     \    | |  | |  .  \         
                                                \___||__|__||____|     \___||____||__|\_| 

                                                  __________________   __________________             
                                              .-/|                  \ /                  |\-.
                                              ||||                   |                   ||||
                                              ||||                   |       ~~*~~       ||||
                                              ||||    --==*==--      |                   ||||
                                              |||| -clear------this- |                   ||||
                                              |||| -------and------- |                   ||||
                                              |||| -enter------your- |     --==*==--     ||||
                                              |||| -------text------ | -clear------this- ||||
                                              ||||                   | -------and------- ||||
                                              ||||                   | -enter------your- ||||
                                              ||||                   | -------text------ ||||
                                              ||||__________________ | _              ___||||                                               
                                              ||/===================\|/===================\||
    """
    # Print each line of the ASCII art one by one
    for line in art.splitlines():
        print(line)
        time.sleep(0.2)

if __name__ == "__main__":
    print_ascii_art()