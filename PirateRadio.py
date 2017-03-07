from pygame import mixer 							#Importing the mixer module from the pygame libary
import phatbeat, glob 								#Importing the phatbeat libary (speaker controller board) and glob libary, used for reading all the music files

tracklist = glob.glob("music/*.mp3") 				#Puts all the mp3 files from the selected directory into an array

volume = 0.1 										#Sets the volume variable to minimum (Still very load)
state = 'new' 										#Sets the state of the program as freshly opened (new) This helps with play/pause later
Run = True

mixer.init() 										#Initialising the mixer module of pygame
mixer.music.load(tracklist[0]) 						#Loads the first track in the tracklist array
mixer.music.set_volume(volume) 						#Sets the initial volume
track = 0

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin): 								#Setting the play/pause function
    global state 									#Globaling the state variable so that it can be used in the function
    if state == 'pause': 							#Checking if the music is currently paused
		mixer.music.unpause()						#This unpauses the music 
		state = 'play' 								#Setting the state to playing
    elif state == 'play': 							#Checking if the musc is currently playing
		mixer.music.pause() 						#Pausing the music
		state = 'pause' 							#Cahnging the state to paused
    else:											#Else statement for if it is the first timeradio plays music. This is used as the music first has to be played before it is paused/unpaused
		mixer.music.play()							#Playing the music
		state = 'play' 								#Setting  the state to playing
@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin): 								#Setting up the volume up function
    global volume 									#Globaling the volume variable so that it can be used in the function
    volume = volume + 0.1 							#Increasing the volume variable by 0.1 (pygame volume between 0 and 1)
    mixer.music.set_volume(volume) 					#Setting radio's the volume with the variable
@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin): 								#Setting up the volume down function
    global volume 									#Globaling the volume variable so that it can be used in the function
    volume = volume - 0.1 							#Decreasing the volume variable by 0.1
    mixer.music.set_volume(volume)  				#Setting radio's the volume with the variable
@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin): 								#Setting up the next track function
    global track 									#Globalising the track number variable so that it can be used in the function
    track = track + 1 								#Increasing the track number vatiable by 1, so that it loads the next track
    mixer.music.load(tracklist[track])	 			#Loads the selected track from the tracklist array
    mixer.music.play() 								#Plays the selected track
	
@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin): 									#Setting up the previous track function
    global track  									#Globalising the track number variable so that it can be used in the function
    track = track - 1 								#Decreasing the track number variable by 1, so that it loads the previous track
    mixer.music.load(tracklist[track]) 				#Loads the selected track from the tracklist array
    mixer.music.play() 								#Plays the selected track

while Run == True: 									#Conditional while loop, broken if the off putton is pressed
    if state != 'new': 								#If the current state is not first run (this stops it cycling through all the tracks before the first track is loadesd)
		if mixer.music.get_busy() != 1: 			#If the Pygame mixer is not busy playing another track, function returns a value of 1 if busy
			track = track + 1 						#In creasing the track number vatiable by 1, so that it loads the next track
			mixer.music.load(tracklist[track])	 	#Loads the selected track from the tracklist array
			mixer.music.play()						#Plays the selected track
    @phatbeat.on(phatbeat.BTN_ONOFF, repeat=False)
    def onoff(pin): 								#Setting up the power function
		global Run										#Globalising the run variable, so that it can be used in the onoff function
		Run = False										#Breaks the while loop to stop the program
	
