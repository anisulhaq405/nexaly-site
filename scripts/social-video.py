"""Render an 18-second vertical editorial preview from verified source content."""
import subprocess
import tempfile
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

def render_video(item, image_path, output):
    directory = Path(tempfile.mkdtemp(prefix='nexaly-video-'))
    font_dir = Path('/usr/share/fonts/truetype/dejavu')
    heading = ImageFont.truetype(str(font_dir / 'DejaVuSans-Bold.ttf'), 40)
    body_font = ImageFont.truetype(str(font_dir / 'DejaVuSans.ttf'), 30)
    small = ImageFont.truetype(str(font_dir / 'DejaVuSans-Bold.ttf'), 22)
    def wrapped(draw, text, xy, font, width, fill, spacing=12):
        words, lines, current = text.split(), [], ''
        for word in words:
            candidate = (current + ' ' + word).strip()
            if current and draw.textlength(candidate, font=font) > width:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        y = xy[1]
        for line in lines:
            draw.text((xy[0], y), line, font=font, fill=fill)
            y += font.size + spacing
        return y
    for index in range(3):
        image = Image.new('RGB', (720, 1280), '#102c3b')
        draw = ImageDraw.Draw(image)
        draw.rounded_rectangle((36, 50, 684, 112), radius=14, fill='#167a74')
        draw.text((58, 69), 'NEXALYPLANNER  /  ' + item['contentType'].upper(), font=small, fill='white')
        if index == 0:
            wrapped(draw, item['title'], (48, 170), heading, 624, 'white')
            with Image.open(image_path) as feature:
                feature = ImageOps.pad(feature.convert('RGB'), (624, 352), color='#f5f8f7')
                image.paste(feature, (48, 650))
            draw.text((48, 1040), 'A practical planning guide', font=body_font, fill='#aae5d9')
        elif index == 1:
            draw.text((48, 174), 'What this covers', font=heading, fill='white')
            wrapped(draw, item['description'], (48, 290), body_font, 624, '#d9eaed', spacing=18)
        else:
            wrapped(draw, 'Explore the full guide', (48, 240), heading, 624, 'white')
            wrapped(draw, item['title'], (48, 405), body_font, 624, '#d9eaed')
            draw.rounded_rectangle((48, 880, 672, 1020), radius=24, fill='#167a74')
            draw.text((85, 930), 'NexalyPlanner.com', font=heading, fill='white')
            draw.text((48, 1080), 'Full link in the video description', font=small, fill='#aae5d9')
        draw.text((48, 1200), f'{index + 1} / 3', font=small, fill='#aae5d9')
        image.save(directory / f'{index}.png')
    playlist = directory / 'frames.txt'
    playlist.write_text(''.join(f"file '{directory / (str(i) + '.png')}'\nduration 6\n" for i in range(3))
                        + f"file '{directory / '2.png'}'\n")
    result = subprocess.run(['ffmpeg', '-y', '-hide_banner', '-loglevel', 'error', '-f', 'concat', '-safe', '0',
                             '-i', str(playlist), '-t', '18', '-vf', 'fps=24', '-c:v', 'libx264',
                             '-preset', 'fast', '-crf', '24', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                             str(output)], capture_output=True)
    if result.returncode:
        raise RuntimeError('Could not create vertical editorial preview')
    shutil.rmtree(directory)
