import time, os , random
clear= lambda: os.system('cls')
clear()
player_hp = 100
Player_heal_hp=0
player_attack= 0
player_heal_attack= 0
backpack=[]
gold= 0
monster_attack=[]
monster_type=[]
monster_hp=[]
encounter= False
score=0

def welcome():
    print("""
                                    ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗██╗
                                    ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝██║
                                    ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░██║
                                    ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░╚═╝
                                    ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗██╗
                                    ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚═╝
                                                                                
                                                            ████████╗░█████╗░
                                                            ╚══██╔══╝██╔══██╗
                                                            ░░░██║░░░██║░░██║
                                                            ░░░██║░░░██║░░██║
                                                            ░░░██║░░░╚█████╔╝
                                                            ░░░╚═╝░░░░╚════╝

                                    ██████╗░██████╗░░██████╗░  ███╗░░██╗██╗██████╗░██████╗░░█████╗░░██████╗
                                    ██╔══██╗██╔══██╗██╔════╝░  ████╗░██║██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
                                    ██████╔╝██████╔╝██║░░██╗░  ██╔██╗██║██║██████╦╝██████╦╝███████║╚█████╗░
                                    ██╔══██╗██╔═══╝░██║░░╚██╗  ██║╚████║██║██╔══██╗██╔══██╗██╔══██║░╚═══██╗
                                    ██║░░██║██║░░░░░╚██████╔╝  ██║░╚███║██║██████╦╝██████╦╝██║░░██║██████╔╝
                                    ╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░  ╚═╝░░╚══╝╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚═════╝░ 
\n
    """)
    time.sleep(5)
    clear()
    menu()

def menu():
    choise=input("""
                                                            🅼🅴🅽🆄 
                                                Here are your options:
                                                type 'Start' to start the game.
                                                type 'help' for a quick explain.
                                                type 'diff' for a difficulty change.
                                                type 'quit' to quit the application.
    \n
    \n
    > """)
    if choise == 'start':
        clear()
        game_intro()
    if choise =='help':
        return
    if choise == 'diff':
        diffs=(input('please select a difficulty level: Hard , Normal , Easy'))
        match diffs:
            case 'hard':
                print('!hard Difficulty has been activated!')
                print('!ok monsters will now have more hp!')
                game_intro()
            case 'normal':
                print('!normal difficulty has been activated!')
                game_intro()
            case 'easy':
                print('!easy difficulty has been activated')
                print('monsters will now have less hp!')
                game_intro()

        
    if choise == 'quit':
        print('ok see you soon !')
        time.sleep(2)
        quit

def game_intro():
    print("""\n""")
    time.sleep(2)
    print('> you wake up in an unlocked cell in some kind of a dungon')
    time.sleep(2)
    print('> you hear a lot of growling ecoing in the halls')
    time.sleep(2)
    print('> you gather your corage and walk out of your cell....')
    time.sleep(5)
    print('> *riminder your controls are "W" to walk "A" to attack and "B" to open inentory')
    starter_gear()

def starter_gear():
    global player_attack
    global player_hp
    global backpack
    global gold
    global player_heal_attack
    global Player_heal_hp
    starter_weapons_list=('heavy hammer', 'wooden staff', 'short sword')
    starter_gear_list=('cloth armor', 'plate armor' 'iron armor', 'leather armor', 'nothing')
    Random_gear_selector= random.choice(starter_gear_list)
    Ramdom_weapon_selector= random.choice(starter_weapons_list)
    gold= 100
    match Ramdom_weapon_selector:
        case 'heavy hammer':
            player_attack = 15
            player_heal_attack= (player_attack)
            backpack.append('heavy hammer')
        case 'wooden staff':
            player_attack = 8
            player_heal_attack= (player_attack)
            backpack.append('wooden staff')
        case 'short sword':
            player_attack = 10
            player_heal_attack= (player_attack)
            backpack.append('shortsword')
    match Random_gear_selector:
        case 'cloth armor':
            player_hp= 110
            Player_heal_hp=(player_hp)
            backpack.append('cloth armor')
        case 'plate armor':
            player_hp = 140
            Player_heal_hp=(player_hp)
            backpack.append('playe armor')
        case 'iron armor':
            player_hp = 130
            Player_heal_hp=(player_hp)
            backpack.append('iron armor')
        case 'leather armor':
            player_hp = 120
            Player_heal_hp=(player_hp)
            backpack.append('leather armor')
        case 'nothing':
            player_hp= 100
            Player_heal_hp=(player_hp)
    print(f'>>> player HP{player_hp}, player ATK{player_attack}')
    print(f'> Your gold: {gold}')
    print(f'> backpack: {backpack}')
    player_move()
        

