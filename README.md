Eurorack Four Module Challenge
==============================

This script is inspired by YouTuber "Comparative Irrelevance" and their #3modulechallenge.

https://www.youtube.com/channel/UCQBQ6F7VD78Ic_FkTexeE8g

Use this to generate a list of four modules from a list in the same folder called 'modules.txt'.

The format of the modules.txt file is:

<module_name>,<type>
  module_name: This is the name of the module.  Spaces are OK.
  type: This is the type of module.  Choose one of the following letters to categorize:
    f: FX (delays, reverbs)
    m: Modulator (function generators, LFOs, sequencers)
    s: Sound Source (oscillators, sample players)
    u: Utility (VCAs, EGs, quantizers, touch controllers)

Anyways, I wanted to do four modules instead of three because mentally it just makes more sense
to me a the moment in how I think of modular.  Also, logically separating the modules into types 
ensure that you'll be able to make some noise at the very least.

I did add an optional switch to this script ("--ci") to allow you to do the true #3modulechallenge.  
It's kind of dumb though since it randomly chooses any three modules from the list provided and 
prints them out.  There's a chance you could end up with nothing but VCAs, for example.
