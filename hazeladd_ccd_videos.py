from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
import pandas as pd

from moviepy.config import change_settings

change_settings(
    {"IMAGEMAGICK_BINARY": r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"}
)

# Define the directory containing the MP4 files
video_directory = r"C:\Users\marco\Escritorio\Video CCD Hazeladd"
output_directory = r"C:\Users\marco\Escritorio\Video CCD output"

mod_file = r"C:\Users\marco\Escritorio\Video CCD Hazeladd\Modifications.csv"
exp_matrix = r"C:\Users\marco\Escritorio\Video CCD Hazeladd\CCD_matrix.csv"

mod_df = pd.read_csv(mod_file, sep=";")
mod_df = mod_df.iloc[[12, 13, 16]]
print(mod_df, "\n")


# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over each row in the CSV file
for _, row in mod_df.iterrows():
    experiment_name = row["Video"]

    # Find the corresponding video file based on the experiment name
    video_path = os.path.join(video_directory, f"{experiment_name}.mp4")
    if not os.path.exists(video_path):
        print(f"Video for {experiment_name} not found. Skipping.")
        continue

    # Define the start and end times for tail trimming (in seconds)
    start_time, end_time = row["start_time"], row["end_time"]
    degree = row["rotate"]

    ## Check if start_time or end_time is NaN
    if pd.isna(start_time) or pd.isna(end_time):
        print(f"Skipping {experiment_name} due to missing trim interval.")
        continue

    # Process the video with a `with` statement
    with VideoFileClip(video_path) as video:
        # Apply rotation
        rotated_video = video.rotate(degree, resample="bicubic")
        print(video.w, video.h)
        print(rotated_video.w, rotated_video.h)
        # Check if the rotation is 90 or 270 degrees, and apply resizing
        # if the width is greater than height (horizontal)
        if rotated_video.size[0] > rotated_video.size[1]:
            # No need to resize if it's already in a horizontal format
            pass
        # if the video is in a vertical format after rotation (it needs resizing)
        else:
            # Swap width and height to horizontal
            rotated_video = rotated_video.resize(newsize=(video.w, video.h))

        # Trim the video
        trimmed_clip = rotated_video.subclip(start_time, end_time)

        # Create text to overlay
        water, additive, gypsum = row["water"], row["additive"], row["gypsum"]
        text = f"{experiment_name}: \t Agua: {water} (mL)\tAditivo: {additive} (mL)\tYeso: {gypsum} (g)"

        text_clip = TextClip(
            text,
            fontsize=24,
            color="yellow",
            bg_color="black",
            size=(trimmed_clip.w, 50),
        )
        text_clip = text_clip.set_duration(trimmed_clip.duration)
        text_clip = text_clip.set_position(("right", "top")).set_duration(
            trimmed_clip.duration
        )

        # Overlay text onto the trimmed video
        video_with_text = CompositeVideoClip([trimmed_clip, text_clip])

        # Save the trimmed video
        output_path = os.path.join(output_directory, f"{experiment_name}.mp4")
        video_with_text.write_videofile(output_path, codec="libx264", audio_codec="aac")


print("Video trimming completed!")
