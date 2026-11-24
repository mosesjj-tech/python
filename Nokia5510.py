menu = """
=========NOKIA 5510==========
  1. PHONE BOOK
  2. MESSAGES
  3. CHAT 
  4. CALL REGISTER 
  5. TONES
  6. SETTINGS
  7. CALL DIVERT
  8. MUSIC
  9. GAMES
  10. CALCULATOR
  11. REMINDERS
  12. CLOCK
  13. PROFILES
  14. SERVICES
  15. SIM SERVICES
"""
print(menu)

choice = int(input())

match choice:
    case 1:
        print("""
========PHONE BOOK OPTION======
1.SEARCH
2.SERVICE NOS.
3.ADD NAME
4.ERASE
5.EDIT
6.COPY
7.ASSIGN TONE
8.EDIT B'CARD
9.OPTIONS
10.SPEED DIALS
11.VOICE TAGS
""")

        choice = int(input())
        match choice:
            case 9: print("""OPTIONS MENU
1.MEMORY IN USE
2.TYPE OF VIEW
3.MEMORY STATUS
""")

    case 2: 
        print("""MESSAGES MENU
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
        choice_2 = int(input())
    case 3:
        print(""" CHAT SENDING ! ! !""")
    case 4:
        print("""CALL REGISTER MENU
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call list
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
""")
        choice = int(input())
        
        match choice:
            case 5:
                print("""CALL DURATION OPTIONS
1.Last call duration
2.All calls' duration
3.Received calls' duration
4.Dialled calls' duration
5.Clear timers
                """)
            
            case 6:
                print("""CALL COST OPTIONS
1.Last call cost
2.All calls' cost
3.Clear counters
                """)
            case 7:
                print("""ALL COST SETTINGS
1.Call cost limit
2.Show costs in
                """)
    case 5:
        print("""TONES MENU
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
        """)
    case 6:
        print("""SETTINGS MENU
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
        """)
        choice = int(input())
        match choice: 
            case 1:
                print("""CALL SETTINGS OPTIONS
1.Automatic redial
2.Speed dialling
3.Call waiting options
4.Own number sendng
5.Phone line in use
6.Automatic answer
""")
            case 2: 
                print("""PHONE SETTINGS OPTIONS
1.Language
2.Cell info display
3.Welcome note
4.Network selection
5.Confirm SIM service actions
""")
            case 3: 
                print("""SECURITY SETTINGS OPTIONS
1.PIN code request
2.Call barring service
3.Fixed dialling
4.Closed user group
5.Security level
6.Change access codes
""")
                
            case 4: 
                print("Factory settings restored")
    
    case 7:
        print("Call divert settings is already activated")
        
    case 8: 
        print("""MUSIC MENU
1. Music player
2. Radio
3. Recorder
4. Track list
""")
    
    case 9:
        print(" NO GAMES ALLOWED, OGA GO READ DIETEL! ! !")
        
    case 10:
        print("CALCULATING 2+2")

    case 11:
        print("REMINDER SET FOR MONDAY 7:00 AM")

    case 12:
        print("""CLOCK MENU
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
""")

    case 13: 
        print("PROFILES")

    case 14:
        print("SERVICE")

    case 15:
        print("SIM SERVICE")