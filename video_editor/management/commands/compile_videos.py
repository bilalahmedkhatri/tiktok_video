import subprocess
import os
import random
import string
from pathlib import Path
from django.core.management.base import BaseCommand
from video_editor.models import VideoID



class Command(BaseCommand):
    help = "Compile Downloaded TIKTOK videos."
    
    # random names
    @property
    def random_name_generator(self) -> str:
        return "".join([random.choice(string.ascii_letters) for s in range(10)]) 
    
    
    # dynamic directory name generator
    @property
    def directory_name(self) -> str:
        cur_dir = os.getcwd()
        create_dir = r"%s/media/compile_videos" % (cur_dir)
        return create_dir
    
    
    # get video full path with name
    @property
    def get_vid_name(self) -> list:
        get_videos = r"%s/videos" % (os.getcwd())
        return [str(f) for f in Path(get_videos).glob("*.mp4")]
    
    
    # create text file and save videos name with there path
    @property
    def create_txt_file(self):
        file_names = self.get_vid_name
        file_path = r"%s/text_file/%s.txt" % (self.directory_name, self.random_name_generator)
        print(file_path)
        with open(file_path, "w") as create_file:
            for name in file_names:
                create_file.write(f"file '{name}'\n")
            create_file.close()
        return os.path.basename(file_path)
        
        
    # Concatenate videos
    def concatenate_videos(self):
        file_dir = f"{self.directory_name}/text_file"
        search_file = "".join([str(f) for f in Path(file_dir).glob(self.create_txt_file)])
        save_file_name = r"%s/videos/%s.mp4" % (self.directory_name, self.random_name_generator)
        subprocess.run(['ffmpeg', '-safe', '0', '-f', 'concat', '-i', search_file, '-c', 'copy', save_file_name])
    
    
    # delete videos after compiled
    def delete_files(self):
        for x in self.get_vid_name:
            os.remove(x)
        
    
    def handle(self, *args, **options):
        self.concatenate_videos()
        self.delete_files()