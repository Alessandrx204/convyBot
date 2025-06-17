import asyncio

class Converter:

    @staticmethod
    async def webm2mp4(input_path, output_path):
        conversion = await asyncio.create_subprocess_exec(
            "ffmpeg",
            "-y",                      # Automatically overwrite the output file if it already exists
            "-i", input_path,         # Input file (in .webm format)
            
            # "-vf", "scale='min(1280,iw)':'min(720,ih)':force_original_aspect_ratio=decrease,pad=1280:720:(ow-iw)/2:(oh-ih)/2"
            # FFmpeg video filter to preserve the original aspect ratio without distortion,
            # adapting the video to a fixed resolution (e.g., 1280x720) while ensuring codec compatibility:
            #
            "-vf", "scale=iw:ih:force_original_aspect_ratio=decrease",

            "-c:v", "libx264",        # Video codec: H.264 (widely compatible)
            "-preset", "fast",        # Encoding speed: "fast" balances quality and speed
            "-crf", "23",             # Constant Rate Factor: 23 = good quality, standard value
            "-pix_fmt", "yuv420p",    # Pixel format: ensures compatibility with Telegram and mobile players
            "-c:a", "aac",            # Audio codec: AAC, lightweight and compatible
            "-movflags", "+faststart", output_path,  # Moves metadata to the beginning for fast streaming
        )

        await conversion.communicate()   # Waits for ffmpeg to finish
        print('File converted (hopefully)')  # Helpful debug message
        return conversion.returncode     # Should be 0 if everything went well