def player_move():
    global player_hp
    global backpack
    while player_hp != 0:
        controls= input('> what is your move? ')
        match controls:
            case 'w':
                if encounter == False:
                    walking()
                    return
                if encounter == True:
                    print('> you cant walk a monster is blocking the way!')
                    player_move()
                    return
            case 'a':
                if encounter == True:
                    combat()
                    return
                if encounter == False:
                    print('> nothing to attack')
                    player_move()
                return
            case 'b':
                print('> opening backpack....')
                print(f'backpack: {backpack}')
                player_move()
                return
    else:
        print('> You have died!')
        re=input('> respawn?')
        print(f'Your score: {score}')
        match re:
         case 'yes':
            print('wip')
         case 'no':
            quit
def combat():
    global player_attack
    global player_hp
    global monster_hp
    global backpack
    global encounter
    global score
    while player_hp > 0: 
        choicev3=input('> In Combat. what is your move? ')
        match choicev3:
            case 'w':
                monster_hp = monster_hp - player_attack
                print(f'> monster recived an attack of {player_attack}')
                monster_stats()
                monster_move()                 
                return
            case 's':
                Strong_attack_chance= random.choice(range(1,100))
                if Strong_attack_chance >30:
                    print('> strong attack missed')
                    monster_move()
                    return
                if Strong_attack_chance <30: 
                    monster_hp= monster_hp - player_attack*2
                    print(f'> monster recived a Strong attack of {player_attack*2}!')
                    monster_stats()
                    monster_move()
                    return
                return
            case 'r':
                run_away_chance= random.choice(range(1,100))
                if run_away_chance > 20:
                    print('> run away failed')
                    monster_move()
                    return
                if run_away_chance < 20:
                    encounter == False
                    print('> you have ran away from the monster!')
                    player_move()
                    return
            case 'b':
                print('> opening backpack....')
                print(f'> backpack: {backpack}')
                if 'potion of hp' or 'potion of cure attack' in backpack:
                    used_potions= input('> what kind of potion you want to drink? ')
                    if used_potions == 'potion of hp':
                        player_hp = player_hp + 40
                        print('> you used potion of hp and gained 40 hp')
                        player_stats()
                        combat()
                    if used_potions == 'potion of cure attack':
                        player_attack = player_heal_attack
                        print('> you used a potion of cure attack and reseted your attack')
                        player_stats()
                        combat()
                else:
                  print('you dont have any potions to use')
                  combat()
                  return
    else:
        clear()
        print('> You have died!')
        re=input('> respawn?')
        print(f'Your score: {score}')
        match re:
            case 'yes': #wip
                menu()
            case 'no':
                quit

def walking():
    print('> You walk forward!')
    chances()
    #change for encounters......

def chances():
    global encounter
    Chance2= random.choice(range(1, 105))
    if Chance2 > 30 and Chance2 < 100 :
        player_move()
    if Chance2 < 30: #encounter a monster!
        encounter= True
        monster_selector()
    if Chance2 > 100:
        return
def shop_selector():
    clear()
    print("""
                                  ░░                    
                  ▒▒▒▒▒▒    ░░░░▒▒▒▒                    
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
                ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒                      
              ▒▒▒▒▒▒░░░░░░░░░░░░░░                      
              ░░▓▓▒▒░░░░░░░░░░░░░░                      
              ░░▒▒░░░░▒▒░░░░░░▒▒░░                      
              ░░▒▒░░░░▓▓░░░░░░▓▓░░              ░░░░    
              ░░░░░░░░░░░░░░░░░░░░              ░░░░░░  
                ▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒              ░░░░░░░░
                ▓▓▒▒▒▒░░░░░░░░▒▒▒▒            ░░░░░░░░░░
                  ▒▒▒▒░░░░░░▒▒▒▒              ░░░░░░░░░░
                  ▓▓▒▒▒▒▒▒▒▒▒▒▓▓                ░░░░░░  
                ▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓              ██▓▓▓▓  
        ██▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓      ▓▓▓▓▓▓▓▓
        ██▓▓▓▓▓▓░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░████▓▓▓▓      ██▓▓▓▓▓▓
      ▓▓▓▓▓▓▓▓▓▓░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒░░██▓▓▓▓▓▓▒▒    ▓▓▓▓▓▓▓▓
      ▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓░░░░  ██▓▓▓▓▓▓▓▓▓▓  ██▓▓▓▓▓▓
      ██▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓░░    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
    ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓
    ██▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ██▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░▓▓▓▓▓▓      ▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓
  ██▓▓▓▓▓▓▓▓██▓▓▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░▓▓▓▓▓▓  ██▓▓▓▓▓▓▓▓▓▓▓▓
  ██▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░░░░░    ▓▓▓▓▓▓  ░░▓▓▓▓▓▓▓▓▓▓▓▓
  ██▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░        ▓▓▓▓▓▓▓▓    ░░▓▓▓▓▓▓▓▓░░
  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░░░░░░░░░▓▓▓▓▓▓▓▓                
  ▓▓▓▓▓▓▓▓▓▓▓▓░░▓▓░░░░          ██░░▓▓▓▓                
    ██▓▓▓▓▓▓░░▓▓▓▓░░            ████░░▓▓                
      ▓▓▓▓░░▓▓▓▓▓▓░░░░░░░░░░░░░░██▓▓██░░                
          ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓                
          ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓                
              ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒                    
              ▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒                    
              ▓▓▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▓▓                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▓▓                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
              ▒▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒                    
                ▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓                      
                  ▒▒▒▒░░  ▒▒▒▒░░                        
                ██▓▓▓▓▓▓  ██▓▓▓▓▓▓                      
            ▒▒▒▒▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▒▒▒▒                      
    """)
    player_move()

