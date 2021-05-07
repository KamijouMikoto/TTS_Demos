# TTS Demo Files


This repository contains demo files for the text-to-speech synthesis. New files can be added as follows:

1. Add a folder containing the demo files (named with the date of the presentation `dd_mm_yy`) to the root of the repository.

2. Extend the container in `index.html` by copying the following templates. Keep in mind to fill in the `{placeholders}`:

    1. Append the title of new section:

        ```html
        <h3 class="text-center display-6 pt-5">Samples from {dd}/{mm}/{yyyy}</h3>
        ```

    2. Append the text representation of the synthesised speech:

        ```
        <h4 class="pt-5 pb-5 text-success">"{This is the text representation.}"</h4>
        ```

    3. Append the generated neutral sample:
    
        ```html
        <div class="row row-cols-1 row-cols-md-2 g-4">
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F610 Neutral</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_neu.wav"></audio>
                    </div>
                </div>
            </div>
        </div>
        ```

    4. Append (if existing) the audio samples generated by the CycleGAN:

        ```html
        <h5 class="pt-5 pb-3">Samples Generated with CycleGAN</h5>
        <div class="row row-cols-1 row-cols-md-2 g-4">
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F604 Amused</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_amu_cyc.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F621 Anger</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_ang_cyc.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F922 Disgust</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_dis_cyc.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F634 Sleepy</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_sle_cyc.wav"></audio>
                    </div>
                </div>
            </div>
        </div>
        ```

    5. Append (if existing) the audio samples generated by the VAW-GAN:

        ```html
        <h5 class="pt-5 pb-3">Samples Generated with VAW-GAN</h5>
        <div class="row row-cols-1 row-cols-md-2 g-4 pb-5">
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F604 Amused</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_amu_vaw.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F621 Anger</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_ang_vaw.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F922 Disgust</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_dis_vaw.wav"></audio>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card">
                    <div class="card-body text-center">
                        <h5 class="card-title">&#x1F634 Sleepy</h5>
                        <audio controls src="{dd_mm_yy}/{file_name}_sle_vaw.wav"></audio>
                    </div>
                </div>
            </div>
        </div>
        ```

It is planned in the future to perform the steps in 2. automatically.