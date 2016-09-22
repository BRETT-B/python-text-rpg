import random
import subprocess
import time

player_skills = {"attacked with a Flaming Sword": 25, "stuck him with a Dagger": 15, "shot an Arrow": 25, "Counter Attacked": 20, "struck with a War Hammer": 30, "landed a CRITICAL HIT": 40, "MISSED": 0}
enemy_skills = {"bashed you with a Mace": 10, "hurled a Fire Ball": 15, "Counter Attacked": 20, "used a Battle Axe": 25, "MISSED": 0, "cut you using a Scythe": 20}
prompt = "--> "

# Represent the player
class Player:
    moves = {1: "Forest", 2: "Cave", 3: "Dungeon"}
    victories = 0
    def __init__(self, health):
        self.health = health

    def print_health(self):
        print "\t\t\t\t\t\t      ---------------------"
        print "\t\t\t\t\t\t      | Player Health: %d |" % self.health
        print "\t\t\t\t\t\t      ---------------------"

    def move(self):
        print "Where would you like to explore?:"
        for key in self.moves:
            print "%d. %s" % (key, self.moves[key])
        advance = int(raw_input(prompt))
        encounter = random.randint(1, 3)
        if not advance in Player.moves:
            print "Sorry, can\'t locate %d on the map." % (advance)
            return False
        elif advance == 10:
            return True
        elif advance == 4:
            print'\t\t           (                 ,&&&.'
            print'\t\t             )                .,.&&'
            print'\t\t            (  (              \=__/'
            print'\t\t                )             ,\'-\'.'
            print'\t\t          (    (  ,,      _.__|/ /|'
            print'\t\t           ) /\ -((------((_|___/ |'
            print'\t\t         (  // | (`\'      \ |`\'--|'
            print'\t\t       _ -.;_/\ \--._      (\ \-._/.'
            print'\t\t      (_;-// | \ \-\'.\    <_,\_\`--\'|'
            print'\t\t      ( `.__ _  ___,\')      <_,-\'__,\''
            print'\t\t       `\'(_ )_)(_)_)\''
            time.sleep(1.5)
            print
            print "After a good nights rest your health increases by 50"
            time.sleep(1)
            self.health += 50
            self.print_health()
            self.moves.pop(4, None)
            return False
        elif advance == encounter:
            print'==========================================================================='
            print'      db   MMP\"\"MM\"\"YMM MMP\"\"MM\"\"YMM   db       .g8\"\"\"bgd `7MMF\' `YMM\''
            print'     ;MM:  P\'   MM   `7 P\'   MM   `7  ;MM:    .dP\'     `M   MM   .M\''   
            print'    ,V^MM.      MM           MM      ,V^MM.   dM\'       `   MM .d\"'     
            print'   ,M  `MM      MM           MM     ,M  `MM   MM            MMMMM.'     
            print'   AbmmmqMA     MM           MM     AbmmmqMA  MM.           MM  VMA'    
            print'  A\'     VML    MM           MM    A\'     VML `Mb.     ,\'   MM   `MM.'  
            print'.AMA.   .AMMA..JMML.       .JMML..AMA.   .AMMA. `\"bmmmd\'  .JMML.   MMb.'
            print'==========================================================================='
            return True
        else:
            print "Your journey has enlightened you...health increases by 5\nExplore some more to find some enemies"
            time.sleep(0.5)
            self.health += 5
            self.print_health()
            return False

    def attack(self):
        attack = random.choice(player_skills.keys())
        damage = player_skills[attack]
        print "You %s and did %d damage!" % (attack, damage)
        return damage

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage


# Represent the enemy
class Enemy:

    def __init__(self, health):
        self.health = health

    def print_health(self):
        print "\t\t\t\t\t\t      ---------------------"
        print "\t\t\t\t\t\t      | Enemy Health: %d  |" % (self.health)
        print "\t\t\t\t\t\t      ---------------------"

    def attack(self):
        attack = random.choice(enemy_skills.keys())
        damage = enemy_skills[attack]
        print "The enemy %s and did %d damage!" % (attack, damage)
        return damage

    def take_damage(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage


# create a player instance with full health
player = Player(100)

# create an enemy instance with full health
enemy = Enemy(100)

while 1:
    encountered = player.move()

    if encountered:
        while player.health > 0 and enemy.health > 0:
            # player attacks
            enemy.take_damage(player.attack())
            enemy.print_health()
            # enemy attacks
            player.take_damage(enemy.attack())
            player.print_health()
            print "-----------------------------------------------------"
            time.sleep(2.5)
        if player.health == 0:
            play_again = str(raw_input("The battle was lost. Your wounds bleed out and you die.\nWould you like to resurrect? [Y/N]").upper())
            if play_again == 'Y':
                print "A beam of bright light floods your vision..."
                time.sleep(1.5)
                print "As you awake, you stand in the middle of the road\nwith a feeling of rejuvination"
                subprocess.call(['python', 'hero-game.py'])
            else:
                print "As your corpse lie rotting...."
                print "you are forgotten by all...."
                print
                print '\t\t\t           )              ) ('      
                print '\t\t\t  *   ) ( /(           ( /( )\ )'   
                print '\t\t\t` )  /( )\())(     (   )\()|()/('
                print '\t\t\t ( )(_)|(_)\ )\    )\ ((_)\ /(_))'
                print '\t\t\t(_(_()) _((_|(_)  ((_) _((_|_))_'
                print '\t\t\t|_   _|| || | __| | __| \| ||   \.'
                print '\t\t\t  | |  | __ | _|  | _|| .` || |) |'
                print '\t\t\t  |_|  |_||_|___| |___|_|\_||___/'

                exit(0)
        else:
            print "_____________________________________________________"
            print 
            print "You have fought bravely...the enemy is dead!"
            Player.victories += 1
            if Player.victories == 1:
                print "You're the talk of the town, and earned %d victory" % (Player.victories)
            elif Player.victories == 2:
                print "Knighthood never felt so good, you earned %d victories" % (Player.victories)
            elif Player.victories == 3:
                print "You have slayed all %d goons" % (Player.victories)
                time.sleep(1)
                print "Destroy the Evil Orc...and rescue the princess"
                Player.moves.pop(1, None)
                Player.moves.pop(2, None)
                Player.moves.pop(3, None)
                Player.moves[10] = "<<<<<<< RESCUE PRINCESS >>>>>>>>"
            elif Player.victories == 4:
                print'          (,);    /\                        '
                print'         ((  ^_   ||            ...         '
                print'          \' /  \  ||           (()))       '
                print'            L {=) ||           {\' ())      '
                print'             ) -  ||            )_ (()      '
                print'           (_   \====       @  (   (_)      '
                print'           | (___{)(         \  \ _) |      '
                print'            \____\/}          {)=== /\      '
                print'            |    |             \|    |     '
                print'            |_/\_|              |    |     '
                print'             |  |               |    |     '
                print'              ) )\              |    |     '
                print'            _/| |/              |    |     '
                print'           ( ,\ |_              \'~~~~\'   '
                print'            \_(___)              _/Y       '
                print "You did it! You rescued the princess! You truly are a HERO!"
                time.sleep(1.5)
                restart = str(raw_input("Play Again? [Y/N]").upper())
                if restart == 'Y':
                    subprocess.call(['python', 'hero-game.py'])
                else:
                    print "Thank you for playing"
                    exit(0)
            Player.moves[4] = "Camp"
            enemy = Enemy(100)
            continue