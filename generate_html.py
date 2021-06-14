import os

from collections import defaultdict

from airium import Airium


def get_file_list():
    sample_path = './out/samples'
    
    folder_list = os.listdir(sample_path)
    files_by_folder = defaultdict(dict)
    
    for folder in folder_list:
        all_files = os.listdir(os.path.join(sample_path, folder))
        original_file_names = sorted(list(set([extract_original_file_name(file) for file in all_files])))

        for original_file in original_file_names:

            files_by_folder[folder][original_file] = {
                'neu': sorted([file for file in all_files if 'neu' in file and original_file in file]),
                'CycleGAN': sorted([file for file in all_files if 'cyc' in file and original_file in file]),
                'VAW-GAN': sorted([file for file in all_files if 'vaw' in file and original_file in file]),
                'Phoneme_embedded VAW-GAN': sorted([file for file in all_files if 'phoneme' in file and original_file in file]),
                'CMU-MOSEI': sorted([file for file in all_files if 'cmu-mosei' in file and original_file in file])
            }
    print(files_by_folder)
    return files_by_folder


def convert_folder_name_to_date(folder_name):
    return folder_name.replace('_', '/')


def extract_original_file_name(file_name):
    return file_name.split('_')[0]


def extract_emotion_from_file_name(file_name):
    emotions = {
        'neu': '&#x1F610 Neutral',
        'amu': '&#x1F604 Amused',
        'ang': '&#x1F621 Anger',
        'dis': '&#x1F922 Disgust',
        'sle': '&#x1F634 Sleepy',
        'sur': 'Surprise'
    }
    if 'neu' in file_name:
        return emotions['neu']
    return emotions[file_name.split('_')[1]]


def generate_html():
    a = Airium()

    a('<!DOCTYPE html>')
    with a.html():
        with a.head():
            a.title(_t="TTS Demo Files")
            a.meta(name="viewport", content="width=device-width, initial-scale=1.0")
            a.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6", crossorigin="anonymous")
        with a.body():
            with a.div(klass="container pb-5 pt-5"):
                a.h1(_t="Huawei ETTS Demo Files", klass="text-center display-1 pt-5 pb-5")
                a.h5(_t="19/04/21: Reproduced VAW-GAN based emotion converter", klass="pt-5 pb-3")
                a.h5(_t="01/06/21-A: Added phoneme embeddings to the encoder of VAW-GAN", klass="pt-5 pb-3")
                a.h5(_t="01/06/21-B: Tested CMU-MOSEI with the vanilla VAW-GAN", klass="pt-5 pb-3")
                for folder, files_by_file_name in get_file_list().items():
                    a.h3(_t=f"Samples from {convert_folder_name_to_date(folder)}", klass="text-center display-6 pt-5")
                    for original_file_name, files_by_model in files_by_file_name.items():
                        a.h4(_t=original_file_name, klass="pt-5 pb-5 text-success")
                        for model, files in files_by_model.items():
                            if 'neu' == model:
                                with a.div(klass="row row-cols-1 row-cols-md-2 g-4"):
                                    with a.div(klass="col"):
                                        with a.div(klass="card"):
                                            with a.div(klass="card-body text-center"):
                                                a.h5(_t=extract_emotion_from_file_name(files[0]), klass="card-title")
                                                a.audio(controls=True, src=os.path.join('samples', folder, files[0]))
                            else:
                                a.h5(_t=f"Samples Generated with {model}", klass="pt-5 pb-3")
                                with a.div(klass="row row-cols-1 row-cols-md-2 g-4"):
                                    for file in files:
                                        with a.div(klass="col"):
                                            with a.div(klass="card"):
                                                with a.div(klass="card-body text-center"):
                                                    a.h5(_t=extract_emotion_from_file_name(file), klass="card-title")
                                                    a.audio(controls=True, src=os.path.join('samples', folder, file))
        a.script(src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js", integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf", crossorigin="anonymous")

    return str(a)


if __name__ == '__main__':
    get_file_list()
    html = generate_html()
    with open('./out/index.html', 'w') as file:
        file.write(html)
