# PirateRadio
PyGame music player, using the Pimoroni Pirate Radio kit

Please note the following code supports .mp3 files only, however you can very easily adapt it to support other media files.

The program is set to pull files from a music folder, however you can change the directory on line 4 to suit your needs

This is still a work in progress, and I hope to possibly add a web interface, of which you can upload files to the music folder.

You must have the PhatBeat Libary installed before using this program. This can be done by executing the following command in the terminal:

<pre>curl -sS https://get.pimoroni.com/phatbeat | bash</pre>

To clone the code, type in the following command:

<pre>sudo git clone https://github.com/ajalexsmith/PirateRadio.git</pre>

#Please note, the error "ALSA lib pcm.c:7843:(snd_pcm_recover) underrun occurred" does occur frequently within the script. From what i have read, it simply means that the pi isn't supplying speaker with information quick enough, however it is nothing to worry about, and is to be expected due to the processing capabilities of the Pi Zero!