def monster_selector():
    global monster_type
    monster_types= ('goblin warrior' , 'goblin mage')
    monster_select= random.choice(monster_types)
    match monster_select:
        case 'goblin warrior':
            monster_type = 'goblin warrior'
            monster_creator_goblin_warrior()
        case 'goblin mage':
            monster_type = 'goblin mage'
            monster_creator_goblin_mage()

def monster_creator_goblin_warrior():
    global monster_hp
    global monster_attack
    monster_hp= random.choice(range(80, 100))
    monster_attack= random.choice(range(10, 15))
    print(f'>>>A {monster_type} appered!<<<')
    print("""
                  (\    /)
                  |_)//(_|
                  |4\_/4)(
                 '( (_  -)D
                   ) _   /\,__
                 _,\_._,/ /   `)
    \.,_,,      ( _   ~ .   ,   |
     \   (\      \(   \/  _)(    )
      \   \\      )). _______>-. `*
       \  /\\    _'( /   /\  '\  _)
        \( ,\\.-'  '/    \/    \/
         '  \><)_'.)|/\/\/\/\/\|
              \) ,( |\/\/\/\/\/|
              ' ((  \    /\    /
               ((((  \___\/___/)
                ((,) /   ((()   )
                 "..-,  (()("   /
                 _//.   ((() ."
                //,/"     ((( ', 
                           ((  )
                            / /
                          _/,/'
                        /,/,"    
    
    """)
    monster_stats()
    player_move()

def monster_creator_goblin_mage():
    global monster_hp
    global monster_attack
    monster_hp= random.choice(range(20, 40))
    monster_attack= 5
    print(f'>>>A {monster_type} appered!<<<')
    print("""
                '             .           .
            o       '   o  .     '   . O
        '   .   ' .   _____  '    .      .
            .     .   .mMMMMMMMm.  '  o  '   .
        '   .     .MMXXXXXXXXXMM.    .   ' 
        .       . /XX77:::::::77XX\ .   .   .
            o  .  ;X7:::''''''':::7X;   .  '
        '    . |::'.:'        '::| .   .  .
            .   ;:.:.            :;. o   .
        '     . \'.:            /.    '   .
            .     `.':.        .'.  '    .
            '   . '  .`-._____.-'   .  . '  .
            ' o   '  .   O   .   '  o    '
            . ' .  ' . '  ' O   . '  '   '
            . .   '    '  .  '   . '  '
                . .'..' . ' ' . . '.  . '
                `.':.'        ':'.'.'
                `\\_  |     _//'
                    \(  |\    )/
                    //\ |_\  /\\
                    (/ /\(" )/\ \)
                    \/\ (  ) /\/
                        |(  )|
                        | \( ]
                        |  )  ]
                        |      ]
                        |       ]
                        |        `.__,
                        \_________.-  
    """)
    monster_stats()
    player_move()

def monster_stats():
    print(f'>>> monster HP{monster_hp}, monster ATK{monster_attack}')

def player_stats():
    print(f'>>> player HP{player_hp}, player ATK{player_attack}')

