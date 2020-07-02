# BNP_Final_Project
Basic network programming final project
Caro game 

=== messagepack ===
Message structure:
    Code.Type.Message

    0: Normal communicate
        Type 1: From server | Message: Top score board
    1: Authentication
        Type 0: From client | Message: username and password
        Type 1: From server | Message: 1 is valid, 0 is invalid
    2: Request to create a room
        Type 0: From client | Message: Empty
        Type 1: From server | Message: Room Code 
    3: Request to join specified room
        Type 0: From client | Message: Room Code
        Type 1: From server | Message: 1 is valid, 0 is invalid
    4: Game data
        Type 0: From client | Message: Player's turn, win check and coordinates of this step
        Type 1: From server | Message: Latest player's turn, win check and its coordinates
                ** Win check: 0 if this player has not won yet
                                1 if this player won
