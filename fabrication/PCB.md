# Making PCBs
Imagine you're working on a robot which needs a GPS sensor. So far, you know how to use a breadboard, and perhaps you've used prototyping boards before, so you know how to solder through hole components.

But when you go to purchase your part, you find that they don't have a through hole GPS sensor! This is typically true of anything more complicated than performing a single logical function and is not particularly cheap: for example, you probably won't find through hole versions of GPS sensors, and (a bunch of stuff that I don't actually know haha).

Instead, you have surface mount components. Surface mount components don't have legs; instead they are plopped straight onto the surface of a pcb (hence the name). Not only are surface mount components smaller and more fiddly to solder, there's also no standard prototyping board / breadboard that you can  use to put them together. Instead, you have to manufacture a PCB (printed circuit board).


## PCB design tools
There are plenty of expensive PCB design tools out there, but the open source version is called KiCAD, and can be downloaded here: https://kicad-pcb.org/

I've also found this series on KiCAD especially helpful as a use guide: https://www.youtube.com/watch?v=vaCVh2SAZY4
Although some of the icons are a little out of date, with a little patience I found it incredibly useful.

Surface mount components are somewhat more difficult to solder as well, and I found these videos useful in explaining:
- How to solder surface mount: https://www.youtube.com/watch?v=VxMV6wGS3NY
- What the random ground pads under some more complex components are for: https://forums.parallax.com/discussion/157200/practical-home-method-to-solder-smd-with-ground-pad-below
- How to use vias to solder thermal pads https://www.youtube.com/watch?v=588iV07nEdM&t=715s