def monster_move():
    global player_hp
    global player_attack
    global monster_attack
    global monster_hp
    global score
    global Player_heal_hp
    global player_heal_attack
    global encounter
    global monster_type
    if monster_type == 'goblin warrior':
        while monster_hp > 0:
            monster_moves= ('attack' , 'weaken', 'strong attack')
            monster_choice= random.choice(monster_moves)
            match monster_choice:
             case 'attack':
                player_hp= player_hp - monster_attack
                print(f'> {monster_type} has attacked the player for {monster_attack}')
                player_stats()
                combat()
                return
             case 'weaken':
                weaken_chance= random.choice(range(1, 100))
                print (f'> {monster_type} is trying to weaken the player')
                if weaken_chance < 10:
                 player_attack= player_attack - 2
                 print(f'> {monster_type} has weakend the players attack by 2')
                 player_stats
                 combat()
                else:
                    print(f'> {monster_type} failed to weaken you!')
                    player_stats()
                    combat()
             case 'strong attack':
                strong_attack_chance= random.choice(range(1, 100))
                print (f'> {monster_type} is trying to do a strong attack')
                if strong_attack_chance < 45:
                    player_hp = player_hp - monster_attack*2
                    print(f'> {monster_type} has hit you for {monster_attack*2} using strong attack!')
                    player_stats()
                    combat()
                else: 
                    print(f'> {monster_type} missed the strong attack!')
                    player_stats()
                    combat() 
        else:
            clear()
            print(f'>>you have slain the {monster_type}<<')
            score += 100
            encounter = False
            player_attack= player_heal_attack
            player_hp = Player_heal_hp
            player_stats()
            loot_system_basic()
            return
    if monster_type == 'goblin mage':
        while monster_hp > 0:
            monster_moves= ('fireball','regen','stick jab')
            monster_choice= random.choice(monster_moves)
            match monster_choice:
                case 'fireball':
                    print(f'> {monster_type} tries to cast fireball')
                    fireball_cast= random.choice(range(1, 100))
                    if fireball_cast < 10:
                        print(f'> {monster_type} failed the fireball cast ')
                        player_stats()
                        combat()
                    else:
                        fireball_dmg= random.choice(range(20, 40))
                        player_hp = player_hp - fireball_dmg
                        print(f'> {monster_type} hit you with a fireball for {fireball_dmg}!')
                        player_stats()
                        combat()
                case 'regen':
                    monster_regen= random.choice(range(5, 10))
                    monster_hp= monster_hp + monster_regen
                    print(f'> {monster_type} casted a regen spell and gained {monster_regen} hp')
                    monster_stats()
                    player_stats()
                    combat()
                case 'jab':
                    player_hp= player_hp - monster_attack
                    print(f'{monster_type} jabed you with thier stick for {monster_attack}')
                    player_stats()
                    combat()
        else:
            clear()
            print(f'>>you have slain the {monster_type}<<')
            score += 100
            encounter = False
            player_attack= player_heal_attack
            player_hp = Player_heal_hp
            player_stats()
            loot_system_basic()
            return                        

def loot_system_basic():
    global backpack
    global gold
    global player_attack
    global player_hp
    global player_heal_attack
    global Player_heal_hp
    Gold_gain= random.choice(range(10, 30))
    gold = Gold_gain + gold
    print(f'> You gained {Gold_gain} Gold.')
    print(f'> You have {gold} Gold, find a shop to spend it.')
    drop_items= ['Poor Helmet', 'Trident', 'shield', 'pickaxe', 'nothing', 'nothing', 'nothing','nothing', 'nothing', 'nothing', 'nothing', 'nothing', 'old sword', 'teeth', 'potion of hp' 'potion of cure attack']
    match drop_items:
        case 'nothing':
            player_move()
        case 'Poor Helmet':
            print('> You found a Poor Helmet! HP +10')
            player_hp = player_hp + 10
            Player_heal_hp=(player_hp)
            backpack.append('Poor Helmet')
            print(backpack)
        case 'Trident':
            print('> You found a Trident ATK +30')
            player_attack = player_attack + 30
            player_heal_attack= (player_attack)
            backpack.append('Trident')
            print(backpack)
        case 'shield':
            print('> You found a Poor shield! HP +30')
            player_hp = player_hp + 30
            Player_heal_hp=(player_hp)
            backpack.append('shield')
            print(backpack)           
        case 'pickaxe':
            print('> You found a Trident ATK +5')
            player_attack = player_attack + 5
            player_heal_attack= (player_attack)
            backpack.append('pickaxe')
            print(backpack)
        case 'old sword':
            print('> You found a Trident ATK +15')
            player_attack = player_attack + 15
            player_heal_attack= (player_attack)
            backpack.append('old sword')
            print(backpack)
        case 'teeth':
            print('you found some monster teeth!(maybe a merchent will want those...)')
            backpack.append('teeth')
            print(backpack)
        case 'potion of hp':
            print('you found a potion of hp!(you can use it to heal in battle)')
            backpack.append('potion of hp')
            print(backpack)
        case 'potion of cure attack':
            print('you found a potion of cure attack(you can use it to heal attack in battle)')
            backpack.append('potion of cure attack')
            print(backpack)
    player_stats()
    player_move()
welcome()