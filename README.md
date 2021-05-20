# TTS Demo Files


This repository contains demo files for the text-to-speech synthesis. New files can be added as follows:

1. Add a new folder that will contain the demo files (named with the date of the presentation `dd_mm_yy`) to the `/out/samples/` folder.

2. Add files named `{file_name}_{emotion}_{model}.wav` into the newly created folder. `file_name` is the original file name, `emotion` is the abbreviated generated emotion (`amused -> amu`, `anger -> ang`, `disgust -> dis`, and `sleepy -> sle`), and model is one of `cyc` or `vaw` for CycleGAN and VAW-GAN, respectively.